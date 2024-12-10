class Message:
    def __init__(self, message="", password="", lengthpw=0,lenghtmsg=0): #initialize the message, password, and length of the password
        self.__message = message #message
        self.__password = password #password
        self.__lengthpw = lengthpw #length of the password
        self.__lenghtmsg = lenghtmsg #length of the message
    #combine function
    def cb(self, message=None, password=None): #get the message and password
        if message is not None:
            self.__message = message #set the message
        if password is not None:
            self.__password = password #set the password
        self.__lengthpw = len(self.__password) #get the length of the password
        self.__lenghtmsg = len(self.__message) #get the length of the message
        try:
            if len(self.__message) > len(self.__password):
                self.__password= self.extentpw()    
            elif len(self.__message) < len(self.__password):
                self.__message = self.extentmsg()             
        except KeyboardInterrupt:
            return ["Console Interrupted"]
        except Exception as e:
            return [e]
        else:
            self.Combine() #combine the message and password
            return self.__message #return the message after combining
            
    def extentpw(self): #extend the password
        if len(self.__password) < len(self.__message): #if the password is shorter than the message
            self.__password = self.__password * (len(self.__message) // len(self.__password)) + self.__password[:len(self.__message) % len(self.__password)]
        return self.__password #return the password after extending
    #if the msg is shorter than the password
    def extentmsg(self):
        if len(self.__message) < len(self.__password):
            self.__message = self.__message * (len(self.__password) // len(self.__message)) + self.__message[:len(self.__password) % len(self.__message)]
        return self.__message
        

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
            keysplit=combined_msg[0]
            #hide the length of the password and message for easy decryption
            combined_msg = combined_msg+keysplit*2+"-"+str(self.__lengthpw)+keysplit*2+"-"+str(self.__lenghtmsg)
            self.__message = combined_msg #set the message to the combined message
        except AttributeError:
            return "Error: Missing attributes 'self.__message' or 'self.__password'."
    
if __name__ == '__main__':
    message = input("Enter the message: ")
    password = input("Enter the password: ")
    msg = Message(message, password)
    print(msg.cb())
    
