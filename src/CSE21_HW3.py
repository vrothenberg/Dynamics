# from itertools import product


# def is_palindrome(s):
#     if len(s) <= 1:
#         return True 
#     if s[0] != s[-1]:
#         return False 
#     return is_palindrome(s[1:-1])



# DNA = 'ACGT'
# p = product(DNA, repeat=7)


# count = 0
# for j in list(p):
#     s = ''.join(j)
#     if is_palindrome(s):
#         print(s)
#         count += 1

# print(count)

# import math 
# from scipy.special import comb 

# def nCr(n,r):
#     f = math.factorial
#     return f(n) // f(r) // f(max(1,n-r))

# rank = nCr(107, 9) + nCr(105, 8) + nCr(103, 7) + nCr(101, 6) + nCr(84, 5) + nCr(67, 4) + nCr(50, 3) + nCr(33, 2) + nCr(16, 1)
# print(rank)
# print(nCr(107,9))
# print(comb(107,9))


def integer_equation():
    ''' a + b + c + d + e = 20 '''
    solutions = 0
    for a in range(3,21):
        for b in range(11):
            for c in range(21):
                for d in range(21):
                    for e in range(21):
                        if a + b + c + d + e == 20:
                            solutions += 1
    return solutions 

print(integer_equation())


