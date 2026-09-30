message="Python Programming"
count=0
vowels=["a", "e", "i", "o", "u"]

for char in message.lower():
    if char in vowels:
        count+=1

print("No.of vowels:", count)