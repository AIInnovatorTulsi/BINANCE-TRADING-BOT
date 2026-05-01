<<<<<<< HEAD
# BINANCE-PROJECT
=======
# BINANCE-TRADING-BOT

# BINANCE-PROJECT

#  Binance Futures Testnet Trading Bot

A simple, structured Python-based CLI trading bot that places **MARKET** and **LIMIT** orders on Binance Futures Testnet (USDT-M).
Built with clean architecture, input validation, logging, and error handling.

---

##  Features

*  Place **MARKET** orders (BUY / SELL)
*  Place **LIMIT** orders (BUY / SELL)
*  CLI-based input using `argparse`
*  Input validation (symbol, side, quantity, price)
*  Structured code (modular design)
*  Logging of requests, responses, and errors
*  Exception handling with full traceback
*  Order execution status tracking

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py          # Binance client setup
│   ├── orders.py          # Order placement logic
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging setup
│
├── cli.py                 # CLI entry point
├── requirements.txt
├── README.md
└── logs/
    └── app.log            # Log file (auto-generated)
```



## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd trading_bot
```

---

### 2. Create virtual environment (recommended)

```bash
python -m venv venv
```

Activate:

* Windows:

```bash
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## API Setup (IMPORTANT)

1. Go to Binance Futures Testnet:
   https://testnet.binancefuture.com

2. Login (no KYC required)

3. Navigate to:
   Profile → API Management

4. Create API Key (System Generated)

5. Copy:

   * API Key
   * API Secret

---

### 4. Create `.env` file

In the root directory:

```
API_KEY=your_api_key_here
API_SECRET=your_api_secret_here
```

---

## Add Testnet Funds

* Use the Testnet Faucet to add USDT balance
* Required to place orders successfully

---

## Usage

### MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

### LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 76000
```

---

## Sample Output

```
 Order Summary:
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

 Initial Response:
{...}

 Order Info:
Order ID: 12345678
Initial Status: NEW

 Waiting for order execution...

 Updated Order Status:
Status: FILLED
Executed Qty: 0.001
Avg Price: 63000

 Order process completed
```

---

## Logging

* Logs are stored in:

```
logs/app.log
```

* Includes:

  * Order requests
  * API responses
  * Errors


## Assumptions

* Only USDT-M Futures Testnet is used
* User provides valid symbol (e.g., BTCUSDT)
* Quantity follows Binance minimum requirements
* LIMIT order price must follow market rules:

  * BUY → below market price
  * SELL → above market price


## Error Handling

Handles:

* Invalid CLI inputs
* API errors (Binance exceptions)
* Network failures
* Missing parameters


>>>>>>> 8d9ead48d7881220e9944afb315cdf6405f666e7
