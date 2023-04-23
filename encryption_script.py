import os
import bcrypt
from tkinter import Tk
from tkinter.filedialog import askopenfile

def encryption_code(key,file_content):
    key_string = str(key)
    counter = 0

    for i,j in enumerate(file_content):
        # use key to shift binary values
        key_mod = ((key*int(key_string[counter])) + len(str(key)))%255
        shifter = j^int(key_mod)
        
        file_content[i] = int(shifter)
        counter += 1
        if counter > len(key_string)-1 : counter = 0
        if int(key_string[counter]) == 0:
            counter += 1


class open_file():
    def __init__(self):
        Tk().withdraw()
        file = askopenfile(mode='rb')
        self.file_content = bytearray(file.read())
        file.close
        self.f_name = file.name

        name_split = file.name.split('.')
        self.file_type = '.' + name_split[-1]


def close_file(file_content, file_type, string):
    file = open(string + file_type,'wb')
    file.write(file_content)
    file.close


def encrypt(password, file_content, file_type, file_name): 
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    key = int.from_bytes(password, byteorder='big')

    encryption_code(key,file_content)
    os.remove(file_name)

    file_content = file_content + hashed
    close_file(file_content, file_type, 'Encrypted_file')


def decrypt(password, file_content, file_type): 
    hashed = file_content[-60:]
    file_content = file_content[0:-60]
    
    if bcrypt.checkpw(password, hashed):
        key = int.from_bytes(password, byteorder='big')

        encryption_code(key,file_content)
        close_file(file_content, file_type, 'Decrypted_file')
        return True
    else:
        return False