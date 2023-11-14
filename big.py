# array5 = [5,5,5,5,5,5,5]
# print (len(array5 )- 1 )

arr = []
g = 0
inc = 1
n = int(input("Number of elements in array: "))
for i in range(n):
  element = int(input(f"List the array of number{g}: "))
  g+= inc
  arr.append(element)
print(arr)

