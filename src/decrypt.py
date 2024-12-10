import base64

class decrypt:
    def __init__(self):
        self.__message = ""
        self.__password = ""
        self.__lengthpw = 0
        self.__lengmsg = 0
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
            # Extract key character (first character of the combined message)
            keysplit = self.__message[0]

            # Extract password and message lengths from metadata
            self.__lengthpw = int(self.__message.split(keysplit * 2 + "-")[1])  # Password length
            self.__lenghtmsg = int(self.__message.split(keysplit * 2 + "-")[2])  # Message length

            # Extract the combined section without the metadata
            combined_section = self.__message.split(keysplit * 2 + "-")[0]

            # Reconstruct password and original message
            self.__password = ""
            extracted_message = ""
            countpw=0
            countmsg=0
            for i in range(len(combined_section)):
                if i % 2 != 0:
                    if countpw == self.__lengthpw:
                        continue
                    self.__password += combined_section[i]
                    countpw+=1
                    
                else:
                    if countmsg == self.__lenghtmsg:
                        continue
                    extracted_message += combined_section[i]
                    countmsg+=1
                    if countmsg == self.__lenghtmsg and countpw == self.__lengthpw:
                        break


            

            # Return the extracted message
            if self.__interpassword == self.__password:
                return extracted_message
            else:
                return "Error: Invalid password."

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
