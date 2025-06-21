import sqlite3

def describe_table(table_name, db_path) :
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    try:
        cursor.execute("PRAGMA table_info({0})".format(table_name))
        columns = cursor.fetchall()

        print("Table Structure : ")
        for col in columns :
            print(f"  {col[1]} ({col[2]})")
    
    except sqlite3.Error as e:
        print("Error : ", e)
    
    connection.close()