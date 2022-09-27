blocks = int(input("Enter the number of blocks: "))

# Write your code here.
height = 0
count = 1
while(blocks >= 1):
    count += 1
    height += 1
    for i in range(0, count):
        blocks -= 1

print("The height of the pyramid:", height)
