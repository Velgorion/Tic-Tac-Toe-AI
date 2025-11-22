from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.clock import Clock
from engine import get_legal_moves, make_move, get_winner, is_draw
from AIs.minimax_ai import _minimax_score

Window.clearcolor = (0.1, 0.13, 0.17, 1)

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=dp(20), padding=dp(48))
        title = Label(text='Крестики-Нолики', font_size=dp(40), color=(0.9,0.83,0.5,1), bold=True, size_hint=(1,0.2))
        layout.add_widget(title)
        btn1 = Button(text='Играть с человеком', font_size=dp(22), background_color=(0.25,0.5,0.8,1), size_hint=(1,0.18),bold=True)
        btn2 = Button(text='Играть с Искусственным интеллектом', font_size=dp(22), background_color=(0.43,0.76,0.38,1),size_hint=(1,0.18),bold=True)
        btn1.bind(on_press=lambda x:self.manager.current='pvp')
        btn2.bind(on_press=lambda x:self.manager.current='pve')
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        self.add_widget(layout)

class GameBoard(BoxLayout):
    def __init__(self, mode='pvp', **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.mode = mode
        self.board = [[None, None, None] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.players = ['X', 'O']
        self.player_names = ['Вы','Друг'] if mode=='pvp' else ['Вы','Искусственный интеллект']
        self.highlight_color = (0.96,0.55,0.28,1)
        self.status_label = Label(text='Ваш ход (X)',font_size=dp(20),size_hint_y=0.12,color=(0.99,0.97,0.88,1))
        self.add_widget(self.status_label)
        grid = GridLayout(cols=3, size_hint_y=0.75, spacing=dp(8), padding=dp(10))
        self.buttons = []
        for i in range(9):
            btn = Button(text='',font_size=dp(48),background_color=(0.13,0.17,0.19,1),color=(0.8,0.8,0.8,1),bold=True)
            btn.bind(on_press=self.on_button_press)
            self.buttons.append(btn)
            grid.add_widget(btn)
        self.add_widget(grid)
        control = BoxLayout(orientation='horizontal',size_hint_y=0.13, spacing=dp(10))
        restart = Button(text='Новая игра',font_size=dp(18),background_color=(0.19,0.46,0.68,1),bold=True)
        restart.bind(on_press=self.restart_game)
        menu = Button(text='Меню',font_size=dp(18),background_color=(0.99,0.61,0.28,1),bold=True)
        menu.bind(on_press=self.goto_menu)
        control.add_widget(restart)
        control.add_widget(menu)
        self.add_widget(control)

    def on_button_press(self, button):
        if self.game_over:
            return
        index = self.buttons.index(button)
        x, y = index % 3, index // 3
        if self.board[y][x] is not None:
            return
        if self.mode=='pvp' or self.current_player=='X':
            self.make_move(x, y, self.current_player)
            self.check_game_over()
            if self.mode=='pve' and self.current_player=='O' and not self.game_over:
                self.status_label.text=f'Ход {self.player_names[1]} (O)'
                Clock.schedule_once(lambda dt: self.ai_move_sequence(), 0.3)

    def ai_move_sequence(self):
        """Выполняет ход AI и проверяет окончание игры"""
        self.make_ai_move()
        self.check_game_over()
        if not self.game_over:
            self.status_label.text = 'Ваш ход (X)'

    def make_move(self, x, y, player):
        self.board[y][x] = player
        idx = y*3+x
        self.buttons[idx].text = player
        color = (0.2,0.5,1,1) if player=='X' else (0.99,0.61,0.28,1)
        self.buttons[idx].color = color
        self.current_player = 'O' if player=='X' else 'X'
        if self.mode=='pvp' and not self.game_over:
            self.status_label.text=f'Ход {self.player_names[0] if self.current_player=="X" else self.player_names[1]} ({self.current_player})'
        elif self.mode=='pve' and not self.game_over and player=='X':
            pass

    def make_ai_move(self):
        legal_moves = get_legal_moves(self.board)
        best_score = float('-inf')
        best_move = None
        for move in legal_moves:
            new_board = make_move(self.board, move, 'O')
            score = _minimax_score(new_board, 'X', 'O', float('-inf'), float('inf'))
            if score == 10:
                best_move = move
                break
            if score > best_score:
                best_score = score
                best_move = move
        if best_move:
            x,y = best_move
            self.make_move(x,y,'O')

    def check_game_over(self):
        winner = get_winner(self.board)
        if winner:
            self.game_over = True
            self.show_popup('Победа!' if winner=='X' else 'Проигрыш', f'{self.player_names[0] if winner=="X" else self.player_names[1]} выиграл!')
            self.highlight_win(winner)
            return True
        if is_draw(self.board):
            self.game_over = True
            self.show_popup('Ничья','Ничья!')
            return True
        return False

    def highlight_win(self, winner):
        win_patterns = [ [(i,j) for j in range(3)] for i in range(3)] + [ [(j,i) for j in range(3)] for i in range(3)] + [ [(i,i) for i in range(3)], [(i,2-i) for i in range(3)] ]
        for pat in win_patterns:
            vals = [self.board[y][x] for x,y in pat]
            if len(set(vals))==1 and vals[0]==winner:
                for x,y in pat:
                    idx = y*3+x
                    self.buttons[idx].background_color = self.highlight_color

    def show_popup(self,title,msg):
        box = BoxLayout(orientation='vertical',padding=dp(18),spacing=dp(12))
        box.add_widget(Label(text=msg,font_size=dp(22),color=(0.95,0.95,0.92,1)))
        btn = Button(text='Новая игра',font_size=dp(18),background_color=(0.18,0.47,0.77,1),bold=True,size_hint_y=0.34)
        btn.bind(on_press=lambda x: (popup.dismiss(),self.restart_game()))
        box.add_widget(btn)
        popup=Popup(title=title,content=box,size_hint=(0.82,0.5),auto_dismiss=False)
        popup.open()

    def restart_game(self,*a):
        self.board = [[None,None,None] for _ in range(3)]
        self.game_over = False
        self.current_player = 'X'
        for btn in self.buttons:
            btn.text = ''
            btn.background_color=(0.13,0.17,0.19,1)
            btn.color=(0.8,0.8,0.8,1)
        self.status_label.text='Ваш ход (X)' if self.mode=='pve' or self.mode=='pvp' else ''

    def goto_menu(self,*a):
        App.get_running_app().root.current = 'menu'

class GameScreen(Screen):
    def __init__(self,mode,**kwargs):
        super().__init__(**kwargs)
        self.game = GameBoard(mode=mode)
        self.add_widget(self.game)

class TicTacToeApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(GameScreen('pvp', name='pvp'))
        sm.add_widget(GameScreen('pve', name='pve'))
        return sm

if __name__=='__main__':
    TicTacToeApp().run()
