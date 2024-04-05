from flask import Flask, request, jsonify
import boto3

# Initialize Flask app
app = Flask(__name__)

# AWS credentials and region
AWS_ACCESS_KEY_ID = 'YOUR_AWS_ACCESS_KEY_ID'
AWS_SECRET_ACCESS_KEY = 'YOUR_AWS_SECRET_ACCESS_KEY'
AWS_REGION = 'YOUR_AWS_REGION'

# Initialize AWS SNS client
sns_client = boto3.client('sns', 
                          aws_access_key_id=AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                          region_name=AWS_REGION)

# Route for sending message
@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        # Get user input (email or phone number)
        recipient = request.json.get('recipient')

        # Message to send
        message = "This is a test message sent via AWS SNS."

        # Send message
        response = sns_client.publish(
            Message=message,
            TargetArn=recipient
        )

        # Check if message sending was successful
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return jsonify({'status': 'success', 'message': 'Message sent successfully.'}), 200
        else:
            return jsonify({'status': 'error', 'message': 'Failed to send message.'}), 500

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
