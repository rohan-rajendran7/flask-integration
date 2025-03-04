from cashfree_pg.api_client import Cashfree
import os
from dotenv import load_dotenv

load_dotenv()


Cashfree.XClientId = os.getenv("CASHFREE_CLIENT_ID")
Cashfree.XClientSecret = os.getenv("CASHFREE_CLIENT_SECRET")
Cashfree.XEnvironment = Cashfree.SANDBOX
x_api_version = "2023-08-01"

def verifyOrder(orderID):
    try:
        api_response = Cashfree().PGFetchOrder(x_api_version, orderID, None)
        return (api_response.data)
    except Exception as e:
        print(e)
