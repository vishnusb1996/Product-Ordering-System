SELECT_ALL_CATEGORIES_SQL = 'SELECT categoryid, categoryname, description FROM categories'

SELECT_ALL_PRODUCTS_SQL = 'SELECT p.ProductID, p.ProductName, p.CategoryID,p.UnitPrice, c.CategoryName, c.Description FROM product p INNER JOIN categories c ON p.CategoryID = c.CategoryID'
SELECT_PRODUCT_SQL = 'SELECT p.ProductID, p.ProductName, p.CategoryID,p.UnitPrice, c.CategoryName, c.Description FROM product p INNER JOIN categories c ON p.CategoryID = c.CategoryID WHERE p.ProductID=%s'
DELETE_PRODUCT_SQL = "DELETE FROM product WHERE ProductID=%s"
INSERT_PRODUCT_SQL = "INSERT INTO product (ProductName,CategoryID,UnitPrice) VALUES (%s,%s,%s)"
UPDATE_PRODUCT_SQL = "UPDATE product SET ProductName = %s,CategoryID = %s,UnitPrice =%s WHERE ProductID = %s"

SELECT_ALL_ORDER_SQL = "SELECT o.OrderID,o.CustomerID,o.OrderDate,o.RequiredDate,o.ShippedDate,o.ShipName,o.ShipAddress,o.ShipCity,o.ShipRegion,o.ShipPostalCode,o.ShipCountry, c.CompanyName,c.ContactName,c.ContactTitle FROM `order` o inner join customers c on c.CustomerID = o.CustomerID"
SELECT_ORDER_SQL = "SELECT o.OrderID,o.CustomerID,o.OrderDate,o.RequiredDate,o.ShippedDate,o.ShipName,o.ShipAddress,o.ShipCity,o.ShipRegion,o.ShipPostalCode,o.ShipCountry, c.CompanyName,c.ContactName,c.ContactTitle FROM `order` o inner join customers c on c.CustomerID = o.CustomerID  WHERE o.OrderID=%s"
DELETE_ORDER_SQL = "DELETE FROM `order` WHERE OrderID = %s"
INSERT_ORDER_SQL = "INSERT INTO `order` ( CustomerID,OrderDate,RequiredDate,ShippedDate,ShipName,ShipAddress,ShipCity,ShipRegion,ShipPostalCode,ShipCountry ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
UPDATE_ORDER_SQL = "UPDATE `order` SET CustomerID = %s,OrderDate = %s,RequiredDate=%s,ShippedDate = %s,ShipName = %s,ShipAddress = %s, ShipCity =%s, ShipRegion= %s , ShipPostalCode =%s, ShipCountry = %s WHERE OrderID = %s"

# Customers SQL Queries
GetAllCustomers_SQL = 'SELECT CustomerID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone, CustomerType, Password FROM Customers'
GetCustomerDataById_SQL = 'SELECT CustomerID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone, CustomerType, Password FROM Customers WHERE CustomerID = %s'
InsertNewCustomer_SQL = 'INSERT INTO customers (CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone, CustomerType, Password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
UpdateCustomer_SQL = 'UPDATE customers SET CompanyName = %s, ContactName = %s, ContactTitle = %s, Address = %s, City = %s, Region = %s, PostalCode = %s, Country = %s, Phone = %s, CustomerType = %s, Password = %s WHERE CustomerID = %s'
DeleteCustomer_SQL = 'DELETE FROM customers WHERE CustomerID = %s'