import json
from datetime import datetime

class User:
    def __init__(self, filename, email):
        self.filename = filename
        self.email = email
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def add_user(self, password, username):
        # Load existing user data from file
        with open(self.filename, 'r') as infile:
            data = json.load(infile)

        # Check if email already exists
        for user in data:
            if user['email'] == self.email:
                return 'Email already exists. Please use a different email address.'

        # Create new user 
        new_user = {"email": self.email, "pass": password, "user": username, "date": self.date, "favorites": []}
        data.append(new_user)

        #  updated data back to file
        with open(self.filename, 'w') as outfile:
            json.dump(data, outfile, indent=4)

        return None

    def delete_user(self):
        # Load existing user data from file
        with open(self.filename, 'r') as infile:
            data = json.load(infile)

        # Filter out user with matching email
        new_data = [user for user in data if user['email'] != self.email]

        #  updated data back to file
        with open(self.filename, 'w') as outfile:
            json.dump(new_data, outfile, indent=4)

        return None
