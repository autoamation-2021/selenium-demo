import configparser
import os

config = configparser.RawConfigParser()
# config.read(os.path.abspath(os.curdir)+'\\configurations\\config.ini')
# config.read(os.path.join(os.path.abspath(os.curdir), 'configurations', 'config.ini'))
config.read(r"D:\pytest-framework-by-sdet\pytest-by-sdet\configurations\config.ini")
print("Config Sections test:", config.sections())

class ReadConfig():

    @staticmethod
    def getApplicationURL():
        url = config.get('commonInfo','baseURL')
        return url


    @staticmethod
    def getUseremail():
        username = config.get('commonInfo','email')
        return username 

    @staticmethod
    def getPassword():
        password = config.get('commonInfo','password')
        return password