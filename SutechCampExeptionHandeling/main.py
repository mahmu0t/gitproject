def is_digit(str):
    try:
        for char in str:
            int(char)

        return True

    except:
        return False

print(is_digit("125"))

print("mahmood")