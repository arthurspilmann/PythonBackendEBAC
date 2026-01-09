def number_pattern(n):
    if not isinstance(n, int):
        print("Argument must be an integer value.")
        return
    if n <= 0:
        print("Argument must be an integer greater than 0.")
        return
    
    numbers = ""
    for i in range(n):
        numbers += str(i+1) + " "
    return (numbers.strip())

print(number_pattern(4))