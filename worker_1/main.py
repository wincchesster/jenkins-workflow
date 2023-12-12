from db_utils import Mysql

class CustomMysql(Mysql):
    def create_shop(self):
        create_table_query = """
            CREATE TABLE shop (
                id INT AUTO_INCREMENT PRIMARY KEY,
                item VARCHAR(255) NOT NULL,
                price FLOAT NOT NULL
            )
        """
        self.execute_query(create_table_query)

    def add_item(self, item, price):
        add_item_query = "INSERT INTO shop (item, price) VALUES (%s, %s)"
        self.execute_query(add_item_query, (item, price))

    def delete_item(self, item):
        delete_item_query = "DELETE FROM shop WHERE item = %s"
        self.execute_query(delete_item_query, (item,))

    def delete_shop(self):
        delete_table_query = "DROP TABLE shop"
        self.execute_query(delete_table_query)

if __name__ == "__main__":
    mysql_instance = CustomMysql()
    mysql_instance.create_shop()
    mysql_instance.add_item("apple", 1.99)
    mysql_instance.add_item("banana", 3.99)
    print("Items in the shop:")
    items = mysql_instance.fetch_all("SELECT * FROM shop")
    for item in items:
        print(item)
    mysql_instance.delete_item("apple")
    print("Items after deletion:")
    items = mysql_instance.fetch_all("SELECT * FROM shop")
    for item in items:
        print(item)
    mysql_instance.delete_shop()
    mysql_instance.close_connection()

