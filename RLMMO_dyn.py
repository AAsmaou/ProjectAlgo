def rendu_monnaie_mem(P,X):
  mem = [0]*(X+1)
  return rendu_monnaie_mem_c(P,X,mem)

def rendu_monnaie_mem_c(P,X,m):
  if X==0:
    return 0
  elif m[X]>0:
    return m[X]
  else:
    mini = 1000
    for i in range(len(P)):
      if P[i]<=X:
        nb=1+rendu_monnaie_mem_c(P,X-P[i],m)
        if nb<mini:
          mini = nb
          m[X] = mini
  return mini
