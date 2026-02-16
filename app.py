import streamlit as st
from bot.client import get_client
from bot.orders import place_order
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)
from bot.logging_config import setup_logger


st.set_page_config(page_title="Trading Bot", layout="centered")
st.title("🚀 Binance Futures Testnet Trading Bot")

logger = setup_logger()

symbol = st.text_input("Symbol", "BTCUSDT")
side = st.selectbox("Side", ["BUY", "SELL"])
order_type = st.selectbox("Order Type", ["MARKET", "LIMIT"])
quantity = st.number_input("Quantity", min_value=0.0001, step=0.0001)

price = None
if order_type == "LIMIT":
    price = st.number_input("Price", min_value=0.0, step=0.1)

if st.button("Place Order"):
    try:
        symbol = validate_symbol(symbol)
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)
        price = validate_price(price, order_type)

        client = get_client()

        response = place_order(
            client, logger, symbol, side, order_type, quantity, price
        )

        st.success("Order Placed Successfully!")
        st.write("Order ID:", response.get("orderId"))
        st.write("Status:", response.get("status"))
        st.write("Executed Qty:", response.get("executedQty"))
        st.write("Avg Price:", response.get("avgPrice"))

    except Exception as e:
        st.error(f"Order Failed: {str(e)}")
