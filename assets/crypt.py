
class Message:
    def __init__(self, message="", password="", length=0):
        self.__message = message #message
        self.__password = password #password
        self.__length = length #length of password
    #combine function
    def cb(self, message=None, password=None): #get the message and password
        if message is not None:
            self.__message = message #set the message
        if password is not None:
            self.__password = password #set the password
        try:
            if len(self.__password) > len(self.__message): #if the password is longer than the message
                raise ValueError("Password is longer than the message.")
            elif len(self.__password) >=10:
                raise AttributeError("Password is longer than 9 characters.")
            else:
                self.__length = len(self.__password) #set the length of the password
        except ValueError :
            return ["Password Cannot be longer than the message."]
        except AttributeError:
            return ["Password Cannot be longer than 9 characters."]
        except KeyboardInterrupt:
            return ["Console Interrupted"]
        except Exception as e:
            return [e]
        else:
            self.__password = self.extentpw() #extend the password
            self.Combine() #combine the message and password
            return self.__message #return the message after combining
            
    def extentpw(self): #extend the password
        if len(self.__password) < len(self.__message): #if the password is shorter than the message
            self.__password = self.__password * (len(self.__message) // len(self.__password)) + self.__password[:len(self.__message) % len(self.__password)]
        return self.__password #return the password after extending
    def Combine(self): #combine the message and password
        try:
        # Combine the two strings character by character
            combined_msg = ''.join(
                char1 + char2
                for char1, char2 in zip(self.__message, self.__password)
            )
        # Add the remaining characters from the longer string
            combined_msg += self.__message[len(self.__password):] #add the remaining characters from the longer string
            combined_msg += self.__password[len(self.__message):] #add the remaining characters from the longer string
            combined_msg =combined_msg+str(self.__length) #add the length of the password
            self.__message = combined_msg #set the message to the combined message
        except AttributeError:
            return "Error: Missing attributes 'self.__message' or 'self.__password'."
    
if __name__ == '__main__':
    message = input("Enter the message: ")
    password = input("Enter the password: ")
    msg = Message(message, password)
    print(msg.cb())
    
