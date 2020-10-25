import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.item import ItemModel

class Item(Resource):

    #### parameter
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('store_id',
        type=int,
        required=True,
        help="Every item needs a store id."
    )

    ###CRUD
    @jwt_required()
    def get(self,name):
        item = ItemModel.find_by_name(name)
        if item :
            return item.json()

        return {"message":'Item not found'}, 404

    @jwt_required()
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message' : "An item with name {} already exists.".format(name)} , 400

        data = Item.parser.parse_args()

        # item = { 'name': name, 'price':data['price']}
        # item = ItemModel(name=name, price=data['price'], store_id=data['store_id'])
        item = ItemModel(name=name, **data )

        try :
            # item.insert()
            item.save_to_db()

        except :
            return {"message" :"An error occurred inserting the item."} , 500  # 500 : Internal Server Error

        return item.json(), 201


    @jwt_required()
    def delete(self, name):
        # connection = sqlite3.connect("data.db")
        # cursor = connection.cursor()
        #
        # query = "DELETE FROM items WHERE name= ? "
        # cursor.execute(query, ( name, ) )
        #
        # connection.commit()
        # connection.close()

        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message':"Item {} deleted".format(name)}

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()

        # item = ItemModel.find_by_name(name)
        # updated_item = {'name':name, 'price': data['price'] }
        # updated_item = ItemModel(name, data['price'])
        item = ItemModel.find_by_name(name)

        if item is None:
            # try :
            #     updated_item.insert()
            # except:
            #     return {"message" :"An error occurred inserting the item."} , 500  # 500 : Internal Server Error

            # item = ItemModel(name, data['price'], data['store_id'])
            item = ItemModel(name, **data)

        else :
            # try :
            #     # Item.update(updated_item)
            #     updated_item.update()
            # except:
            #     return {"message" :"An error occurred updating the item."} , 500  # 500 : Internal Server Error
            item.price = data['price']

        item.save_to_db()

        # return updated_item.json()
        return item.json()



class ItemList(Resource):
    @jwt_required()
    def get(self):

        # connection = sqlite3.connect("data.db")
        # cursor = connection.cursor()
        #
        # query ="SELECT * FROM items "
        # result = cursor.execute(query)
        #
        # items = []
        # for row in result:
        #     items.append({'name': row[1], 'price': row[2]})
        #
        # connection.close()
        #
        # return {'items' : items }

        items = ItemModel.query.all()
        # return {'items' : [ item.json() for item in items ] }
        return {'items' : list(  map(lambda x : x.json(), items) ) }
