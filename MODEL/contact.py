from sys import maxsize

class Contact:

    def __init__( self,
                        first_name,
                        middle_name = None,
                        last_name = None,
                        nick_name = None,
                        contact_title = None,
                        company_name = None,
                        contact_address = None,
                        home_phone = None,
                        mobile_phone = None,
                        work_phone = None,
                        fax_phone = None,
                        contact_email1 = None,
                        contact_email2 = None,
                        contact_email3 = None,
                        home_page = None,
                        birthday_day = None,
                        birthday_month = None,
                        birthday_year = None,
                        anniversary_day = None,
                        anniversary_month = None,
                        anniversary_year = None,
                        second_address = None,
                        second_home = None,
                        second_notes = None,
                        contact_id = None):

        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.contact_title = contact_title
        self.company_name = company_name
        self.contact_address = contact_address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax_phone = fax_phone
        self.contact_email1 = contact_email1
        self.contact_email2 = contact_email2
        self.contact_email3 = contact_email3
        self.home_page = home_page
        self.birthday_day = birthday_day
        self.birthday_month = birthday_month
        self.birthday_year = birthday_year
        self.anniversary_day = anniversary_day
        self.anniversary_month = anniversary_month
        self.anniversary_year = anniversary_year
        self.second_address = second_address
        self.second_home = second_home
        self.second_notes = second_notes
        self.contact_id = contact_id

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (self.first_name, self.last_name, self.middle_name, self.contact_id,self.home_phone,self.mobile_phone, self.work_phone, self.fax_phone, self.home_page, self.second_home)

    def __eq__(self, other):

        return   (self.contact_id == other.contact_id or self.contact_id == None or other.contact_id is None) # and self.first_name == other.first_name


    def id_or_max(self):
       if self.contact_id:
           return int(self.contact_id)
       else:
            return maxsize

