# input standard function : 'input'
response='y'
while response=='y':
	print ("\n Enter your information please:  ")
	#name= input ("\n name:  ")
	height= float(input ("\n height:  "))
	weight= float(input ("\n weight:  "))
	# sex= input ("\n sex:  ")
	# age= input ("age:  ")
	# claculation of body mass index 
	bmi=weight/(height*height)
	print ("your body mass index is: ", bmi, "  So, you are: ")
	if bmi<18.5:
		print ("under_weight")
	elif bmi<25:
		print ("ideal_wight")
	elif bmi<30:
		print("over_weight")
	else:
		print("obese")
	print("\n\n\n")
	if bmi>30:
		minus1= weight-height*height*30
		minus2= weight-height*height*25
		print ("You should loss more than : ", minus1," kg to pass to over_weight and more than: ",minus2," kg to pass to ideal_wight")
	elif bmi>25:
		minus2= weight-height*height*25
		print ("You should loss more than: ",minus2," kg to pass to ideal_wight")
	elif bmi>18.5:
		print ("You should preserve your weight")
	else:
		plus= height*height*25-weight
		print ("You should gain more than: ",plus," kg to pass to ideal_wight")
	response=input(" \n\n\n again! (Yes[y]/No[n]): ")		