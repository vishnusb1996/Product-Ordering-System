SELECT_ALL_CATEGORIES_SQL = 'SELECT categoryid, categoryname, description FROM categories'
GetAllCustomers_SQL = 'SELECT * FROM Customers'

SELECT_ALL_PRODUCTS_SQL = 'SELECT p.ProductID, p.ProductName, p.CategoryID,p.UnitPrice, c.CategoryName, c.Description FROM product p INNER JOIN categories c ON p.CategoryID = c.CategoryID'
SELECT_PRODUCT_SQL = 'SELECT p.ProductID, p.ProductName, p.CategoryID,p.UnitPrice, c.CategoryName, c.Description FROM product p INNER JOIN categories c ON p.CategoryID = c.CategoryID WHERE p.ProductID=%s'
DELETE_PRODUCT_SQL = "DELETE FROM product WHERE ProductID=%s"
INSERT_PRODUCT_SQL = "INSERT INTO product (ProductName,CategoryID,UnitPrice) VALUES (%s,%s,%s)"
UPDATE_PRODUCT_SQL = "UPDATE product SET ProductName = %s,CategoryID = %s,UnitPrice =%s WHERE ProductID = %s"

SELECT_ALL_ORDER_SQL = "SELECT o.OrderID,o.CustomerID,o.OrderDate,o.RequiredDate,o.ShippedDate,o.ShipName,o.ShipAddress,o.ShipCity,o.ShipRegion,o.ShipPostalCode,o.ShipCountry, c.CompanyName,c.ContactName,c.ContactTitle FROM `order` o inner join customers c on c.CustomerID = o.CustomerID"
SELECT_ORDER_SQL = "SELECT o.OrderID,o.CustomerID,o.OrderDate,o.RequiredDate,o.ShippedDate,o.ShipName,o.ShipAddress,o.ShipCity,o.ShipRegion,o.ShipPostalCode,o.ShipCountry, c.CompanyName,c.ContactName,c.ContactTitle FROM `order` o inner join customers c on c.CustomerID = o.CustomerID  WHERE o.OrderID=%s"
DELETE_ORDER_SQL = "DELETE FROM `order` WHERE OrderID = %s"
INSERT_ORDER_SQL = "INSERT INTO `order` ( CustomerID,OrderDate,RequiredDate,ShippedDate,ShipName,ShipAddress,ShipCity,ShipRegion,ShipPostalCode,ShipCountry ) VALUES (%S,%S,%S,%S,%S,%S,%S,%S,%S,%S)"
UPDATE_ORDER_SQL = "UPDATE `order` SET CustomerID = %s,OrderDate = %s,RequiredDate=%s,ShippedDate = %s,ShipName = %s,ShipAddress = %s, ShipCity =%s, ShipRegion= %s , ShipPostalCode =%s, ShipCountry = %s WHERE OrderID = %s"