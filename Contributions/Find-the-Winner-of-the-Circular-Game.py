
def find_winner(string, n) :

	string1= ""; string2 = "";
	for i in range(n) :

		if (i % 2 == 0) :

			string1 += string[i];
		
		else :

			string2 += string[i];
			
	string1 = "".join(sorted(string1))
	string2 = "".join(sorted(string2))

	if (string1 < string2) :
		print("A", end = "");
		
	elif (string2 < string1) :
		print("B", end = "");
		
	else :
		print("Tie", end = "");

if __name__ == "__main__" :

	string = "geeksforgeeks";
	n = len(string);

	find_winner(string, n);


