# Function to find the the best way to get a change of N
def greedy(change, start, return_coins):
    
    global list_coins

    #clean-up phase: find the next candidates for the next choice
    while (change < list_coins[start]): #find the next coin
      start = start + 1

    coin = list_coins[start] #greedy choice
    return_coins.append(coin)
    change = change - coin

    if change == 0:
        return #stop recursion
    
    greedy(change, start, return_coins)
    
   

 #main function
if __name__ == '__main__':
    print("START GREEDY PROGRAM")

    # coins of given denominations
    list_coins = [200, 100, 50, 20, 10, 5, 2, 1]
    #list_coins = [6, 4, 1]
    #list_coins = [50, 30, 10, 5, 3, 1]
    #list_coins = [9, 6, 5, 1]

 
    #total change required
    change = 190

    #declare variables for the function
    return_coins = []
    start = 0
    
    greedy(change, start, return_coins)

    print("The best way to give back change", change,  "is: ", return_coins)
    print("End program")
