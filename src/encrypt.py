from asset.crypt import Message
import base64
class encrypt(Message):
    def __init__(self):
        self.__message = ""
        self.__password = ""
    def encrypt(self, message=None, password=None):
        if message is not None:
            self.__message = message
        if password is not None:
            self.__password = password
        self.__message=self.cb(self.__message, self.__password)
        print(self.__message)
        if isinstance(self.__message, list):
            return self.__message[0]
        else:
            return base64.b64encode(self.__message.encode()).decode()


if __name__ == '__main__':
    message = input("Enter the message: ")
    password = input("Enter the password: ")
    msg = encrypt()
    print(msg.encrypt(message, password))    

