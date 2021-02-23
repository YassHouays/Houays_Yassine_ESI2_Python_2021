nl=[]
n = int(input("Tapez la valeur de n : "))
for x in range(0, n):
  if (x%7==0):
    nl.append(str(x))
print (','.join(nl))