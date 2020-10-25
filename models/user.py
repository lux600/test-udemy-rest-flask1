import sqlite3
from flask_restful import Resource
from db import db

# class UserModel(Resource) :
class UserModel(db.Model) :

    __tablename__ ='users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        # self.id =_id
        self.username = username
        self.password = password

    # @jwt_required()
    # def get(self):
    #     user = current_identity
         ##then implement admin auth method

    @classmethod
    def find_by_username(cls, username):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query ="SELECT * FROM users WHERE username=?"
        # result = cursor.execute(query, (username,))  # ,에 대해서 (2+3)*8
        # row = result.fetchone()
        #
        # if row :
        #     # user = cls(row[0], row[1], row[2])
        #     user = cls(*row)
        #
        # else :
        #     user = None
        #
        # connection.close()
        #
        # return user

        return cls.query.filter_by(username=username).first()  # "SELECT * FROM users WHERE username=?"


    @classmethod
    def find_by_id(cls, _id):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM users WHERE id=?"
        # result = cursor.execute(query, (_id,))  # ,에 대해서 (2+3)*8
        # row = result.fetchone()
        #
        # if row:
        #     # user = cls(row[0], row[1], row[2])
        #     user = cls(*row)
        #
        # else:
        #     user = None
        #
        # connection.close()
        #
        # return user

        return cls.query.filter_by(id=_id).first()  # "SELECT * FROM users WHERE id=?"

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
