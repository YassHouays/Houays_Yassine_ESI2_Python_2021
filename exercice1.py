x = range(3000, 3200)
concat = ""
for n in x:
    if n % 7 == 0 and n % 5 == 1:
        concat+=str(n)+","
print(concat[:-1])