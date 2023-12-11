# In this exercise we can find the even number sum from 1 to 100 using for loo:

sum = 0
for even in range(2, 101, 2):
    sum += even 
print(f"The even number of sum from 1 to hundred is: {sum}")

# Another way:

sum1 = 0
for even1 in range(1, 101):
    if even1 % 2 == 0:
        sum1 +=even1
print(sum1)

