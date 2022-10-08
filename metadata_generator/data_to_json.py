import json


def data_to_json(user_metadata):
    user_data = {user_metadata["user_name"]: user_metadata}
    to_json = json.dumps(user_data, indent = 4)

    with open("new_user_data.json", "w") as file:
        file.write(to_json)