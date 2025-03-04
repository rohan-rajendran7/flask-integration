from flask import Flask, render_template, request, flash, redirect
from createOrder import create_order
from verifyOrder import verifyOrder
from createPaymentLinks import create_payment_links
from flask_cors import CORS
from fetchPaymentLink import fetchPaymentLinkDetails

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/pay', methods = ['GET', 'POST'])
def pay():
    data = {}
    if request.method == 'POST':
        data = request.get_json()
        amount = data.get('amount')
        phone = data.get('phone')  
        data = create_order(phone, amount)
        return data
    else:
        return render_template('pay.html')
    
@app.route('/verify', methods = ['GET'])
def verifyOrderStatus():
    return render_template('verify.html')

@app.route('/verify/<order_id>', methods = ['GET'])
def verifyStatus(order_id):
    # order_id = request.args.get('order_id')
    status = verifyOrder(order_id)
    print(status.order_status, "actual status")
    return status.order_status

@app.route('/orderPay', methods = ['GET', 'POST'])
def orderPay():
    if request.method == 'POST':
        data = request.get_json()
        amount = data.get('amount')
        phone = data.get('phone')  
        data = create_order(phone, amount)
        return data
    else:
        return render_template('orderPay.html')

@app.route('/paymentLink', methods =['GET'])
def paymentLink():
    return render_template('paymentLinks.html')

@app.route('/createPaymentLink', methods = ['POST'])
def createPaymentLink():
    data = request.get_json()
    payment_link_data = {}
    payment_link_data["link_id"] = data.get('link_id')
    payment_link_data["link_amount"] = int(data.get('link_amount')) 
    payment_link_data["link_purpose"] = data.get('link_purpose')  
    payment_link_data["customer_phone"] = data.get('customer_phone')
    payment_link_data["customer_email"] = data.get('customer_email')  
    payment_link_data["send_sms"] = data.get('send_sms')
    payment_link_data["send_email"] = data.get('send_email')
    response = create_payment_links(payment_link_data)
    if response["status"] == "success":
        return redirect('/')
    else:
        print("Payment link creation failed: " + response["message"])
        return render_template('verify.html')
    
@app.route('/fetchPaymentLink', methods = ['GET'])
def verifyPaymentStatus():
    return render_template('fetchPaymentLinks.html')

@app.route('/fetchPaymentStatus/<order_id>', methods = ['GET'])
def FetchStatus(order_id):
    # order_id = request.args.get('order_id')
    status = fetchPaymentLinkDetails(order_id)
    return status.link_url


if __name__ == '__main__':
    app.run(debug=True) 