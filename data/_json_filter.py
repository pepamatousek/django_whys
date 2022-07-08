"""
Parsuje data do souborů .json dle klíče "slovníku".
"""

import json


file_name = "test_data.json"


def main():
    filter_json()


def open_json(file_name: str) -> list:
    with open("test_data.json", mode="r", encoding="utf-8") as data:
        open_data = json.load(data)
    return open_data


def give_keys():
    keys = set()
    for item in open_json(file_name):
        for key in item.keys():
            keys.add(key)
    list_with_keys = sorted([key for key in keys])
    return list_with_keys


def add_content_json(json_name, json_part):
    file_name_json = json_name + ".json"
    new_line = ",\n"
    convert_to_json = json.dumps(json_part)
    with open(file_name_json, "a", encoding="utf-8") as adding:
        adding.write(new_line)
        adding.write(convert_to_json)
        adding.close()

def close_data_to_list(json_name):

    file_name_json = json_name + ".json"
    with open(file_name_json, "r", encoding="utf-8") as to_list:
        list = to_list.readlines()
        list.pop(0)
        list.insert(0, "[\n")
        list.append ("\n]")
    
    with open(file_name_json, "w", encoding="utf-8") as doing_list:
        doing_list.writelines(list)
        doing_list.close()


def filter_json():
    for found_key_name in give_keys():
        print(found_key_name)
        for count, item in enumerate(open_json(file_name), 1):
            for key in item.keys():
                if key == found_key_name:
                    add_content_json(found_key_name, item)
                if len(open_json(file_name)) == count:
                    close_data_to_list(found_key_name)

                
if __name__ == "__main__":
    main()