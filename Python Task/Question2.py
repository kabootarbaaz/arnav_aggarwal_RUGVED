#Write a Python program to sort a string alphabetically and print the count of each character


a=str(input("Enter a string: "))
sort=sorted(a)
print("Sorted string: " , sort)
for ch in sort(set(a)): #set()=removes repeated words   
    print(ch, ":", a.count(ch))