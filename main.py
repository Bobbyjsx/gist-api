from dotenv import load_dotenv
load_dotenv()
from flask import Flask, request, jsonify
from datetime import datetime
from supabase_py import create_client, Client # type: ignore
import os

app = Flask(__name__)

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

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
    message_list = [{'id': message['id'], 'body': message['body'], 'user_id': message['user_id'],
                      'sent_at': message['sent_at']} for message in messages['data']]
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
    app.run(debug=True)
