import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request
import dbconstants
from flask import Blueprint

productAPI = Blueprint('productAPI', __name__)

@productAPI.route('/products')
def products():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute(dbconstants.SELECT_ALL_PRODUCTS_SQL)
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@productAPI.route('/createproduct', methods=['POST'])
def add_product():
	try:
		_json = request.json
		_product_name = _json['productName']
		_category_id = _json['categoryId']
		_UnitPrice = _json['unitPrice']
		# validate the received values
		if _product_name and _category_id and _UnitPrice and request.method == 'POST':
		
			# save edits
			sql = dbconstants.INSERT_PRODUCT_SQL
			data = (_product_name, _category_id,_UnitPrice)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Product added successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@productAPI.route('/product/<int:id>')
def product(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute(dbconstants.SELECT_PRODUCT_SQL, id)
		row = cursor.fetchone()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@productAPI.route('/UpdateProduct', methods=['POST'])
def update_product():
	try:
		_json = request.json
		_product_id = _json['productid']
		_product_name = _json['productName']
		_category_id = _json['categoryId']
		_UnitPrice = _json['unitPrice']
		
		# validate the received values
		if _product_id and _product_name and _category_id and _UnitPrice and request.method == 'POST':
			
			# save edits
			sql = dbconstants.UPDATE_PRODUCT_SQL
			data = (_product_name, _category_id,_UnitPrice, _product_id)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Product updated successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@productAPI.route('/DeleteCategory/<int:id>')
def delete_category(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute(dbconstants.DELETE_PRODUCT_SQL, (id,))
		conn.commit()
		resp = jsonify('Product Deleted successfully!')
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@productAPI.errorhandler(404)
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