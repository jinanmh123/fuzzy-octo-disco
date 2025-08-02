from flask import Flask, request, jsonify
import os
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/submit-email', methods=['POST'])
def submit_email():
    email = request.json.get('email')

    if not email:
        return jsonify({"error": "Email is required"}), 400

    try:
        with open("emails.txt", "a") as file:
            file.write(email + "\n")
        return jsonify({"message": "Email saved successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
