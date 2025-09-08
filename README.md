# Trading Bot

A simple, modular trading bot project written in Python. This repository provides a basic framework for building, configuring, and running automated trading strategies.

## Features
- Modular codebase for easy extension
- CLI interface for managing the bot
- Logging support
- Configurable via `.env`
- Utility functions for common tasks

## Project Structure
```
trading_bot/
├── bot.py              # Core trading bot logic
├── cli.py              # Command-line interface for the bot
├── config.py           # Configuration settings
├── main.py             # Main entry point
├── requirements.txt     # Python dependencies
├── test_connection.py  # Script to test API or broker connection
├── utils.py            # Utility functions
├── logs/
│   └── bot.log         # Log files
└── __pycache__/        # Python cache files
```

## Getting Started

### Prerequisites
- Python 3.7+

### Installation
1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd trading_bot
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Usage
- Run the main bot:
  ```sh
  python main.py
  ```
- Use the CLI:
  ```sh
  python cli.py [options]
  ```
- Test your connection:
  ```sh
  python test_connection.py
  ```

## Configuration
Edit `.env` to set your API keys, trading parameters, and other settings.

## Logging
Logs are stored in the `logs/` directory. Check `bot.log` for runtime information and errors.

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.
