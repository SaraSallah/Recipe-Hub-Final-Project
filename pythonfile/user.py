import json

class User:
    def __init__(self, filename):
        self.filename = filename

    def add_user(self, email, password, username):
        with open(self.filename, 'r') as infile:
            data = json.load(infile)

        for user in data:
            if user['email'] == email:
                return 'Email already exists. Please use a different email address.'

        new_user = {"email": email, "pass": password, "user": username, "favorites": []}  # Add empty favorites list
        data.append(new_user)

        with open(self.filename, 'w') as outfile:
            json.dump(data, outfile, indent=4)

        return None

    def delete_user(self, email):
        with open(self.filename, 'r') as infile:
            data = json.load(infile)

        new_data = [user for user in data if user['email'] != email]

        with open(self.filename, 'w') as outfile:
            json.dump(new_data, outfile, indent=4)

        return None
