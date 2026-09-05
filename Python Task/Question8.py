a = input("Enter a string: ")
n = int(input("Enter n: "))

if len(a) % n != 0:
    print("Division is not possible")

else:
    first = a[0:n]
    same = True

    for i in range(0, len(a), n):
        part = a[i:i+n]

        if part != first:
            same = False
            break

    if same:
        for i in range(0, len(a), n):
            print(a[i:i+n])
    else:
        print("The sequence is not the same")