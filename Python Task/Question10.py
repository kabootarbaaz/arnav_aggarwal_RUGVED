n = input("Enter CC number: ")

sum = 0
double = False

for i in range(len(n)-1, -1, -1):
    x = int(n[i])

    if double:
        x = x * 2

        if x > 9:
            x = x - 9

    sum = sum + x
    double = not double

if sum % 10 == 0:
    print("Valid CC Number")
else:
    print("Give Another Nummber (FBI)")