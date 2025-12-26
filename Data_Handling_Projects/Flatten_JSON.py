"""
Docstring for Data_Handling_Projects.Flatten_JSON

ASKED IN INTERVIEWS!!

{
    "user":{
        "id": 1,
        "name": "Aman",
        "address":{
            "city":"Delhi",
            "pincode": 110011
        }
    
    },
    "roles": ["admin", "editor"],
    "is_active": true
}

Flatten this JSON to :

{
    "user.id":1,
    "user.name": "Aman",
    "user.address.city":"Delhi",
    "user.address.pincode":110011,
    "roles.0": "admin",
    "roles.1": "editor",
    "is_active": True
}
"""
import json
import os

INPUT_FILE = "nested_data.json"
OUTPUT_FILE = "flatten_data.json"

def flatten_json(data, parent_key='', sep='.'):
    items = {}

    if isinstance(data, dict):
        for k, v in data.items():
            full_key = f"{parent_key}{sep}{k}" if parent_key else k
            print(full_key)
            items.update(flatten_json(v, full_key, sep=sep))

    elif isinstance(data, list):
        for idx, item in enumerate(data):
            full_key = f"{parent_key}{sep}{idx}" if parent_key else str(idx)
            items.update(flatten_json(item, full_key, sep=sep))
    else:
        items[parent_key] = data

    return items

def main():
    if not os.path.exists(INPUT_FILE):
        print("No Input file found!")
        return
    
    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)

        sep =  input("ENter your separator like . or - : ").strip() or '.'

        flattened=flatten_json(data, sep=sep)
        with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
            json.dump()

        print(f"Flattened JSON saved to {OUTPUT_FILE}")

    except Exception as e:
        print("Failed to flatten the data", e)

if __name__ == "__main__":
    main()