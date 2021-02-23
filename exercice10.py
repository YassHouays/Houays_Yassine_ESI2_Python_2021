subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]

res = [[i, j, k] for i in subjects  
                 for j in verbs 
                 for k in objects] 
for x in res:
    print(" ".join(x))