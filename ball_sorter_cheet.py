#  you specify N = number of buckets, and an equal number of balls. Imagine all buckets a placed in a line, numbered from
# bucket 1 to lets say 4 (N=4). You start with all the 4 balls placed inside a single bucket (could be any one of the 4).
# And your destination is to distribute all the balls evenly across the buckets- so the end state is one ball per bucket.
# You can only move one ball from one bucket to the next in each move 


def optimal_n_moves(n, init_bucket):
 
 buckets = [0] * (n-1)
 buckets.insert(init_bucket, n)

 moves = 0
 center = init_bucket

 for i in range(center, n-1):
    buckets[i+1] =  (n - i -1)
    buckets[i] -= buckets[i + 1]
    moves += buckets[i+1]

 for i in range(center, 0, -1):
    buckets[i-1] = i 
    buckets[i] -= buckets[i - 1]
    moves += buckets[i-1]
    
 return moves

# What's a move?
# Move one ball to the next.
# So if index is 0; a ball will keep moving until the end of balls
# 4, 0, 0, 0 -> 3, 1, 0, 0 -> 2, 2, 0, 0 -> 1, 3, 0, 0 -> 1, 2, 1, 0 -> 1, 1, 2, 0 -> 1, 1, 1, 1 : 6 moves
# 4, 0, 0, 0 -> 3, 1, 0, 0 -> 3, 0, 1, 0 -> 3, 0, 0, 1 -> 2, 1, 0, 1 -> 2, 0, 1, 1 -> 1, 1, 1, 1 : 6 moves

# 0, 0, 4, 0 -> 0, 0, 3, 1 -> 0, 1, 2, 1 -> 0, 2, 1, 1 -> 1, 1, 1, 1 : 4
# 0, 0, 4, 0 -> 0, 0, 3, 1 -> 0, 1, 2, 1 -> 1, 0, 2, 1 -> 1, 1, 1, 1: 4

# 0, 0, 4, 0 -> 0, 0, 3, 1 -> 0, 1, 2, 1 -> 1, 0, 2, 1 -> 1, 1, 1, 1

# 0, 0, 5, 0, 0 -> 0, 1, 4, 0, 0 -> 0, 1, 3, 1, 0 -> 1, 0, 3, 1, 0 -> 1, 0, 3, 0, 1 -> 1, 1, 2, 0, 1 -> 1, 1, 1, 1, 1
# 0, 0, 5, 0, 0 -> 0, 1, 4, 0, 0 -> 1, 0, 4, 0, 0 -> 1, 1, 3, 0, 0 -> 
# As long as each move doesn't go back and we don't re-do actions and keep on filling the buckets in the right way, it's valid.
# Run this as algorithm first;
# 5
# 0, 0, 0, 5, 0, 0
# 0, 0, 0, 4, 1, 0
# ... 3, 2, 0
# ... 3, 1, 1

# Algorithm Implementation
# You look at right, how many buckets there? Let's say it's 2, you make 2 moves right.
# When done, switch center to the i+1 Right there is one you finish that.
# You switch to the position that has more than 1 ball.
# Flip direction to left, and start working there.
# moves = 0
# center = init_bucket
# # Right Direction
# for i in range(center, n-1):
 
#  buckets[i+1] =  (n - i -1)
#  buckets[i] -= buckets[i + 1]
#  moves += buckets[i+1]
#  print(buckets, moves)

# # Left Direction
# for i in range(center, 0, -1):
#  buckets[i-1] = i 
#  buckets[i] -= buckets[i - 1]
#  moves += buckets[i-1]
#  print(buckets, moves)
