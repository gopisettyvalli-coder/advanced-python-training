# remove

fruits=["Kiwi", "Berries", "Avagadro", "Watermelon", "Banana"]
print(fruits)
result=fruits.remove("Banana")
print("After removing:", fruits)
print("=========================================================")

#pop

names=["Seetha", "Geetha", "Radha", "Anu", "Raghu"]
print(names)
names.pop()
names.pop(2)
print("Names after modifing:", names)
print("=========================================================")


# both remove and pop
numbers=[10,20,30,40,15,25,35,45,56]
print("Number list:", numbers)

numbers.remove(40)
numbers.pop()
numbers.pop(2)
print("Numbers after removing:", numbers)