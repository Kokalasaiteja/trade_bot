# Binance Futures Testnet Trading Bot

A simplified Python trading bot that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).

This project was built as part of the Python Developer Internship assignment.

---

## 🚀 Features

- Place MARKET orders
- Place LIMIT orders
- Supports BUY and SELL sides
- CLI-based input using argparse
- Structured project architecture
- Logging of API requests and responses
- Proper input validation
- Exception handling
- Optional Streamlit UI (Bonus)

## Live Link:
https://tradebot-project.streamlit.app/

---

## 🏗 Project Structure
trading_bot/ <br>
│<br>
├── bot/<br>
│ ├── init.py<br>
│ ├── client.py<br>
│ ├── orders.py<br>
│ ├── validators.py<br>
│ └── logging_config.py<br>
│<br>
├── cli.py<br>
├── app.py<br>
├── requirements.txt<br>
└── README.md<br>


---

## 🔧 Setup Instructions

## 1️⃣ Clone the Repository
git clone https://github.com/your-username/trade_bot.git
cd trade_bot

## 2️⃣ Create Virtual Environment (Recommended)
python -m venv venv

## Activate:
## Windows
venv\Scripts\activate

## Mac/Linux
source venv/bin/activate

## 3️⃣ Install Dependencies
pip install -r requirements.txt

## 4️⃣ Create Binance Futures Testnet Account
- Go to: https://testnet.binancefuture.com
- Register/Login
- Generate API Keys from API Management

## 5️⃣ Create .env File
In the root project folder, create a file named:
.env

## Add your API credentials:
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_secret_key

⚠️ Do NOT push .env to GitHub.

## 🖥 Running the Application (CLI)
▶ MARKET Order Example
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

▶ LIMIT Order Example
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000

## 🖥 Running Streamlit UI (Optional Bonus)
- streamlit run app.py
- Open browser at: http://localhost:8501

## 📄 Output
When placing an order, the application prints:
- Order request summary
- Order ID
- Status
- Executed Quantity
- Average Price (if available)
- Success / Failure message

## 📝 Logging
All API requests, responses, and errors are logged to:
- logs/trading_bot.log

Logs include:
- MARKET order execution
- LIMIT order execution
- Any validation or API errors

## ⚠ Deployment Note
- Due to Binance geo restrictions, live order execution may not work on certain cloud-hosted environments.
- The application works fully when executed locally.

## 📦 Requirements
- Python 3.x
- python-binance
- python-dotenv
- streamlit (optional bonus)
