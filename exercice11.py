from bisect import bisect_left 
  
def BinarySearch(a, x): 
    i = bisect_left(a, x) 
    if i != len(a) and a[i] == x: 
        return i 
    else: 
        return -1
  
a  = [1, 2, 4, 4, 8] 
x = int(8) 
res = BinarySearch(a, x) 
if res == -1: 
    print(x, "is absent") 
else: 
    print("La première fois que l'on voit", x, "est présent au caractère numéro : ", res) 