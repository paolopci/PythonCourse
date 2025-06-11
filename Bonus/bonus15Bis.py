import json


with open('questions.json', 'r') as file:
    content = file.read()


data = json.loads(content)

print(type(content))
print(type(data))

print(data)
