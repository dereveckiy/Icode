import json

app_data = {
    "method": [
        "ISO 4480-83",
        "GOST 2708-75",
        "International 1/4 Log Rule",
        "Doyle Log Rule",
        "Scribner Log Rule",
        "JAS Scale",
        "Hoppus Log Rule"
    ],
    "wood_type": ["Сосна", "Дуб", "Ясень"],
    "price": ["1000", "2000", "3000"],
    "sort": ["A", "B", "C"],
    "quantity": ["1", "2", "3"],
    "table": []
}

def save_data(data):
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_data():
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return app_data

app_data = load_data()
print(f"Loaded app_data: {app_data}")

def save_table(table_data, filename="table_data.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(table_data, f, ensure_ascii=False, indent=4)

def load_table(filename="table_data.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []