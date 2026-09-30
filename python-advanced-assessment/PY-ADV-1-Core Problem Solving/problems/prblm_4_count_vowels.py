text= "Hello World"
vowels="aeiou"
count=0

for i in text.lower():
    if i in vowels:
        count+=1

print("Vowels:", count)