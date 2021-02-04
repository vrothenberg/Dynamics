#CSE 21 HW 0

import random
import math 


def marbles(red=25, green=25, trials=100, debug=False):
    '''
    Empirically calculates the probability that the final marble will be red or green, from a bag of red and green marbles.
    If two chosen marbles are the same color then they are removed and one green marble is put into the bag.
    If two chosen marbles are different colors then they are removed and one red marble is put into the bag.
    '''
    final_red = 0
    final_green = 0
    for i in range(trials):
        num_red = red 
        num_green = green
        print(f"Trial %d" % (i+1))
        while num_red + num_green > 1:
            m1 = random.randint(1, num_red + num_green)
            m1_color = ''
            if m1 <= num_red:
                # First marble is red 
                num_red -= 1 
                m1_color = 'red'
            else: 
                # First marble is green 
                num_green -= 1 
                m1_color = 'green' 

            m2 = random.randint(1, num_red + num_green)
            m2_color = ''
            if m2 <= num_red: 
                # Second marble is red
                num_red -= 1
                m2_color = 'red'
            else:
                # Second marble is green
                num_green -= 1
                m2_color = 'green'

            if m1_color == m2_color: 
                # Same color 
                num_green += 1
            else:
                # Different colors
                num_red += 1
            if debug:
                print(num_red, num_green)
        if num_red == 1 and num_green == 0:
            final_red += 1
        elif num_green == 1 and num_red == 0:
            final_green += 1
        
    print("Reds: %d Greens: %d " %(final_red, final_green))



#marbles(25, 25, trials=10, debug=True)


def min_puzzle_moves(n,m):
    x = math.floor(math.log(n*m, 2))
    moves = 0
    pieces = m*n
    steps = 0
    while pieces > 1:
        steps += 1
        moves += math.floor(pieces / 2)
        pieces = math.ceil(pieces / 2)
        
    print(moves, steps, m*n)

        

min_puzzle_moves(5,5)