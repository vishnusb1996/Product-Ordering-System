import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request
import dbconstants
from flask import Blueprint

orderAPI = Blueprint('orderAPI', __name__)

@orderAPI.route('/orders')
def orders():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute(dbconstants.SELECT_ALL_ORDER_SQL)
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@orderAPI.route('/creatorder', methods=['POST'])
def add_order():
	try:
		_json = request.json
		CustomerID = _json['CustomerID']
		OrderDate = _json['OrderDate']
		# FormattedOrderDate = datetime.strptime(OrderDate, format)

		RequiredDate = _json['RequiredDate']
		ShippedDate = _json['ShippedDate']
		ShipName = _json['ShipName']
		ShipAddress = _json['ShipAddress']
		ShipCity = _json['ShipCity']
		ShipRegion = _json['ShipRegion']
		ShipPostalCode = _json['ShipPostalCode']
		ShipCountry = _json['ShipCountry']
		# validate the received values
		if CustomerID and OrderDate and RequiredDate and ShipName and ShipAddress and ShippedDate and ShipCity and ShipRegion and ShipPostalCode and ShipCountry and request.method == 'POST':
		
			# save edits
			sql = dbconstants.INSERT_ORDER_SQL
			data = (CustomerID, OrderDate,RequiredDate,ShippedDate,ShipName,ShipAddress,ShipCity,ShipRegion,ShipPostalCode,ShipCountry)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Order added successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@orderAPI.route('/order/<int:id>')
def order(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute(dbconstants.SELECT_ORDER_SQL, id)
		row = cursor.fetchone()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@orderAPI.route('/updateorder', methods=['POST'])
def update_order():
	try:
		_json = request.json
		OrderID = _json['OrderID']
		CustomerID = _json['CustomerID']
		OrderDate = _json['OrderDate']
		RequiredDate = _json['RequiredDate']
		ShippedDate = _json['ShippedDate']
		ShipName = _json['ShipName']
		ShipAddress = _json['ShipAddress']
		ShipCity = _json['ShipCity']
		ShipRegion = _json['ShipRegion']
		ShipPostalCode = _json['ShipPostalCode']
		ShipCountry = _json['ShipCountry']

		# validate the received values
		if CustomerID and OrderDate and RequiredDate and ShipName and ShipAddress and ShippedDate and ShipCity and ShipRegion and ShipPostalCode and ShipCountry and request.method == 'POST':
		
			# save edits
			sql = dbconstants.UPDATE_ORDER_SQL
			data = (CustomerID, OrderDate,RequiredDate,ShippedDate,ShipName,ShipAddress,ShipCity,ShipRegion,ShipPostalCode,ShipCountry,OrderID)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Order updated successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@orderAPI.route('/deleteorder/<int:id>')
def delete_order(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute(dbconstants.DELETE_ORDER_SQL, (id,))
		conn.commit()
		resp = jsonify('Order Deleted successfully!')
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@orderAPI.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
		
# if __name__ == "__main__":
#     productAPI.run(debug=True)