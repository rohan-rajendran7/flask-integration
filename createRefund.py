import requests, os
from dotenv import load_dotenv
from cashfree_pg.models.order_create_refund_request import OrderCreateRefundRequest
from cashfree_pg.api_client import Cashfree


load_dotenv()

Cashfree.XClientId = os.getenv("CASHFREE_CLIENT_ID")
Cashfree.XClientSecret = os.getenv("CASHFREE_CLIENT_SECRET")
Cashfree.XEnvironment = Cashfree.XSandbox
x_api_version = "2023-08-01"

def createRefund(order_id, amount,refund_id):
    refundRequest=OrderCreateRefundRequest(
        refund_amount=amount,
        refund_id=refund_id,
        refund_speed = "INSTANT"
    )
    try:
        api_response = Cashfree().PGOrderCreateRefund(x_api_version=x_api_version, order_id=order_id, order_create_refund_request=refundRequest)
        print(api_response.data)
    except Exception as e:
        print(e)

createRefund("order_103723062tX4D99sbkNj8ZMGRD8NLHP8P88", 1, "ref_order_P881")
