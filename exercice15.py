def length_of_string(str1, str2):
	if (len(str1) == len(str2)):
		print(str1)
		print(str2)

	elif (len(str1) < len(str2)):
		print(str2)
	
	else:
		print(str1)

stri1 = input(str("Entrer la première chaine: "))
stri2 = input(str("Entrer la seconde chaine: "))

print("\n")

length_of_string(stri1, stri2)