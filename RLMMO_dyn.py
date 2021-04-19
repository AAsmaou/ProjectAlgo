def NBP(S,N):
# initialization of table to store the different ways to give back change
# the size of this is statique
  store = [0]*(N+1)
# calling the dynamic methods to solve the problem
  return RLMMO_dyn(S,N,store)

def RLMMO_dyn(S,N,storeMin):
# when the change is egal to 0 no coins to give 
  if N==0:
    return 0
# if the last case of our table of ways is higher than 0 return this
  elif storeMin[N]>0:
    return storeMin[N]
# search the miminim of coins
  else:
	# this variable will store the minimum of coins , we init it with a big number
    minimum = 9000
    for i in range(len(S)): # loop in the list of coins
      if S[i]<=N:#  if the first coins is leq than the change so
        nbWays=1+RLMMO_dyn(S,N-S[i],storeMin)# increment number of ways each times a new ways is found
        if nbWays<minimum: # compare the number of ways with the minimum we have fixed
          minimum = nbWays # the value of minumum become the number of ways
          storeMin[N] = minimum# the last block of our table takes the minimum value
  return minimum # at the end return the minimum


#main function
if __name__ == '__main__':
    import time
    # coins of given denominations
    list_coins = [200, 100, 50, 20, 10, 5, 2, 1]
 
    # total change required
    change = 31
    start = time.time()
    print("\n==============================START DYNAMIC PROGRAM=============================\n")
    print("\nThe minimum number of change to give back is: ", NBP(list_coins, change))
    finished = time.time() - start
    print("\n\nthe executing time is", finished)
    print("\n\n================================End of program==================================\n")

