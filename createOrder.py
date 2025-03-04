from cashfree_pg.models.create_order_request import CreateOrderRequest
from cashfree_pg.api_client import Cashfree
from cashfree_pg.models.customer_details import CustomerDetails
import os
from dotenv import load_dotenv
from cashfree_pg.models.order_meta import OrderMeta


load_dotenv()

Cashfree.XClientId = os.getenv("CASHFREE_CLIENT_ID")
Cashfree.XClientSecret = os.getenv("CASHFREE_CLIENT_SECRET")
Cashfree.XEnvironment = Cashfree.XSandbox
x_api_version = "2023-08-01"

def create_order(phoneNo=None, amount=None):
    if phoneNo is None:
        phoneNo = "9489437364"
    if amount is None:
        amount = 12

    customerDetails = CustomerDetails(customer_id="123", customer_phone=phoneNo)
    order_meta = OrderMeta(return_url="http://127.0.0.1:5000/", notify_url = "https://webhook.site/149bdb5c-77f7-4b3b-aca4-e016e67fee1f",)
    createOrderRequest = CreateOrderRequest(order_amount= amount, order_currency="INR", customer_details=customerDetails, order_meta = order_meta)
    try:
        api_response = Cashfree().PGCreateOrder(x_api_version, createOrderRequest, None, None)
        print(api_response.data)
        return {"session_id": api_response.data.payment_session_id, "order_id": api_response.data.order_id}
    except Exception as e:
        print("Encountered exception", e)


create_order('9489437364', 12)
