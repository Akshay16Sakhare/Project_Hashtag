import configparser

config = configparser.RawConfigParser()
config.read(r"C:\Users\Admin\PycharmProjects\Project_Has#tag\Configuration\config.ini")

class Read_values():

    @staticmethod
    def getName():
        name_field = config.get('application details', 'name_field')
        return name_field

    @staticmethod
    def getEmail():
        email_field = config.get('application details', 'email_field')
        return email_field

    @staticmethod
    def getPhone():
        phone_field = config.get('application details', 'phone_field')
        return phone_field

    @staticmethod
    def getDescrp():
        description_field = config.get('application details', 'description_field')
        return description_field
