
#1 sum_to
def sum_to(n):
  print(sum(range(1, n+1)))


# sum_to(6)
# sum_to(10)


#2 largest
list1 = [1,2,3,4,0]
list2 = [10,4,2,231,91,54]

def largest1(list):
  list.sort()
  return print(list[-1])

def largest2(list):
  return print(max(list))

# largest1(list1)
# largest1(list2)

# largest2(list1)
# largest2(list2)




#3 occurences
def occurrences(str1, str2):
  return print(str1.count(str2))

# occurrences('fleep floop', 'e')   
# occurrences('fleep floop', 'p')   
# occurrences('fleep floop', 'ee')  
# occurrences('fleep floop', 'fe')  

#4 product
def product(*nums):
  product = 1
  for num in nums:
    product *= num
  return print(product)

# product(-1, 4) 
# product(2, 5, 5)
# product(4, 0.5, 5)