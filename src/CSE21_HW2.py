from itertools import permutations

perms = list(permutations([1,2,3]))

def check_lightning(p, k):
    first = p[:k]
    second = p[k:]
    # Check first subsequence is decreasing
    for i in range(1, len(first)):
        if first[i-1] <= first[i]:
            return False 
    if p[k-1] >= p[k]:
        return False 
    for i in range(1, len(second)):
        if second[i-1] <= second[i]:
            return False 
    return True


def lightning_perms(n, k):
    perms = list(permutations([i for i in range(1,n+1)]))
    total = 0 
    lightning_perms = []
    for p in perms:
        if check_lightning(p, k):
            lightning_perms.append(p)
            total += 1
    return lightning_perms 

def total_lightning_perms(n):
    total = 0
    for k in range(1,n):
        total += len(lightning_perms(n,k))
    return total

# print(total_lightning_perms(5))
print(lightning_perms(4,2))

