import pymysql
from db_config import mysql
from flask import jsonify
from flask import flash, request
import dbconstants
from flask import Blueprint

customersAPI = Blueprint('customersAPI', __name__)
generalExceptionMessage = 'Oops..Something went wrong..Please try again later'

# Used to get all customers details


@customersAPI.route("/GetAllCustomers")
def getAllCustomers():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(dbconstants.GetAllCustomers_SQL)
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    # except Exception as e:
    except Exception:
        resp = jsonify(generalExceptionMessage)
        resp.status_code = 500
        return resp
    finally:
        cursor.close()
        conn.close()

# Used to get a customer details by customer id


@customersAPI.route('/GetCustomerDataById/<int:id>')
def getCustomerDataById(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(dbconstants.GetCustomerDataById_SQL, id)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    # except Exception as e:
    except Exception:
        resp = jsonify(generalExceptionMessage)
        resp.status_code = 500
        return resp
    finally:
        cursor.close()
        conn.close()

# Used to save new customer


@customersAPI.route('/InsertNewCustomer', methods=['POST'])
def insertNewCustomer():
    try:
        _json = request.json
        _company_name = _json['companyName']
        _contact_name = _json['contactName']
        _contact_title = _json['contactTitle']
        _address = _json['address']
        _city = _json['city']
        _region = _json['region']
        _postal_code = _json['postalCode']
        _country = _json['country']
        _phone = _json['phone']

        if _company_name and _contact_name and _contact_title and _address and _city and _region and _postal_code and _country and _phone and request.method == 'POST':

            sql = dbconstants.InsertNewCustomer_SQL
            data = (_company_name, _contact_name, _contact_title,
                    _address, _city, _region, _postal_code, _country, _phone)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Customer saved successfully')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    # except Exception as e:
    except Exception:
        resp = jsonify(generalExceptionMessage)
        resp.status_code = 500
        return resp
    finally:
        cursor.close()
        conn.close()

# Used to edit existing customer


@customersAPI.route('/UpdateCustomer', methods=['POST'])
def updateCustomer():
    try:
        _json = request.json
        _customer_id = _json['customerId']
        _company_name = _json['companyName']
        _contact_name = _json['contactName']
        _contact_title = _json['contactTitle']
        _address = _json['address']
        _city = _json['city']
        _region = _json['region']
        _postal_code = _json['postalCode']
        _country = _json['country']
        _phone = _json['phone']

        if _customer_id and _company_name and _contact_name and _contact_title and _address and _city and _region and _postal_code and _country and _phone and request.method == 'POST':

            sql = dbconstants.UpdateCustomer_SQL
            data = (_company_name, _contact_name, _contact_title, _address,
                    _city, _region, _postal_code, _country, _phone, _customer_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Customer updated successfully')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    # except Exception as e:
    except Exception:
        resp = jsonify(generalExceptionMessage)
        resp.status_code = 500
        return resp
    finally:
        cursor.close()
        conn.close()

# Used to delete existing customer


@customersAPI.route('/DeleteCustomer/<int:id>')
def deleteCustomer(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(dbconstants.DeleteCustomer_SQL, id)
        conn.commit()
        resp = jsonify('Customer deleted successfully')
        resp.status_code = 200
        return resp
    except Exception as e:
        if 'a foreign key constraint fails' in str(e):
            resp = jsonify('Cannot delete..This customer is mapped somewhere')
            resp.status_code = 500
            return resp
        else:
            resp = jsonify(generalExceptionMessage)
            resp.status_code = 500
            return resp
    finally:
        cursor.close()
        conn.close()


@customersAPI.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
