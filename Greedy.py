# Function to find the the best way to get a change of `N` 

def greedy(change, start, return_coins):
    
    global list_coins

    #greedy choice
    coin = list_coins[start]
    return_coins.append(coin)

    #clean-up phase: find the next candidates for the next choice
    change = change - coin

    #check whether to keep the current coin for the next iteraction or not. Eg. 0.40 = 0.20 + 0.20
    if change < coin:
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

    #return the first coin not higher than change
    while change <= list_coins[i]:
        start = i + 1
        i = i + 1

    greedy(change, start, return_coins)

    #trasform into decimal
    for i in range(len(return_coins)):
        return_coins[i] = return_coins[i] / 100
    
    print("START GREEDY PROGRAM")
    print("The best way to give back change is: ", return_coins)
    print("End program")
