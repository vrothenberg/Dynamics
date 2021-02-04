from itertools import permutations 

def num_DNA_strings(n):
    '''
    Returns the number of DNA strings of length n that do not contain "AA"
    '''
    letters = ['A', 'C', 'G', 'T']
    res = []
    num_DNA_strings_rec(letters, "", n, res)

    return res

def num_DNA_strings_rec(letters, prefix, n, res):
    if n == 0:
        res.append(prefix)
        return

    for i in range(len(letters)):
        newPrefix = prefix + letters[i]
        num_DNA_strings_rec(letters, newPrefix, n-1, res)

# for i in range(1,7):
      
#     permutations = num_DNA_strings(i)

#     final = []

#     for p in permutations:
#         if p.find('AA') == -1:
#             final.append(p)

#     print(i, len(final))


#print("BACT".find('AA'))

def DNA_recurrence(n):
    if n == 0:
        return 1 
    if n == 1:
        return 4
    return 3 * DNA_recurrence(n-1) + 3 * DNA_recurrence(n-2)

# for i in range(1, 7):
#     print(DNA_recurrence(i))

n = 5

total = 0
for i in range(1,n+1):
    total += 4**(n-i)

print(total) 

total = 0
for i in range(0, n):
    total += 4**i

print(total)

print((4**n - 1)/3)