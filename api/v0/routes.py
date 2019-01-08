from . import api_v0

@api_v0.route('/user', methods=['GET'])
def user_route():
    return {}