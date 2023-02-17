import configparser

config=configparser.RawConfigParser()
config.read("./Configuration/config.ini")

class Readconfig:

    @staticmethod
    def geturl():
        url=config.get("common info", "url")
        return url

    @staticmethod
    def getusername():
        name=config.get("common info","username")
        return name

    @staticmethod
    def getpassword():
        password=config.get("common info","password")
        return password
