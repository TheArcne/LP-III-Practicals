#Practical 3

def knapsack_dp(capacity, weights, values, n): 
    dp = [0 for _ in range(capacity + 1)] 
  
    for i in range(1, n + 1): 
        for w in range(capacity, 0, -1): 
            if weights[i - 1] <= w: 
                dp[w] = max(dp[w], dp[w - weights[i - 1]] + values[i - 1]) 
  
    return dp[capacity] 
  

if __name__ == '__main__': 
    values = [60, 100, 120] 
    weights = [10, 20, 30] 
    knapsack_capacity = 50
    number_of_items = len(values) 
    print(knapsack_dp(knapsack_capacity, weights, values, number_of_items)) 

