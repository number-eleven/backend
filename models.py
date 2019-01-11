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

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    first_name = db.Column(db.String(254), nullable=False)
    last_name = db.Column(db.String(254), nullable=False)
    email = db.Column(db.String(254), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    read_receipts_on = db.Column(db.Boolean(254), nullable=False)
    message = db.relationship("Message", uselist=False, backref="user")


class Chat(BaseModel, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    is_group = db.Column(db.Boolean, nullable=False)
    message = db.relationship("Message", uselist=False, backref="chat")


class Message(BaseModel, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    chat_id = db.Column(db.Integer, db.ForeignKey("chat.id"), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.String(5000), nullable=False)


# many to many relationship? I'm hecking confused, idk how to configure this
ReactionMessage = db.Table("reaction_message",
                           db.Column(message_id, db.Integer, db.ForeignKey)
                           )
