from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Get JSON data from the webhook
    data = request.json

    # Print the received JSON data
    print("Received JSON data:", data)

    # You can now process the data
    # For example, you can access values like data['key_name']

    # Return a response
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)