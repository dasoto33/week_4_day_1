# Please complete three problems on CodeWars. I recommend that at least one problem be of 6kyu difficulty or lower.
# Analyze and comment on the Time and Space complexity of your solution for each problem.
# Include these analyses in separate Python files or Jupyter Notebook cells alongside your solution code.

# Problem 1:

def like_counter(names):
    if len(names) == 0: #O(1)
        return "no one likes this"
    elif len(names) == 1: #O(1)
        return f'{names[0]} likes this'
    elif len(names) == 2: #O(1)
        return f'{names[0]} and {names[1]} like this'
    elif len(names) == 3: #O(1)
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    elif len(names) >= 4: #O(1)
        return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'
    
    # This function is O(1) Constant

# Problem 2:

def sum_mul(n, m):
    if n <= 0 or m <= 0: #O (1)
        return 'INVALID'
    
    total = 0
    
    for num in range(n,m,n): # O(n) loop runs m n number of times (domintating factor)
        total += num # O(1)
        
    return total

# This function is O(n) linear

# Problem 3:

def max_profit(prices):

    min_price = prices[0]
    max_profit = 0

    for price in prices: #O(N)
        min_price = min(min_price, price) #O(1)
        max_profit = max(max_profit, price - min_price) #O(1)

    return max_profit #O(1)

# This function is O(N) linear

# Problem 4:

import random

def create_show(fireworks, show_time):
    fireworks.sort() #O(n log n) Quasilinear as it is a sorting method

    show = []
    remaining_time = show_time

    while remaining_time > 0 and fireworks: 

           # Select a random firework

           firework = random.choice(fireworks) # O(1) Constant

           if firework <= remaining_time:

               # Add the firework to the show

               show.append(firework) # O(1)

               remaining_time -= firework

          else:

              # This firework is too long, remove it from consideration

              fireworks.remove(firework) # O(n) linear as it requires a search

  return show

# This function is Quasilinear O(n log n)