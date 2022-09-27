# first method
my_list = []
for i in range(5):
  my_list.append(i+1)
# print [1, 2, 3, 4, 5]

  
# second method
for i in range(5):
  my_list.insert(0, i+1)
# print [5, 4, 3, 2, 1]


# count list
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

# print(total) # 27
