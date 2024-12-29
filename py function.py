def add_numbers(n1, n2, n3):
    result = n1 + n2 + n3
    return result

output = add_numbers(3.6, 5.6, 8.8)
print(output)



n1 = 3.6
n2 = 5.6
n3 = 8.8

#Another example of global variables

message = "How are you doing?"

def greet():
    message = "How are you?"
    print("message inside the function", message)

    greet()
    print("message outside the function", message)