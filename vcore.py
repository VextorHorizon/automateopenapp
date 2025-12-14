import json
import os
import subprocess
import webbrowser

try:
    with open('profile.json', 'r') as file:
        app_data = json.load(file)
except FileNotFoundError:
    print("profile.json not found")
    exit()
except json.JSONDecodeError:
    print("profile.json broken!")
    exit()
# print(app_data)

# ตอนนี้มันรู้แล้วว่ามีอะไรบ้าง(ด้วยการเข้าไปอ่านใน json) สเต็ปต่อไปคือ 1.เช็คว่าเจ้าตัวแอพใน profile มันมีอยู่ในเครื่องจริงๆหรือป่าว 2.ถ้ามี ก้บอกว่ามี 3.เปิด 4.กลับไปวนใหม่เช็คตามขั้นลำดับ 

for data in app_data:
    app_name = data["name"]
    app_type = data["type"]
    app_path = data["path"]

    print(f"Checking.. {app_name}")

    if app_type == "url":
        webbrowser.open(app_path)

    elif app_type == "app":
        if os.path.exists(app_path): 
            print(f"Opening a {app_name}")
            subprocess.Popen(app_path)
        else:
            print(f"{app_name} not found at path")
    else:
        print(f"Unknown type for {app_type}!")

