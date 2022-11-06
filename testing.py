import json

def write_json(new_data, filename='data.json'):
    with open('data.json', 'r+') as file:
        file_data = json.load(file)
        file_data.append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

if __name__ == '__main__':
    y = [{"name": "uc urvine sweatr petr",
        "image_link": "",
        "timestamp": "8/30/22",
        "location": "humanities gateway",
        "instagram": "petr_the_harbingr"}, 
        
        {"name": "ZotBites",
        "image_link": "",
        "timestamp": "11/7/22",
        "location": "Fresh Basic Needs",
        "instagram": "petr_the_harbingr"}]

    for sticker in y:
        write_json(y)