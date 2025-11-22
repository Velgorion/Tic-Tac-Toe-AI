from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.metrics import dp

from engine import get_legal_moves, make_move, get_winner, is_draw
from AIs.minimax_ai import _minimax_score

Window.clearcolor = (0.95, 0.95, 0.95, 1)


class TicTacToeGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = dp(20)
        self.spacing = dp(15)
        
        # Game state
        self.board = [[None, None, None] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.player_mode = 'X'  # Player always plays as X
        self.ai_mode = 'O'      # AI always plays as O
        
        # Title
        title = Label(
            text='Крестики-Нолики',
            font_size=dp(32),
            size_hint_y=0.15,
            color=(0.2, 0.2, 0.2, 1),
            bold=True
        )
        self.add_widget(title)
        
        # Status label
        self.status_label = Label(
            text='Ваш ход (X)',
            font_size=dp(20),
            size_hint_y=0.1,
            color=(0.3, 0.3, 0.3, 1)
        )
        self.add_widget(self.status_label)
        
        # Game grid
        self.grid = GridLayout(
            cols=3,
            spacing=dp(10),
            size_hint_y=0.6
        )
        
        self.buttons = []
        for i in range(9):
            btn = Button(
                text='',
                font_size=dp(48),
                bold=True,
                background_color=(1, 1, 1, 1),
                background_normal='',
                color=(0.2, 0.2, 0.2, 1)
            )
            btn.bind(on_press=self.on_button_press)
            self.buttons.append(btn)
            self.grid.add_widget(btn)
        
        self.add_widget(self.grid)
        
        # Control buttons
        control_layout = BoxLayout(
            orientation='horizontal',
            spacing=dp(10),
            size_hint_y=0.15
        )
        
        restart_btn = Button(
            text='Новая игра',
            font_size=dp(18),
            background_color=(0.2, 0.6, 0.8, 1),
            background_normal=''
        )
        restart_btn.bind(on_press=self.restart_game)
        control_layout.add_widget(restart_btn)
        
        difficulty_btn = Button(
            text='Уровень: Minimax',
            font_size=dp(18),
            background_color=(0.6, 0.2, 0.8, 1),
            background_normal='',
            disabled=True
        )
        control_layout.add_widget(difficulty_btn)
        
        self.add_widget(control_layout)
    
    def on_button_press(self, button):
        if self.game_over:
            return
        
        if self.current_player != self.player_mode:
            return
        
        # Get button index
        index = self.buttons.index(button)
        x, y = index % 3, index // 3
        
        # Check if move is valid
        if self.board[y][x] is not None:
            return
        
        # Make player move
        self.make_move(x, y, self.player_mode)
        
        # Check game state
        if self.check_game_over():
            return
        
        # AI move
        self.current_player = self.ai_mode
        self.status_label.text = 'Ход AI...'
        self.make_ai_move()
        
        # Check game state after AI
        self.check_game_over()
    
    def make_move(self, x, y, player):
        self.board[y][x] = player
        index = y * 3 + x
        self.buttons[index].text = player
        
        if player == 'X':
            self.buttons[index].color = (0.2, 0.4, 0.8, 1)
        else:
            self.buttons[index].color = (0.8, 0.2, 0.2, 1)
    
    def make_ai_move(self):
        # Use minimax to find best move
        best_score = float('-inf')
        best_move = None
        
        legal_moves = get_legal_moves(self.board)
        
        for move in legal_moves:
            new_board = make_move(self.board, move, self.ai_mode)
            score = _minimax_score(new_board, self.player_mode, self.ai_mode, float('-inf'), float('inf'))
            
            if score == 10:
                best_move = move
                break
            
            if score > best_score:
                best_score = score
                best_move = move
        
        if best_move:
            x, y = best_move
            self.make_move(x, y, self.ai_mode)
            self.current_player = self.player_mode
            self.status_label.text = 'Ваш ход (X)'
    
    def check_game_over(self):
        winner = get_winner(self.board)
        
        if winner:
            self.game_over = True
            if winner == self.player_mode:
                self.show_popup('Победа!', 'Вы выиграли! 🎉')
            else:
                self.show_popup('Поражение', 'AI победил! 🤖')
            return True
        
        if is_draw(self.board):
            self.game_over = True
            self.show_popup('Ничья', 'Ничья! 🤝')
            return True
        
        return False
    
    def show_popup(self, title, message):
        content = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))
        
        msg_label = Label(
            text=message,
            font_size=dp(20),
            color=(0.2, 0.2, 0.2, 1)
        )
        content.add_widget(msg_label)
        
        btn_layout = BoxLayout(spacing=dp(10), size_hint_y=0.3)
        
        restart_btn = Button(
            text='Новая игра',
            background_color=(0.2, 0.6, 0.8, 1),
            background_normal=''
        )
        btn_layout.add_widget(restart_btn)
        
        close_btn = Button(
            text='Закрыть',
            background_color=(0.6, 0.6, 0.6, 1),
            background_normal=''
        )
        btn_layout.add_widget(close_btn)
        
        content.add_widget(btn_layout)
        
        popup = Popup(
            title=title,
            content=content,
            size_hint=(0.8, 0.4),
            auto_dismiss=False
        )
        
        restart_btn.bind(on_press=lambda x: (popup.dismiss(), self.restart_game(None)))
        close_btn.bind(on_press=popup.dismiss)
        
        popup.open()
    
    def restart_game(self, instance):
        self.board = [[None, None, None] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.status_label.text = 'Ваш ход (X)'
        
        for btn in self.buttons:
            btn.text = ''
            btn.color = (0.2, 0.2, 0.2, 1)


class TicTacToeApp(App):
    def build(self):
        return TicTacToeGame()


if __name__ == '__main__':
    TicTacToeApp().run()
