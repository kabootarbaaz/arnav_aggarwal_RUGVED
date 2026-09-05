text = input("Enter the text: ")

let = 0
word= 0
sent = 0

for i in range(len(text)):

    if ('a' <= text[i] <= 'z') or ('A' <= text[i] <= 'Z'):
        let = let + 1
    if text[i] == ' ':
        word = word + 1
    if text[i] == '.' or text[i] == '!' or text[i] == '?':
        sent = sent + 1

word = word + 1

L = (let / word) * 100
S = (sent / word) * 100

grade = 0.0588 * L - 0.296 * S - 15.8

print("Grade:", grade)