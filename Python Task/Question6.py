a=list(str(input("Enter first word: ")))
b=list(str(input("Enter second word: ")))
a.sort()
b.sort()
if a==b:
    print("Anagram")
else:
    print("not anagram")