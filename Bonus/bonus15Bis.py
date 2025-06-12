import json


with open('questions.json', 'r') as file:
    content = file.read()


data = json.loads(content)

for item in data:
    print(item["question"])
    for index, option in enumerate(item["alternatives"]):
        print(f"{index+1} - {option}")
    answer = int(input("Your answer: "))
    if answer == int(item["correct_answer"]):
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is: {item['correct_answer']}")
