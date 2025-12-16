import csv
import json

def create_animals_csv(path: str) -> None:
    with open(path, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        
        writer.writerow(["Животное", "Среда обитания"])
        
        writer.writerow(["Медведь", "Лес"])
        writer.writerow(["Дельфин", "Океан"])
        writer.writerow(["Верблюд", "Пустыня"])

def convert_csv_to_json(csv_path: str, json_path: str) -> None:
    data = []

    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file) 
        
        for row in reader:
            data.append(row)

    with open(json_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def convert_json_to_csv(json_path: str, csv_path: str) -> None:
    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file) 
    if not data:
        return 
    headers = data[0].keys()

    with open(csv_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        
        writer.writeheader()
        writer.writerows(data)

create_animals_csv("animals.csv")
convert_csv_to_json("animals.csv", "animals.json")
convert_json_to_csv("animals.json", "animals_from_json.csv")