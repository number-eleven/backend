from flask import jsonify, request

from api.v0 import api_v0

from .controllers import get_user, get_chat, get_message


@api_v0.route('/user', methods=['GET'])
def user_route():
    user_id = request.args.get('id')

    return jsonify(get_user(user_id))


@api_v0.route('/chat', methods=['GET'])
def chat_route():
    chat_id = request.args.get('id')

    return jsonify(get_chat(chat_id))


@api_v0.route('/messages', methods=['GET'])
def message_route():
    message_id = request.args.get('id')

    return jsonify(get_message(message_id))
