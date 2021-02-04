def num_divisible(n, nums):
    
    return 

print(num_divisible(1000000, [12,14,15]))

x = [1 if i % 12 == 0 or i % 14 == 0 or i % 15 == 0 else 0 for i in range(1,1000001) ]
print(sum(x))

y = [1 if i % 2 == 0 or i % 3 == 0 or i % 4 == 0 else 0 for i in range(1,11)]
print(sum(y))
