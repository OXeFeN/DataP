import json

data = {
    "Name": "Adam",
    "Age": 23,
    "Kids": [],
    "Married": False
}


if __name__ == "__main__":

    f = open("Test_json", "w")


    json_data = json.dumps(data)
    json_data = json.dump(data, f)

    #print(json_data)
    with open("Test_json", "r") as f:
        data = json.load(f)

    print(data)

