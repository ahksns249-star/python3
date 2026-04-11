from flet import *
import os

def main(page: Page):

    # إنشاء الفولدر
    folder_name = "test_apk"
    os.makedirs(folder_name, exist_ok=True)

    # إنشاء ملف داخل الفولدر
    file_path = os.path.join(folder_name, "done.txt")

    with open(file_path, "w") as f:
        f.write("Done successfully!")

    # نص يظهر في التطبيق
    T = Text("Folder and file created ✔️")

    page.add(T)
    page.update()

app(target=main)
