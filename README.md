# Four-in-a-Row Game 🔴🟡

A classic Connect Four game implementation in Python featuring multiple game modes and customizable win conditions.

## 📋 Table of Contents

- [✨ Features](#-features)
- [🎮 Game Modes](#-game-modes)
- [🚀 Installation](#-installation)
- [🎯 Usage](#-usage)
- [📖 Game Rules](#-game-rules)
- [📁 Project Structure](#-project-structure)
- [🤝 Contributing](#-contributing)

## ✨ Features

- **Two Game Modes**: Player vs Player and Player vs Bot
- **Customizable Win Condition**: Choose between 3, 4, or 5 in a row
- **Smart Bot AI**: Bot can detect winning moves and play strategically
- **Clean Console Interface**: Clear terminal display with real-time board updates
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 🎮 Game Modes

### Player vs Player (Duo)

Two human players take turns dropping pieces into the board to achieve the target number in a row.

### Player vs Bot

Play against an AI opponent that can:

- Detect and execute winning moves
- Provide challenging gameplay with strategic placement

## 🚀 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/BIGGASSS/four-in-a-row.git
   cd four-in-a-row
   ```

2. **Ensure Python is installed:**
   This game requires Python 3.6 or higher. No additional dependencies needed!

## 🎯 Usage

Run the game using Python:

```bash
# Windows
python main.py

# macOS/Linux
python3 main.py
```

### Game Setup

1. **Choose Win Condition**: Select 3, 4, or 5 in a row (default: 4)
2. **Select Game Mode**: Choose between "duo" (Player vs Player) or "bot" (Player vs Bot)
3. **Start Playing**: Take turns dropping pieces into columns (1-7)

## 📖 Game Rules

- The board consists of a 6x7 grid
- Players take turns dropping colored pieces into columns
- Pieces fall to the lowest available position in the selected column
- Win by connecting the chosen number of pieces (3-5) in a row:
  - Horizontally
  - Vertically
  - Diagonally (both directions)
- Player 1 uses pieces marked as `1`, Player 2/Bot uses pieces marked as `2`

## 📁 Project Structure

```text
four-in-a-row/
├── main.py          # Main game loop and user interface
├── board.py         # Board class with game logic
├── utils.py         # Utility functions (screen clearing, random numbers)
├── README.md        # Project documentation
└── __pycache__/     # Python bytecode cache
```

### Core Components

- **`Board` class**: Handles game board operations, win detection, and bot AI
- **Game Loop**: Manages player turns, input validation, and game state
- **Utility Functions**: Cross-platform screen clearing and random number generation

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

- Report bugs or issues
- Suggest new features
- Improve the bot AI strategy
- Enhance the user interface
- Add more customization options

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🎮 Enjoy the Game

Have fun playing Four-in-a-Row! Whether you're challenging a friend or testing your skills against the bot, may the best strategist win! 🏆
