n=list(str(input("Enter the message to be encrypted(lower case only): ")))
s=int(input("Enter shift: "))
for i in range(len(n)):
    n[i] = chr((ord(n[i]) - ord('a') + s) % 26 + ord('a'))
print(''.join(n))
 