"""
Docstring for Data_Handling_Projects.JSON-to-Excel_Converter_tool

Created a Python Utility that reads structured data (like you would get from an API) from a `.json` file and converts it to a CSV file that can be opened in Excel.

What it does?
- Read from a file named `api_data.json` in the same folder.
- Convert the JSON content (a list of dictionaries) into `converted_data.csv`.
- Automatically extrcat field names as CSV headers. 
- Handled nested structures by flattening or skipping them.

"""
import json
import csv
import os

INPUT_FILE = "../api_data.json"
OUTPUT_FILE = "converted_data.csv"

def load_json_data(filename):
    if not os.path.exists(filename):
        print("JSON file not found")
        return []
    
    with open(filename, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            print("Invalid JSON format! ")

def convert_to_csv(data, output_file):
    if not data:
        print("No data to convert")
        return
    fieldname = list(data[0].keys())

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldname)
        writer.writeheader()
        for record in data:
            writer.writerow(record)

    print(f"Converted {len(data)} records to {output_file}")

def main():
    print("Converting JSON to CSV...")
    data = load_json_data(INPUT_FILE)
    convert_to_csv(data, OUTPUT_FILE)

if __name__ == "__main__":
    main()