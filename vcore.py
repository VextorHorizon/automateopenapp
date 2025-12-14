import json
import os
import subprocess
import webbrowser

with open('profile.json', 'r') as file:
    app_data = json.load(file)

# print(app_data)

# ตอนนี้มันรู้แล้วว่ามีอะไรบ้าง(ด้วยการเข้าไปอ่านใน json) สเต็ปต่อไปคือ 1.เช็คว่าเจ้าตัวแอพใน profile มันมีอยู่ในเครื่องจริงๆหรือป่าว 2.ถ้ามี ก้บอกว่ามี 3.เปิด 4.กลับไปวนใหม่เช็คตามขั้นลำดับ 
