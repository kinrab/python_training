
# from FIXTURE.orm import ORMFixture
#
# db = ORMFixture(host = "127.0.0.1", name = "addressbook", user = "root", password = "")
#
# try:
#     list = db.get_contact_list()
#     for item in list:
#         print(item)
#     print("Len = "+ str(len(list)))
# finally:
#     pass # ORM автоматически удаляет все что нужно



from FIXTURE.db import DbFixture
dbFix = DbFixture(host = "127.0.0.1",
                  name = "addressbook",
                  user = "root",
                  password = "")

try:
    contacts = dbFix.get_contact_list()
    for contact in contacts:
        print(contact)
    print("Контактов: " + str(len(contacts)))
finally:
    dbFix.destroy()




# dbFix = DbFixture(host = "127.0.0.1",
#                   name = "addressbook",
#                   user = "root",
#                   password = "")
#
# try:
#     groups = dbFix.get_group_list()
#     for group in groups:
#         print(group)
#     print("Групп: " + str(len(groups)))
# finally:
#     dbFix.destroy()





#################################################################################################
# ПЕРВЫЙ ВАРИАНТ ПРОВЕРКИ ДОСТУПА К БАЗЕ:
#################################################################################################
# import mysql.connector
# from mysql.connector import Error

# print("Start...\n")
#
# try:
#     # Establish the connection MySQL version 5.6.26 mysql-connector-python==8.4.0
#     # Нужно устанавливать именно эту версию коннектора: pip install mysql-connector-python==8.4.0
#
#     connect = mysql.connector.connect( user='root', password='', host='127.0.0.1',
#                                        database = "addressbook")
#     if connect.is_connected():
#         print("Connection successful.\n")
#         print("Connect : Ok\n")
#     else:
#         print("Connection Unsuccessful!\n")
#     cursor = connect.cursor()
#     print("Cursor : Ok\n")
#     cursor.execute("select * from group_list")
#     print("Execute GROUPS: Ok\n")
#     for row in cursor.fetchall():
#         print(row)
#     print("Execute COUNT start...\n")
#     cursor.execute("select COUNT(*) from group_list")
#     print("Execute COUNT: Ok\n")
#     list_of_tuple = cursor.fetchall()
#
#     first_elements_list = [t[0] for t in list_of_tuple]
#     #print(str(list_of_tuple[0][0]))
#     print("Всего записей group в базе: " + str(first_elements_list[0]))
#     print ("End COUNT")
#
#     print("End of group list")
#
# except Error as err:
#     print(f"Error connecting to MySQL: {err}")
#
# finally:
#
#     print("Finally:\n")
#
#     if connect and connect.is_connected():
#         cursor.close()
#         connect.close()
#         print("Connection closed")
#
#     print("End of finally\n")
#
# print("Exit.\n")
