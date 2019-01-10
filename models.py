from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

# unsure if this is necessary


class BaseModel(db.Model):
    # base data model for all objects
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        # define a base way to print models
        return "%s(%s)" % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

    def json(self):
        # define a base way to jsonify models, dealing with datetime objects
        return {
            column: value if not isinstance(
                value, datetime.date) else value.strftime("%Y-%m-%d")
            for column, value in self._to_dict().items()
        }


class User(BaseModel, db.Model):
    # overwrites default table name which is CamelCase -> camel_case
    __tablename__ = "User"

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    first_name = db.Column(db.String(254), nullable=False)
    last_name = db.Column(db.String(254), nullable=False)
    email = db.Column(db.String(254), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    read_receipts_on = db.Column(db.Boolean(254), nullable=False)


class Chat(BaseModel, db.Model):
    __tablename__ = "Chat"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    is_group = db.Column(db.Boolean, nullable=False)

# class Message(BaseModel, db.Model):
#     __tablename__ = "Message"

#     id = db.Column(db.Integer, primary_key = True)
#     user_id = db.Column(db.Integer, db.ForeignKey(''))
#
