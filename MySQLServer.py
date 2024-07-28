import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL server
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",    # replace with your MySQL username
            password="Miki@6454" # replace with your MySQL password
        )
        cursor = cnx.cursor()

        # Create the database
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied, please check your username and password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(err)
    else:
        cursor.close()
        cnx.close()

if __name__ == "__main__":
    create_database()
