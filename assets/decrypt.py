import base64

class decrypt:
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
        
        # Decode Base64
        try:
            self.__message = base64.b64decode(self.__message.encode()).decode()
            print(self.__message)
        except Exception as e:
            return f"Error decoding message: {e}"
        
        return self.__process_message()

    def __process_message(self):
        try:
            # Extract password length
            self.__length = int(self.__message[-1])
            self.__message = self.__message[:-1]
            
            # Reset password and extract characters
            self.__password = ""
            extracted_message = ""
            
            for i, char in enumerate(self.__message):
                if i % 2 != 0 and len(self.__password) < self.__length:
                    self.__password += char
                elif i % 2 == 0:
                    extracted_message += char
            
            # Verify password
            if self.__password == self.__interpassword:
                return extracted_message
            else:
                return "Error: Passwords do not match."

        except ValueError:
            return "Error: Invalid format for the message."
        except Exception as e:
            return f"An error occurred: {e}"

if __name__ == '__main__':
    message = input("Enter the Base64-encoded message: ")
    password = input("Enter the password: ")
    msg = decrypt()

    result = msg.decrypt(message, password)
    print("Decryption result:", result)
