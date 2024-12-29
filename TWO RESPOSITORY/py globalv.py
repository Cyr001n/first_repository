message = "how are you doing?"

def greet():
    message = "how are you?"
    print("message inside the function", message)

    greet()
    print("message outside the function", message)