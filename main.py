import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request
import dbconstants
from CustomersController import customersAPI
from CategoryController import categoryAPI
from ProductsController import productAPI
from OrderController import orderAPI
from OrderDetailsController import orderDetailsAPI

# Register controllers
app.register_blueprint(customersAPI, url_prefix='/api/Customers')
app.register_blueprint(categoryAPI, url_prefix='/api/Category')
app.register_blueprint(productAPI, url_prefix='/api/Products')
app.register_blueprint(orderAPI, url_prefix='/api/Order')
app.register_blueprint(orderDetailsAPI, url_prefix='/api/OrderDetails')

# @app.route('/createcategory', methods=['POST'])
# def add_category():
# 	try:
# 		_json = request.json
# 		_category_name = _json['categoryname']
# 		_cat_description = _json['description']
# 		# validate the received values
# 		if _category_name and _cat_description and request.method == 'POST':
		
# 			# save edits
# 			sql = "INSERT INTO categories(categoryname, description) VALUES(%s, %s)"
# 			data = (_category_name, _cat_description)
# 			conn = mysql.connect()
# 			cursor = conn.cursor()
# 			cursor.execute(sql, data)
# 			conn.commit()
# 			resp = jsonify('category added successfully!')
# 			resp.status_code = 200
# 			return resp
# 		else:
# 			return not_found()
# 	except Exception as e:
# 		print(e)
# 	finally:
# 		cursor.close() 
# 		conn.close()

# @app.route('/products')
# def products():
# 	try:
# 		conn = mysql.connect()
# 		cursor = conn.cursor(pymysql.cursors.DictCursor)
# 		cursor.execute(dbconstants.SELECT_ALL_CATEGORIES_SQL)
# 		rows = cursor.fetchall()
# 		resp = jsonify(rows)
# 		resp.status_code = 200
# 		return resp
# 	except Exception as e:
# 		print(e)
# 	finally:
# 		cursor.close() 
# 		conn.close()

# @app.route('/categories')
# def categories():
# 	try:
# 		conn = mysql.connect()
# 		cursor = conn.cursor(pymysql.cursors.DictCursor)
# 		cursor.execute(dbconstants.SELECT_ALL_CATEGORIES_SQL)
# 		rows = cursor.fetchall()
# 		resp = jsonify(rows)
# 		resp.status_code = 200
# 		return resp
# 	except Exception as e:
# 		print(e)
# 	finally:
# 		cursor.close() 
# 		conn.close()

# @app.route('/category/<int:id>')
# def category(id):
# 	try:
# 		conn = mysql.connect()
# 		cursor = conn.cursor(pymysql.cursors.DictCursor)
# 		cursor.execute("SELECT categoryid, categoryname, description FROM categories WHERE categoryid=%s", id)
# 		row = cursor.fetchone()
# 		resp = jsonify(row)
# 		resp.status_code = 200
# 		return resp
# 	except Exception as e:
# 		print(e)
# 	finally:
# 		cursor.close() 
# 		conn.close()

# @app.route('/UpdateCategory', methods=['POST'])
# def update_category():
# 	try:
# 		_json = request.json
# 		_category_id = _json['categoryid']
# 		_category_name = _json['categoryname']
# 		_category_description = _json['description']
		
# 		# validate the received values
# 		if _category_id and _category_name and _category_description and request.method == 'POST':
			
# 			# save edits
# 			sql = "UPDATE categories SET categoryname=%s, description=%s WHERE categoryid=%s"
# 			data = (_category_name, _category_description, _category_id)
# 			conn = mysql.connect()
# 			cursor = conn.cursor()
# 			cursor.execute(sql, data)
# 			conn.commit()
# 			resp = jsonify('Category updated successfully!')
# 			resp.status_code = 200
# 			return resp
# 		else:
# 			return not_found()
# 	except Exception as e:
# 		print(e)
# 	finally:
# 		cursor.close() 
# 		conn.close()

# @app.route('/DeleteCategory/<int:id>')
# def delete_category(id):
# 	try:
# 		conn = mysql.connect()
# 		cursor = conn.cursor()
# 		cursor.execute("DELETE FROM categories WHERE categoryid=%s", (id,))
# 		conn.commit()
# 		resp = jsonify('CategoryDeleted deleted successfully!')
# 		resp.status_code = 200
# 		return resp
# 	except Exception as e:
# 		print(e)
# 	finally:
# 		cursor.close() 
# 		conn.close()

# @app.route('/GetAllCategories')
# def GetAllCategories():
# 	try:
# 		conn = mysql.connect()
# 		cursor = conn.cursor(pymysql.cursors.DictCursor)
# 		cursor.callproc("GetAllCategories")
# 		rows = cursor.fetchall()
# 		resp = jsonify(rows)
# 		resp.status_code = 200
# 		return resp
# 	except Exception as e:
# 		print(e)
# 	finally:
# 		cursor.close() 
# 		conn.close()

# @app.route('/GetCategoryById/<int:id>')
# def GetCategoryById(id):
# 	try:
# 		conn = mysql.connect()
# 		cursor = conn.cursor(pymysql.cursors.DictCursor)
# 		args = (id,)
# 		cursor.callproc("GetCategoryById", args)
# 		rows = cursor.fetchall()
# 		resp = jsonify(rows)
# 		resp.status_code = 200
# 		return resp
# 	except Exception as e:
# 		print(e)
# 	finally:
# 		cursor.close() 
# 		conn.close()

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
		
if __name__ == "__main__":
    app.run(debug=True)