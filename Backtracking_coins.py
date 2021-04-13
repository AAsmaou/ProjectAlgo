# Function to find the total number of ways to get a change of `N` from an
# unlimited supply of coins in set `S`
def backtracking(change, list_coins):
    global best_return_coins
    global return_coins

    global N
    
    for i in range(len(list_coins)):
        
        #define the global variable that the function is editing
        
        coin = list_coins[i]
        return_coins.append(coin)
        change = change - coin

        if change >= 0:

            if change == 0:

                #set the best list of coins as result to return
                total = sum(return_coins)

                if len(return_coins) <= len(best_return_coins) and total == N:

                 #copy list by value 
                 best_return_coins = return_coins[:]

            else:
                backtracking(change, list_coins)

        #backtrack step
        else:
            return_coins.pop()
            change = change + coin 


#function to sum all the elements of a list
def sum(list):
     sum = 0
     for i in range(0,len(list)):
        sum = sum + list[i]
     return sum


 #main function
if __name__ == '__main__':
 
    # coins of given denominations
    list_coins = [200, 100, 50, 20, 10, 5, 2, 1]
 
    # total change required
    N = 190

    # declare a list for hosting the coins for the change to return 
    return_coins = []
    best_return_coins = list_coins

    backtracking(N, list_coins)
    
    print("START BACKTRACKING PROGRAM")
    print("The best way to give back change is: ", best_return_coins)
    print("End program")
