a = list(input("Enter a string: "))

for i in range(len(a)-1):
    min = i

    for j in range(i+1, len(a)):
        if a[j] < a[min]:
            min = j

    a[i], a[min] = a[min], a[i]

print("Sorted string is: " ''.join(a))