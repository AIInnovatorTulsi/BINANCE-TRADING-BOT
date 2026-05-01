import logging
from bot.client import get_client

logger = logging.getLogger(__name__)

client = get_client()

def place_market_order(symbol, side, quantity):
    try:
        logger.info(f"Placing MARKET order: {symbol} {side} {quantity}")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logger.info(f"Response: {order}")
        return order

    except Exception as e:
        logger.error(f"Error placing MARKET order: {e}")
        raise


def place_limit_order(symbol, side, quantity, price):
    try:
        logger.info(f"Placing LIMIT order: {symbol} {side} {quantity} @ {price}")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(f"Response: {order}")
        return order

    except Exception as e:
        logger.error(f"Error placing LIMIT order: {e}")
        raise