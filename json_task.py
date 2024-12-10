import json
from Example_json import data

def save_data_to_json_file(data, filename):
    try:
        f = open(f"{filename}.json", "w")
        data = json.dump(data, f)
        return True
    except:
        print("Somethink goes wrong")
        return False
        

def load_data_from_json_file(file):
    try:
        with open(f"{file}.json", "r") as f:
            data = json.load(f)
            return data
    except:
        print("Somethink goes wrong")
        return 
    
print(save_data_to_json_file(data, "correct"))
