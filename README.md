# Tic-Tac-Toe with Advanced AI 🎮

A sophisticated Python implementation of Tic-Tac-Toe featuring multiple AI opponents with varying difficulty levels, from random moves to unbeatable Minimax algorithm with advanced optimizations.

## 🎯 Features

### 🤖 Multiple AI Opponents
- **Random AI** - Makes completely random legal moves
- **Smart AI** - Implements basic strategy (winning moves and blocking)  
- **Minimax AI** - Unbeatable AI using Minimax algorithm with alpha-beta pruning and transposition tables

### ⚡ Advanced Technical Implementation
- **Optimized Minimax** with alpha-beta pruning and caching
- **Position evaluation heuristics** for strategic play
- **Symmetry recognition** - understands equivalent board positions
- **Early exit optimization** - stops searching when win is found

### 🎮 Game Features
- Clean console-based interface with coordinate system
- Flexible player configuration (Human vs AI, AI vs AI)
- Choice of first player
- Real-time board visualization
- Input validation and error handling

## 🏗️ Architecture

The project follows a modular architecture with clear separation of concerns:

### Core Modules

#### `engine.py` - Game Engine
- Board state management
- Win condition detection
- Move validation and execution
- Board rendering
- Position evaluation heuristics

#### `AIs/` - AI Implementations Directory
- **`random_ai.py`** - Baseline random moves
- **`smart_ai.py`** - Rule-based strategy with win/block detection
- **`minimax_ai.py`** - Optimal play with alpha-beta pruning and caching

#### `fullgame.py` - Game Orchestration
- Main game loop and flow control
- Player configuration and selection
- User interaction handling
- Match sequencing and turn management

## 🧠 AI Technical Details

### Minimax with Alpha-Beta Pruning

```python
# Key optimizations implemented:
- Alpha-beta pruning for search reduction
- Transposition table caching
- Early exit on win detection
- Board symmetry recognition
- Heuristic evaluation for draws
```

### Performance Achievements
- **Minimax vs Minimax**: ~2300 games per second
- **Smart search reduction** through branch elimination
- **Intelligent caching** with composite keys

### Heuristic Evaluation
The AI evaluates positions based on:
- Center control (highest priority)
- Corner positions
- Potential winning lines
- Strategic board patterns

## 🚀 Installation & Usage

### Requirements
- Python 3.6+

### Running the Game

```bash
# Clone and run
git clone <repository-url>
cd Tic-Tac-Toe-AI
python fullgame.py
```

### Game Setup
1. Choose player types for X and O:
   - `1` - Random AI
   - `2` - Smart AI  
   - `3` - Minimax AI (unbeatable)
   - `4` - Human player

2. Select who moves first (X or O)

3. For human players:
   - Enter coordinates (0-2) for X and Y positions
   - Board uses standard matrix coordinates

## 🎯 Gameplay Example

```
  0 1 2
 - - -
0| | | |
1| | | |
2| | | |
 - - -
```

Human vs Minimax AI match demonstrating optimal play.

## 🔧 Technical Highlights

### Performance Optimizations
- **Alpha-Beta Pruning**: Significantly reduces search space
- **Transposition Table**: Caches board evaluations
- **Early Termination**: Stops search when winning move found
- **Symmetry Detection**: Recognizes equivalent board positions

### Code Quality
- Type hints throughout
- Comprehensive error handling
- Clean separation of concerns
- Extensive code documentation

## 📊 AI Performance

| AI Level | Strategy | Speed (games/sec) | Key Features |
|----------|----------|-------------------|--------------|
| Random | None | ~1000 | Baseline |
| Smart | Rule-based | ~800 | Win/block detection |
| Minimax | Alpha-Beta | ~2300 | Optimal play |

## 🎓 Learning Outcomes

This project demonstrates:
- Advanced recursive algorithm optimization
- Game theory concepts (Minimax)
- Performance optimization techniques
- AI heuristic design
- Software architecture patterns

## 🤝 Contributing

Feel free to fork and enhance:
- Add GUI interface
- Implement machine learning approaches
- Extend to larger board sizes
- Add tournament mode

## 📝 License

MIT License - feel free to use this project for learning and development!

---

**Challenge yourself against an unbeatable opponent or study the implementation of game theory in practice!** 🚀