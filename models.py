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


class User(BaseModel):

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    first_name = db.Column(db.String(254), nullable=False)
    last_name = db.Column(db.String(254), nullable=False)
    email = db.Column(db.String(254), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    read_receipts_on = db.Column(db.Boolean(254), nullable=False)

    message = db.relationship("Message", uselist=True, backref="user")
    file_message = db.relationship("FileMessage", uselist=True, backref="user")
    reaction_message = db.relationship("ReactionMessage", uselist=True, backref="user")
    user_in_chat = db.relationship("UserInChat", uselist=True, backref="user")

class Chat(BaseModel):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    is_group = db.Column(db.Boolean, nullable=False)

    message = db.relationship("Message", uselist=True, backref="chat")
    file_message = db.relationship("FileMessage", uselist=True, backref="user")
    reaction = db.relationship("Reaction", uselist=True, backref="chat")
    user_in_chat = db.relationship("UserInChat", uselist=True, backref="chat")


class Message(BaseModel):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    chat_id = db.Column(db.Integer, db.ForeignKey("chat.id"), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.String(5000), nullable=False)

    reaction_message = db.relationship("ReactionMessage", uselist=True, backref="message")

class Reaction(BaseModel):

    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer, db.ForeignKey("chat.id"), nullable=False)
    alias = db.Column(db.String(100), nullable=False)

    reaction_message = db.relationship("ReactionMessage", uselist=True, backref="reaction")

class ReactionMessage(BaseModel):
    
    message_id = db.Column(db.Integer, db.ForeignKey("message.id"), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    reaction_id = db.Column(db.Integer, db.ForeignKey("reaction.id"), nullable=False)

class FileMessage(BaseModel):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    chat_id = db.Column(db.Integer, db.ForeignKey("chat.id"), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    file_type = db.Column(db.String(10), nullable=False)

class UserInChat(BaseModel):

    chat_id = db.Column(db.Integer, db.ForeignKey("chat.id"), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    nickname = db.Column(db.String(200), nullable=True)
    active = db.Column(db.Boolean, nullable=False)
    last_read_message_id = db.Column(db.Integer, db.ForeignKey(chat.id), nullable=False)
    last_read_message_timestamp = db.Column(db.DateTime, nullable=False)
    read_receipts_on = db.Column(db.Boolean, nullable=False)

# class Deleted(BaseModel):

#     user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
#     message_id = db.Column(db.Integer, db.ForeignKey("message.id"), primary_key=True)


