import json
from tqdm import tqdm
import requests
import os

min_json = "students.min.json"

if os.path.exists(min_json):
    os.remove(min_json)
    print(f"File '{min_json}' deleted successfully.")

json_list = "student-list.json"

if os.path.exists(json_list):
    os.remove(json_list)
    print(f"File '{json_list}' deleted successfully.")

URL = "https://schaledb.com/data/en/students.min.json"

schaledb = requests.get(URL, stream=True)
#print(schaledb)

with open("students.min.json", "wb") as handle:
    for data in tqdm(schaledb.iter_content(chunk_size=1024), unit="kB"):
        handle.write(data)

json_file = "students.min.json"

with open(json_file) as json_data:
    data = json.load(json_data)

num_index = 10000

with open("student-list.json", "w") as f:
    f.write("{")

for x in enumerate(data):
    if num_index == 10112:
        num_index = 13000
    if num_index == 13013:
        num_index = 16000
    if num_index == 16016:
        num_index = 20000
    if num_index == 20042:
        num_index = 23000
    if num_index == 23008:
        num_index = 26000
    x = data[str(num_index)]
    name = x["Name"]
    school = x["School"]
    combat = x["SquadType"]
    role = x["TacticRole"]
    damage = x["BulletType"]
    armor = x["ArmorType"]
    skill = x["Skills"]["Ex"]["Cost"][0]
    imgName = name.replace(" ", "_")
    if num_index == 26014:
        with open("student-list.json", "a") as f:
            f.write('"' + name + '":')
            f.write("{\n")
            f.write('"img":')
            f.write('"https://schalidle.vercel.app/imgs/' + imgName + '.png"')
            f.write(",\n")
            f.write('"name":')
            f.write('"' + name + '"')
            f.write(",\n")
            f.write('"school":')
            f.write('"' + school + '"')
            f.write(",\n")
            f.write('"combatClass":')
            f.write('"' + combat + '"')
            f.write(",\n")
            f.write('"role":')
            f.write('"' + role + '"')
            f.write(",\n")
            f.write('"damageType":')
            f.write('"' + damage + '"')
            f.write(",\n")
            f.write('"armorType":')
            f.write('"' + armor + '"')
            f.write(",\n")
            f.write('"skill":')
            f.write('"' + str(skill) + '"')
            f.write("}\n")
    else:
        with open("student-list.json", "a") as f:
            f.write('"' + name + '":')
            f.write("{\n")
            f.write('"img":')
            f.write('"https://schalidle.vercel.app/imgs/' + imgName + '.png"')
            f.write(",\n")
            f.write('"name":')
            f.write('"' + name + '"')
            f.write(",\n")
            f.write('"school":')
            f.write('"' + school + '"')
            f.write(",\n")
            f.write('"combatClass":')
            f.write('"' + combat + '"')
            f.write(",\n")
            f.write('"role":')
            f.write('"' + role + '"')
            f.write(",\n")
            f.write('"damageType":')
            f.write('"' + damage + '"')
            f.write(",\n")
            f.write('"armorType":')
            f.write('"' + armor + '"')
            f.write(",\n")
            f.write('"skill":')
            f.write('"' + str(skill) + '"')
            f.write("},\n")
    num_index += 1
    
    if num_index == 26015:
        break

with open("student-list.json", "a") as f:
    f.write("}")
    
