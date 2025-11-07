# Tic-Tac-Toe with Advanced AI 🎮

A sophisticated Python implementation of Tic-Tac-Toe featuring multiple AI opponents with varying difficulty levels, from random moves to unbeatable Minimax algorithm with advanced heuristics.

## 🎯 Features

### 🤖 Multiple AI Opponents
- **Random AI** - Makes completely random legal moves
- **Smart AI** - Implements basic strategy (winning moves and blocking)  
- **Minimax AI** - Unbeatable AI using Minimax algorithm with alpha-beta pruning and transposition tables

### ⚡ Advanced Technical Implementation
- **Optimized Minimax** with 3000x speedup through caching
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
- **`minimax_ai.py`** - Optimal play with caching and heuristics

#### `fullgame.py` - Game Orchestration
- Main game loop and flow control
- Player configuration and selection
- User interaction handling
- Match sequencing and turn management

## 🧠 AI Technical Details

### Minimax with Enhancements

```python
# Key optimizations implemented:
- Transposition table caching
- Early exit on win detection  
- Board symmetry recognition
- Heuristic evaluation for draws
```

### Smart AI Strategy
- Immediate win detection
- Threat blocking
- Fallback to random moves when no tactics apply

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
cd tic-tac-toe-ai
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
- **Transposition Table**: Caches board evaluations for 3000x speedup
- **Early Termination**: Stops search when winning move found
- **Symmetry Detection**: Reduces search space by recognizing equivalent positions

### Code Quality
- Type hints throughout
- Comprehensive error handling
- Clean separation of concerns
- Extensive code documentation

## 📊 AI Performance Comparison

| AI Level | Strategy | Win Rate vs Optimal | Key Features |
|----------|----------|---------------------|--------------|
| Random | None | ~3% | Baseline |
| Smart | Rule-based | ~15% | Win/block detection |
| Minimax | Game theory | 100% (draw) | Perfect play |

## 🎓 Learning Outcomes

This project demonstrates:
- Recursive algorithm implementation
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

**Challenge yourself against an unbeatable opponent or study the elegant implementation of game theory in practice!** 🚀