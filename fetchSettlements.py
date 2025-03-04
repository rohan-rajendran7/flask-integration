from cashfree_pg.api_client import Cashfree
import os
from dotenv import load_dotenv

load_dotenv()

Cashfree.XClientId = os.getenv("CASHFREE_CLIENT_ID")
Cashfree.XClientSecret = os.getenv("CASHFREE_CLIENT_SECRET")
Cashfree.XEnvironment = Cashfree.XSandbox
x_api_version = "2023-08-01"

def fetchSettlements(order_id):
    try:
        api_response = Cashfree().PGOrderFetchSettlement(x_api_version=x_api_version, order_id=order_id)
        print(api_response.data)
    except Exception as e:
        print("exception", e)

fetchSettlements("order_103723062tX4D99sbkNj8ZMGRD8NLHP8P88")