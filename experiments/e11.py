def greet():
    message = "Hello, World!"
    new_message = message.replace("World", "Python").capitalize()
    return new_message


result = greet()

print(result)
