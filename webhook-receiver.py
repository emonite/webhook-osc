from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Get data from the webhook
    data = request.get_data(as_text=True)

    # You can now process the data as plain text
    print("Received data:", data)

    # Return a response
    return 'Success', 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)