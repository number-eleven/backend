from flask import Blueprint

api_v0 = Blueprint('mod_api_v0', __name__)

import api.v0.routes  # pylint: disable=cyclic-import,wrong-import-position  # noqa: E402
