import datetime
import json
import os


# Get the current directory of the Py script
current_directory = os.path.dirname(os.path.realpath(__file__))
json_file_path = os.path.join(current_directory, 'quotes_and_tips.json')

# Get the current day
current_day = datetime.datetime.now().strftime("%A")

# Read the JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Access the quotes and tips based on the current day
quotes = data["quotes"]
tips = data["tips"]

print ("Quote for", current_day + ":", quotes[current_day])
print ("Daily Green tip:", tips[current_day])