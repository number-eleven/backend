from flask import Blueprint

import api.v0.routes  # pylint: disable=cyclic-import

api_v0 = Blueprint('mod_api_v0', __name__)
