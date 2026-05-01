
import argparse
import time
import traceback

from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_input
from bot.logging_config import setup_logging
from bot.client import get_client


def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading pair e.g. BTCUSDT")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=float, required=True, help="Order quantity")
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")

    args = parser.parse_args()

    try:
        
        validate_input(args.symbol, args.side, args.type, args.quantity, args.price)            # Input validation

        print("\n Order Summary:")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")
        if args.type == "LIMIT":
            print(f"Price: {args.price}")

        
        if args.type == "MARKET":                # Place order
            response = place_market_order(args.symbol, args.side, args.quantity)
        else:
            response = place_limit_order(args.symbol, args.side, args.quantity, args.price)

        
        print("\n Initial Response:")            # Raw response (debug + logging clarity)
        print(response)

    
        order_id = response.get("orderId")       # Extract basic info
        status = response.get("status")

        print("\n📌 Order Info:")
        print(f"Order ID: {order_id}")
        print(f"Initial Status: {status}")

        
        print("\n⏳ Waiting for order execution...")      # Wait for execution
        time.sleep(2)

        client = get_client()

        order_status = client.futures_get_order(
            symbol=args.symbol,
            orderId=order_id
        )

        print("\n Updated Order Status:")
        print(f"Status: {order_status.get('status')}")
        print(f"Executed Qty: {order_status.get('executedQty')}")
        print(f"Avg Price: {order_status.get('avgPrice', 'N/A')}")

        print("\n Order process completed")

    except Exception:
        print("\n FULL ERROR:")
        traceback.print_exc()


if __name__ == "__main__":
    main()

