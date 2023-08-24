from dotenv import load_dotenv
import uvicorn
load_dotenv()
from flask import Flask, request, jsonify
from datetime import datetime
from supabase_py import create_client, Client # type: ignore
import os

app = Flask(__name__)

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

@app.route('/', methods=['GET'])
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            /* Your existing styles */

            /* New styles for documentation */
            .endpoint {
                margin: 20px 0;
                border: 1px solid #ddd;
                padding: 20px;
                border-radius: 8px;
            }
            .endpoint h2 {
                margin-top: 0;
            }
            .method {
                color: #007bff;
                font-weight: bold;
            }
            .input-output {
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to Gist API</h1>
            <p>This is a simple Flask API homepage.</p>
            
            <!-- Documentation for the endpoints -->
            
            <div class="endpoint">
                <h2>/users (GET)</h2>
                <p>Get a list of users.</p>
                <div class="input-output">
                    <h3>Input:</h3>
                    <p>None</p>
                    <h3>Output:</h3>
                    <pre>
[
    {
        "id": 1,
        "name": "John Doe",
        ...
    },
    ...
]
                    </pre>
                </div>
            </div>
            
            <div class="endpoint">
                <h2>/users/&lt;id&gt; (PUT)</h2>
                <p>Update user information.</p>
                <div class="input-output">
                    <h3>Input:</h3>
                    <pre>
{
    "name": "Updated Name",
    ...
}
                    </pre>
                    <h3>Output:</h3>
                    <pre>
{
    "message": "endpoint isn't fully ready"
}
                    </pre>
                </div>
            </div>
            
            <div class="endpoint">
                <h2>/signup (POST)</h2>
                <p>Sign up a new user.</p>
                <div class="input-output">
                    <h3>Input:</h3>
                    <pre>
{
    "name": "New User",
    ...
}
                    </pre>
                    <h3>Output:</h3>
                    <pre>
{
    "message": "Supabase API response"
}
                    </pre>
                </div>
            </div>
            
            <div class="endpoint">
                <h2>/messages (GET)</h2>
                <p>Get a list of messages.</p>
                <div class="input-output">
                    <h3>Input:</h3>
                    <p>None</p>
                    <h3>Output:</h3>
                    <pre>
[
    {
        "id": 1,
        "body": "Hello",
        "user_id": 1,
        "sent_at": "2023-08-21T12:34:56Z"
    },
    ...
]
                    </pre>
                </div>
            </div>
            
            <div class="endpoint">
                <h2>/messages (POST)</h2>
                <p>Create a new message.</p>
                <div class="input-output">
                    <h3>Input:</h3>
                    <pre>
{
    "body": "New message body",
    "user_id": 1
}
                    </pre>
                    <h3>Output:</h3>
                    <pre>
{
    "message": "Supabase API response"
}
                    </pre>
                </div>
            </div>
            
            <div class="endpoint">
                <h2>/messages/&lt;message_id&gt; (DELETE)</h2>
                <p>Delete a message by ID.</p>
                <div class="input-output">
                    <h3>Input::</h3>
                    <p>None</p>
                    <h3>Output:</h3>
                    <pre>
{
    "message": "Supabase API response"
}
                    </pre>
                </div>
            </div>

        </div>
    </body>
    </html>
    """



@app.route('/users', methods=['GET'])
def get_users():
    users = supabase.table('users').select().execute()
    return jsonify(users)

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.json
    # user = supabase.table('users').update(data).eq('id', id).execute()
    return jsonify({'message':"endpoint isn't fully ready"})


@app.route("/signup", methods=["POST"])
def signup():
        """get users info from the frontend"""
        data = request.json
        result = supabase.table("users").insert(data).execute()
        return jsonify(result)

@app.route('/messages', methods=['GET'])
def get_messages():
    messages = supabase.table('messages').select().execute()
    message_list = []
    for message in messages['data']:
        user_id = message.get('user_id', None)  # Use None as default value if 'user_id' is missing
        message_item = {
            'id': message['id'],
            'body': message['body'],
            'user_id': user_id,
            'sent_at': message['sent_at']
        }
        message_list.append(message_item)

    return jsonify(message_list)

@app.route('/messages', methods=['POST'])
def create_message():
    data = request.json
    result = supabase.table("messages").insert(data).execute()
    return jsonify(result)

@app.route('/messages/<message_id>', methods=['DELETE'])
def delete_message(message_id):
    result = supabase.table('messages').delete().eq("id", message_id).execute()
    return jsonify(result)

if __name__ == '__main__':
    # uvicorn.run(app, host="0.0.0.0", port=8000)
    app.run()
