import random

queries = """
SELECT * FROM Products WHERE Price > 500;
SELECT * FROM Customers WHERE LastName LIKE 'S%';
SELECT OrderID, CustomerID FROM Orders WHERE OrderDate BETWEEN '2024-07-01' AND '2024-07-05';
SELECT ProductName, Stock FROM Products WHERE Stock < 100;
SELECT COUNT(*) FROM Orders WHERE TotalAmount > 100;
INSERT INTO Products (ProductID, ProductName, Price, Stock) VALUES (6, 'Mouse', 29.99, 150);
UPDATE Products SET Stock = Stock + 10 WHERE ProductID = 1;
DELETE FROM Customers WHERE CustomerID = 5;
SELECT o.OrderID, c.FirstName, c.LastName FROM Orders o JOIN Customers c ON o.CustomerID = c.CustomerID;
SELECT p.ProductName, od.Quantity FROM OrderDetails od JOIN Products p ON od.ProductID = p.ProductID WHERE od.OrderID = 1;
"""

operations = [
    "SELECT * FROM Products WHERE ProductID = {id};",
    "SELECT * FROM Customers WHERE CustomerID = {id};",
    "UPDATE Products SET Price = Price * 1.05 WHERE ProductID = {id};",
    "UPDATE Customers SET LastName = 'Updated' WHERE CustomerID = {id};",
    "DELETE FROM Orders WHERE OrderID = {id};",
    "INSERT INTO Products (ProductID, ProductName, Price, Stock) VALUES ({id}, 'Product{id}', {price}, {stock});",
    "INSERT INTO Customers (CustomerID, FirstName, LastName) VALUES ({id}, 'First{id}', 'Last{id}');",
    "SELECT o.OrderID, c.FirstName, c.LastName FROM Orders o JOIN Customers c ON o.CustomerID = c.CustomerID WHERE o.OrderID = {id};",
    "SELECT p.ProductName, od.Quantity FROM OrderDetails od JOIN Products p ON od.ProductID = p.ProductID WHERE od.OrderID = {id};",
    "SELECT COUNT(*) FROM Orders WHERE OrderID = {id};",
]

additional_queries = "\n".join(
    [
        random.choice(operations).format(
            id=random.randint(1, 100),
            price=random.uniform(10.0, 1000.0),
            stock=random.randint(1, 200),
        )
        for _ in range(990)
    ]
)

all_queries = queries + additional_queries

file_path = "sql_queries.txt"
with open(file_path, "w") as file:
    file.write(all_queries)
