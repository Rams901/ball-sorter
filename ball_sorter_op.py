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