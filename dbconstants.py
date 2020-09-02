SELECT_ALL_CATEGORIES_SQL = 'SELECT categoryid, categoryname, description FROM categories'
GetAllCustomers_SQL = 'SELECT * FROM Customers'
SELECT_ALL_PRODUCTS_SQL = 'SELECT p.ProductID, p.ProductName, p.CategoryID,p.UnitPrice, c.CategoryName, c.Description FROM product p INNER JOIN categories c ON p.CategoryID = c.CategoryID'
SELECT_PRODUCT_SQL = 'SELECT p.ProductID, p.ProductName, p.CategoryID,p.UnitPrice, c.CategoryName, c.Description FROM product p INNER JOIN categories c ON p.CategoryID = c.CategoryID WHERE p.ProductID=%s'
DELETE_PRODUCT_SQL = "DELETE FROM product WHERE ProductID=%s"
INSERT_PRODUCT_SQL = "INSERT INTO product (ProductName,CategoryID,UnitPrice) VALUES (%s,%s,%s)"
UPDATE_PRODUCT_SQL = "UPDATE product SET ProductName = %s,CategoryID = %s,UnitPrice =%s WHERE ProductID = %s"