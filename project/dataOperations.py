import psycopg2
from datetime import date


class DataOperations():

    def insert(Book1, Book2, support, confidence, lift):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="abcdef!",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="LibraryOnlineSystem")
            cursor = connection.cursor()

            postgres_insert_query = """ INSERT INTO recommendations ("creation_date", "bookBase",  "bookRecommended", "support", "confidence", "lift") VALUES (%s,%s,%s,%s,%s,%s)"""
            #print(bookBase, bookRecommend, support, confidence, lift)
            record_to_insert = (date.today(), Book1, Book2, support, confidence, lift)
            #record_to_insert =(1,"01/01/2020",15,54,0.5,0.3,6)
            cursor.execute(postgres_insert_query, record_to_insert)

            connection.commit()
            count = cursor.rowcount
            print(count, "Record inserted successfully into mobile table")

        except (Exception, psycopg2.Error) as error:
            if (connection):
                print("Failed to insert record into mobile table", error)

        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    def updateTable(id,Book1, Book2, support, confidence, lift):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="abcdef!",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="LibraryOnlineSystem")

            cursor = connection.cursor()

            print("Table Before updating record ")
            sql_select_query = """select * from mobile where id = %s"""
            cursor.execute(sql_select_query, (id,))
            record = cursor.fetchone()
            print(record)

            # Update single record now
            sql_update_query = """Update mobile set price = %s where id = %s"""
            cursor.execute(sql_update_query, (Book1, Book2, support, confidence, lift, id))
            connection.commit()
            count = cursor.rowcount
            print(count, "Record Updated successfully ")

            print("Table After updating record ")
            sql_select_query = """select * from mobile where id = %s"""
            cursor.execute(sql_select_query, (id,))
            record = cursor.fetchone()
            print(record)

        except (Exception, psycopg2.Error) as error:
            print("Error in update operation", error)

        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    def deleteData(mobileId):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="abcdef!",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="LibraryOnlineSystem")

            cursor = connection.cursor()

            # Update single record now
            sql_delete_query = """Delete from mobile where id = %s"""
            cursor.execute(sql_delete_query, (mobileId,))
            connection.commit()
            count = cursor.rowcount
            print(count, "Record deleted successfully ")

        except (Exception, psycopg2.Error) as error:
            print("Error in Delete operation", error)

        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")