import basic

while True:
    text = input('Basic > ')
    result, error = basic.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)
