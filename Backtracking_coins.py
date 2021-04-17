import timeit

# Function to find the minimum list of coins to get a change of `N` from an
# limited supply of coins in set `list_coins`
def bk(change, return_coins):

    global best_return_coins
    global size
    global list_coins
    global N
    global N_combination
    
    for i in range(len(list_coins)):
                
        curr_coin = list_coins[i]
        return_coins.append(curr_coin)
        change = change - curr_coin
        
        #Consider only the elements that can lead to a best solution
        if change >= 0 :

            #candidate solution found
            if change == 0:
                
                #print all the possible combinations
                N_combination = N_combination + 1
                print("Combination #", N_combination," ", return_coins)
            
                #update best solutions
                if len(return_coins) <= size:
                    best_return_coins = return_coins[:]
                    size = len(best_return_coins)

            else:
                backtracking(change, return_coins)

        #backtrack step
        return_coins.pop()
        change = change + curr_coin 


# Optimized backtracking function
def bkOpt(change, return_coins):

    global best_return_coins
    global size
    global list_coins
    global N
    global N_combination
    
    for i in range(len(list_coins)):
                
        curr_coin = list_coins[i]
        return_coins.append(curr_coin)
        change = change - curr_coin
        
        #Consider only the elements that can lead to a best solution
        if change >= 0 and len(return_coins) <= size:

            #candidate solution found
            if change == 0:
                
                #print all the possible combinations
                N_combination = N_combination + 1
                print("Combination #", N_combination," ", return_coins)
            
                #update best solutions
                best_return_coins = return_coins[:]
                size = len(best_return_coins)

            else:
                backtracking(change, return_coins)

        #backtrack step
        return_coins.pop()
        change = change + curr_coin 


#main function
if __name__ == '__main__':

    start = timeit.default_timer() #start timer
  
    print("START BACKTRACKING PROGRAM")
    print("") #newline
    N_combination=0

    # coins of given denominations
    list_coins = [200, 100, 50, 20, 10, 5, 2, 1]
    #list_coins = [6, 4, 1]
    #list_coins = [3, 1]
 
    print("Set of coins: ", list_coins)
    print("") #newline

    # total change required
    N = 40

    # These variables are going to be used by the backtracking function to compute the solution 
    return_coins = []
    best_return_coins = []
    size = 1000;

    #run backtracking algo
    bk(N, return_coins)

    stop = timeit.default_timer() #stop timer

    #Print results
    print("") #newline
    print("The best way to give back the change: ", N, " is: ", best_return_coins)
    print('Time: ', stop - start)
    print("END program")

