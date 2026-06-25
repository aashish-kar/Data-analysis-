#set
fruits ={"apple","banana","mango","pineapple","grape"}
fruits.add("watermelon")
print(fruits)

#dictionary
student ={
    "name":"aashish",
    "age" : 21,
    "faculty" : "Data Analysis"
}

print(student["name"])

#while loop
i= 1
while i < 11:
    print(i)
    i = i + 1


#for loop
for num in range(2,20,2):
    print("even numbers = ", num)


#function
def add_numbers(a,b):
    return a + b

result = add_numbers(10,10)
print(result)

#list
list = [1,2,3,4,5]
print(list[0])
print(list[-1])
print(len(list))

#loop through list
fruits =["apple","banana","mango","pineapple","grape"]
for fruit in fruits:
    print(fruit)

#range
for i in range(10,0,-1):
    print(i)