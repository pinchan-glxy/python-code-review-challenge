# Saves a user's data to a JSON file named by their user ID.
import json

def save_user_info(user_id, data):
    file_name = "user_" + str(user_id) + ".json"
    with open(file_name, "w") as f:
        f.write(json.dumps(data))