from pony.orm import *
from datetime import datetime
from MODEL.group import Group
from MODEL.contact import Contact
from pymysql.converters import decoders

# Не заработало! При прекомпиляции ошибка!
# Error:  IndexError: tuple index out of range

class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):

        _table_ = 'group_list'
        id = PrimaryKey(int, column = 'group_id')
        name = Optional(str, column = 'group_name')
        header = Optional(str, column = 'group_header')
        footer = Optional(str, column = 'group_footer')

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column = 'id')
        firstname = Optional(str,column = 'firstname')
        lastname = Optional(str, column = 'lastname')
        deprecated = Optional(datetime, column='deprecated')

    def __init__(self,host,name,user,password):
        self.db.bind(provider='mysql', host=host, db=name, user=user, passwd=password, conv=decoders)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_module(self,groups):
        def convert(group):
            return Group(group_id = group.id,
                         group_name = group.name,
                         group_header = group.header,
                         group_footer = group.footer)
        map(convert, groups)

    def convert_contacts_to_module(self,contacts):
        def convert(contact):
            return Contact(contact_id = contact.id,
                           first_name = contact.first_name,
                           last_name = contact.last_name)
        map(convert, contacts)

    @db_session
    def get_group_list(self):
        #return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))
        return self.convert_groups_to_module(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_module(select(c for c in ORMFixture.ORMContact if c.deprecated is None))