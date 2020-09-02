import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request
import dbconstants
from flask import Blueprint

orderDetailsAPI = Blueprint('orderDetailsAPI', __name__)

@orderDetailsAPI.route('/orderDetails')
def orders():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute(dbconstants.SELECT_ALL_CATEGORIES_SQL)
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@orderDetailsAPI.errorhandler(404)
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