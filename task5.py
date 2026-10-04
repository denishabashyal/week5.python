text = input("Enter a string: ")

seen = []

for char in text:
    if char in seen:
        print("First repeated character:", char)
        break
    seen.append(char)