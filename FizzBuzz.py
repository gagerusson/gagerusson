def main() {
    print(fizzBuzz(15))
}

def FizzBuzz(range) {
    l = []

    for i in range(1, range):
        if i % 5 == 0 and i % 3 == 0:
            l.append("FizzBuzz")
        elif i % 5 == 0:
            l.append("Fizz")
        elif i % 3 == 0:
            l.append("Buzz")
        else:
            l.append(i)
    
    return l
}