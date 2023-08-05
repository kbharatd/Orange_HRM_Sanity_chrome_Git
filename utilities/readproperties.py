import configparser

configuration = configparser.RawConfigParser()

configuration.read("C:\\Users\\Kalpesh\\OneDrive\\Desktop\\Credence\\Notes\\Python selenium automation\\OrangeHrm\\Configurations\\config.ini")


class Readconfig:

    @staticmethod
    def geturl():
        url = configuration.get('common info', 'Url')
        return url

    @staticmethod
    def getusername():
        username = configuration.get('common info', 'Username')
        return username

    @staticmethod
    def getpassword():
        password = configuration.get('common info', 'Password')
        return password
