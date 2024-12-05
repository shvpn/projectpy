import base64
from asset.crypt import Message
class decrypt(Message):
    def __init__(self):
        self.__message = ""
        self.__password = ""
        self.__length = 0
        self.__interpassword = None
    def decrypt(self, message=None, password=None):
        if message is not None:
            self.__message = message
        if password is not None:
            self.__interpassword = password
        self.__message= base64.b64decode(self.__message.encode()).decode()
        return self.uncb()
    def uncb(self):
        try:
            # Get the length of the password
            self.__length = int(self.__message[-1])
            # Split the message and password
            self.__message = self.__message[:-1]
            count=0
            msg=""
            for i in range(len(self.__message)):
                if i % 2 != 0:
                    self.__password=self.__password+self.__message[i]
                    count+=1
                if count==self.__length:
                    break
            for i in range(len(self.__message)):
                if i % 2 == 0:
                    msg=msg+self.__message[i]
            self.__message=msg
        except ValueError:
            return "Error: Could not convert the last character of the message to an integer."
        except AttributeError:
            return "Error: Missing attributes 'self.__message' or 'self.__password'."
        except IndexError:
            return "Error: Index out of range."
        except Exception as e:
            return "An error occurred: ", e
        else:
            if self.__password == self.__interpassword:
                return self.__message
            else:
                return "Error: Passwords do not match."

if __name__ == '__main__':
    message = input("Enter the message: ")
    password = input("Enter the password: ")
    msg = decrypt()
    print(msg.decrypt(message, password))
   

