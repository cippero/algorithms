# find the odd or even number from a list with either all odds and one even or the opposite

def find_outlier(l):
  even = odd = 0
  for i in range(3):
    if l[i] % 2 == 0: even += 1
    else: odd += 1
  if odd > even: 
    return [e for e in l if e % 2 == 0][0]
  else: return [e for e in l if e % 2 != 0][0]