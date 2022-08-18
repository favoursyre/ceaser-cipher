import os

#Ceaser Cipher Substitution Encrypting technique



print("CEASER CIPHER \n")
directory = os.getcwd() #Getting the current directory that we are in 
print(f"Current Directory: {directory}")


print("This function allows you to Encrypt/Decrypt Alpha-Numeric message using Ceaser Cipher \n")
class ceaserCipher():
    def __init__(self, plainText, key):
        self.plainText = plainText
        self.key = key 
        self.alphabets = "0123456789abcdefghijklmnopqrstuvwxyz"
        #print(f"Alpha length: {len(alphabets)}")

    #This function allows us to encrypt the message
    def encrypt(self):
        #global cipherText
        cipherText = ""
        textLength = len(self.plainText)
        for i in range(textLength):
            character = self.plainText[i] #This gets each characters 
            if character == " ": #This checks if there is space in the text
                cipherText += " "
            else:
                characterLocation = self.alphabets.find(character) #This finds the selected character in the alphabets
                newLocation = (characterLocation + self.key) % len(self.alphabets) #This finds the modulos and adding the key
                cipherText += self.alphabets[newLocation] #This finds the index on the alphabets with respect to the alphabets and appends the cipherText

        #print(f"Encrypted Text: {cipherText}")
        return cipherText

    #This function allows us to decrypt a text encrypted by a ceaser cipher algorithm
    def decrypt(self, cipherText):
        #pass
        decodedText = ""
        for i in range(len(cipherText)):
            character = cipherText[i] #This gets each characters 
            if character == " ": #This checks if there is space in the text
                decodedText += " "
            else:
                characterLocation = self.alphabets.find(character) #This finds the selected character in the alphabets
                newLocation = (characterLocation - self.key) % len(self.alphabets) #This finds the modulos and adding the key
                decodedText += self.alphabets[newLocation] #This finds the index on the alphabets with respect to the alphabets and appends the cipherText

        #print(f"Decrypted Text: {decodedText}")
        return decodedText


def main():
    key = int(input("Input the key: ")) #Asking for the key of choice    
    choice = input("Do you want to encrypt/decrypt the message?__[Press 1/2 respectively]__: ")
    if choice == "1":
        plainText = input("Write your message: ")
        cipherText = ceaserCipher(plainText, key).encrypt()
        print(f"Cipher Text: {cipherText}")
        newChoice = input("Do you want to decrypt the message?__[Press y/n respectively]__: ")
        if newChoice == "y":
            decodedText = ceaserCipher(plainText, key).decrypt(cipherText)
            print(f"Decoded Text: {decodedText}")
        elif newChoice == "n":
            pass
        else:
            raise ValueError("Input the correct answer__[y or n]__")
    elif choice == "2":
        cipherText = input("Enter encrypted message: ")
        decodedText = ceaserCipher(None, key).decrypt(cipherText)
        print(f"Decoded Text: {decodedText}")
    else:
        raise ValueError("Input the correct answer__[1 or 2]__")


if __name__ == "__main__":
    main()
