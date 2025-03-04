from cashfree_pg.api_client import Cashfree
from cashfree_pg.models.create_link_request import CreateLinkRequest
from cashfree_pg.models.link_customer_details_entity import LinkCustomerDetailsEntity
from cashfree_pg.models.link_notify_entity import LinkNotifyEntity
from dotenv import load_dotenv
import os

def create_payment_links(payment_link_data):

    load_dotenv()

    Cashfree.XClientId = os.getenv("CASHFREE_CLIENT_ID")
    Cashfree.XClientSecret = os.getenv("CASHFREE_CLIENT_SECRET")
    Cashfree.XEnvironment = Cashfree.XSandbox

    create_link_request = CreateLinkRequest(
        link_id=payment_link_data["link_id"],
        link_amount=payment_link_data["link_amount"],
        link_currency="INR",
        link_purpose=payment_link_data["link_purpose"],
        customer_details=LinkCustomerDetailsEntity(customer_phone=payment_link_data["customer_phone"], customer_email = payment_link_data["customer_email"]),
        link_notify=LinkNotifyEntity(send_sms=True, send_email = True),
        enable_invoice = True
    )
    try:
        api_response = Cashfree().PGCreateLink(x_api_version="2023-08-01", create_link_request=create_link_request)
        return {"status": "success", "data": api_response.data}
    except Exception as e:
        print("Exception", e)
        return {"status": "failure", "message": str(e)}