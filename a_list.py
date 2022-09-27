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


# sort list
my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.

while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# print(my_list) # [10, 8, 6, 4, 2]
