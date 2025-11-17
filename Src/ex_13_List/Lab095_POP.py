squares=[1,2,3,4]
print(squares.pop())
print(squares)

print(squares.pop(1))
print(squares)


squares.clear()
print(squares)

numbers=[1,2,3,4]
print(numbers.index(3))

print(numbers.count(3))

numbers.sort()
print(numbers)

#reverse-reverse the list
numbers.reverse()
print(numbers)

print(max(numbers))
print(min(numbers))
print(sum(numbers))

#Slicing

print(numbers)
print(numbers[1:4])
print(numbers[-1])

print("apple" in numbers)
print(2 in numbers)



#list creation and comprehension

l=list(range(1,5))
print(l)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1])


del numbers[1]
print(numbers)


