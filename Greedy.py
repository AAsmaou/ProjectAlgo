# Function to find the total number of ways to get a change of `N` from an
# unlimited supply of coins in set `S`
def greedy(change, start, return_coins):
    
    global list_coins

    coin = list_coins[start]
    

    #check whether to keep the current coin for the next iteraction or not. Eg. 0.40 = 0.20 + 0.20
    if change >= coin:

        change = change - coin
        return_coins.append(coin)

    else:
        start = start + 1

    if change == 0:
        return #stop recursion

    greedy(change, start, return_coins)
    
   

 #main function
if __name__ == '__main__':
 
    # coins of given denominations
    list_coins = [200, 100, 50, 20, 10, 5, 2, 1]
 
    # total change required
    change = 190

    # declare a list for hosting the coins for the change to return 
    return_coins = []
    i = 0
    start = 0

    while change <= list_coins[i]:
        start = i
        i = i + 1

    greedy(change, start, return_coins)

    #trasform into decimal
    for i in range(len(return_coins)):
        return_coins[i] = return_coins[i] / 100
    
    print("START GREEDY PROGRAM")
    print("The best way to give back change is: ", return_coins)
    print("End program")
