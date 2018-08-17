def get_bmi(h,w):
	bmi=w/(h*h)
	return bmi

def bmi_report(a_bmi):
	print ("\nYour body mass index is: ", a_bmi)
	if a_bmi<18.5:
		print ("So, you are: under_weight")
	elif a_bmi<25:
		print ("So, you are: ideal_wight")
	elif a_bmi<30:
		print("So, you are: over_weight")
	else:
		print("So, you are: obese")

def weight_advices(a_bmi):
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

response='y'
while response=='y':
	print ("\n Enter your information please:  ")
	#name= input ("\n name:  ")
	height= float(input ("\n height:  "))
	weight= float(input ("\n weight:  "))
	# sex= input ("\n sex:  ")
	# age= input ("age:  ")
	# claculation of body mass index 
	bmi=get_bmi(height,weight)
	bmi_report(bmi)
	print("\n")
	weight_advices(bmi)
	response=input(" \n\n\n again! (Yes[y]/No[n]): ")		