import sqlite3
import json
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from db import db

# class ItemModel(Resource):
class ItemModel(db.Model):

    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)  # auto increment
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2)) ## 소숫점 2자리

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))  # Foreign Key
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {
            'id':self.id,
            'name':self.name,
            'price':self.price,
            'store_id':self.store_id
        }

    #### common sql query
    @classmethod
    def find_by_name(cls, name):
        # connection = sqlite3.connect("data.db")
        # cursor = connection.cursor()
        #
        # query ="SELECT * FROM items WHERE name =?"
        # result = cursor.execute(query, (name,))
        # row = result.fetchone()
        # connection.close()
        #
        # if row :
        #      # return {'item':{'name':row[0], 'price':row[1]}}
        #      # return cls(row[0], row[1])
        #      return cls(*row)  # each argument

        return cls.query.filter_by(name=name).first()  # select * from items where name=name limit 1


    # def insert(self):
    def save_to_db(self):
        # connection = sqlite3.connect("data.db")
        # cursor = connection.cursor()
        #
        # query = "INSERT INTO items VALUES (?,?)"
        # cursor.execute(query, ( self.name, self.price ) )
        #
        # connection.commit()
        # connection.close()

        db.session.add(self)
        db.session.commit()


    # def update(self):
    #     connection = sqlite3.connect("data.db")
    #     cursor = connection.cursor()
    #
    #     query = "UPDATE items SET price = ? WHERE name =? "
    #     cursor.execute(query, ( self.price, self.name ) )
    #
    #     connection.commit()
    #     connection.close()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()