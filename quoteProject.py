
# citations list
quotes=["If one has good manners, one may attain the same level of merit as those who spend their nights in prayer", 
		"The best among you is he who learns the Quran and teaches it","A person will be with those whom he loves (in the Hereafter)" ]
# characters (personages) list
characters=["sahih_el_boukhari", "sahih_mouslim","sounan_el_tirmidi", "sounan_el_nissai", "sounan_abi_daoud", "sounan_ibn_maja" ]

def get_random_item(myList):
	# get random number
	# get random element from myList
	chosen_quote=myList[0]
	# return the chosen element
	return chosen_quote


# Display a randomly choosen quote 
print(get_random_item(quotes))
# Ask user to hit "enter" for another citation and "b" to exit  
user_answer= input("hit 'enter' for another citation and 'B' to exit \n ")
while user_answer!= "B": 
	print(get_random_item(quotes))
	user_answer= input("hit 'enter' for another citation and 'B' to exit \n ")

# capitalizing cheracters' elements
for x in characters:
	x=x.capitalize()
	print(x)