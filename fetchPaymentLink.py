from cashfree_pg.api_client import Cashfree
import os
from dotenv import load_dotenv

load_dotenv()


Cashfree.XClientId = os.getenv("CASHFREE_CLIENT_ID")
Cashfree.XClientSecret = os.getenv("CASHFREE_CLIENT_SECRET")
Cashfree.XEnvironment = Cashfree.SANDBOX
x_api_version = "2023-08-01"

def fetchPaymentLinkDetails(linkID):
    try:
        api_response = Cashfree().PGFetchLink(x_api_version="2023-08-01", link_id=linkID)
        print("inside fetchPaymentLinkDetails", api_response.data, "\n", type(api_response))
        return(api_response.data)
    except Exception as e:
        print(e)

