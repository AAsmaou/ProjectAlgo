# Function to find the the best way to get a change of N
def greedy(change, start, return_coins):
    
    global list_coins

    coin = list_coins[start] #greedy choice
    return_coins.append(coin)
    change = change - coin

    if change == 0:
        return #stop recursion

    #clean-up phase: find the next candidates for the next choice
    while (change < list_coins[start]): #find the next coin
      start = start + 1
    
    greedy(change, start, return_coins)
    
   

 #main function
if __name__ == '__main__':
    print("START GREEDY PROGRAM")

    # coins of given denominations
    list_coins = [200, 100, 50, 20, 10, 5, 2, 1]
    #list_coins = [6, 4, 1]
    #list_coins = [50, 30, 10, 5, 3, 1]
    #list_coins = [9, 6, 5, 1]

 
    # total change required
    change = 190

    # declare a list for hosting the coins for the change to return 
    return_coins = []
    i = 0
    start = 0

    #find the first greedy choice to start the algorithm
    while change < list_coins[i]:
        i = i + 1
    start = i
    
    greedy(change, start, return_coins)

    print("The best way to give back change", change,  "is: ", return_coins)
    print("End program")
