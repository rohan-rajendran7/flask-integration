import requests
import os
from dotenv import load_dotenv


def fetchRefundDetails(order_id):
    load_dotenv()
    url = f"https://sandbox.cashfree.com/pg/orders/{order_id}/refunds"
    XClientId = os.getenv("CASHFREE_CLIENT_ID")
    XClientSecret = os.getenv("CASHFREE_CLIENT_SECRET")
    headers = {
        "x-client-id": XClientId,
        "x-client-secret": XClientSecret,
        "x-api-version": "2023-08-01"
    }
    response = requests.request("GET", url, headers=headers)
    print(response.text)

fetchRefundDetails("order_103723062to2dSY3xcJRI7TDxcAYYXVpKGr")