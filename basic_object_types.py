

# numbers types int and float

integerVar= 30
# tne function "print" prints on the screen its arguments
print (integerVar)
# the function "type" returns the class of its argument
print (type(integerVar))
realVar= 30.20
print ("The type of the value: ", realVar, " is: ",type(realVar))

# *******************************************************************************************

#  string type

stringVar="Good morning"
print ("The type of the value: ", stringVar, " is: ",type(stringVar))
strCitation_1= "Mohammed sayed 'the best people are the most beneficial to the people' "
strCitation_2= 'Mohammed sayed "the best people are the most beneficial to the people" ' 
strCitation_3= 'Mohammed sayed \"the best people are the most beneficial to the people\" ' 
print (strCitation_1)
print (strCitation_2)
print (strCitation_3)

#*******************************************************************************************

#  boolean type 

boolVar_1=True   # True not true
boolVar_2=False  # False not false
boolVar_3=10<5
print ("The type of the value: ", boolVar_1, " is: ",type(stringVar))
print(boolVar_3)

#*******************************************************************************************
#  list  type : multiType array

listVar=["elment_0","elment_1", 22, 33.55, "elment_4", True]    

print ("The type of the value: ", listVar, " is: ",type(listVar))
print ("The value of the ", '4', "th element of", listVar, "is ",listVar[3])

#*******************************************************************************************
#  tuple  type : multiType array of CONSTANT values

tupleVar=("elment_0","elment_1", 22, 33.55, "elment_4", True)   

print ("The type of the value: ", tupleVar, " is: ",type(tupleVar))
print ("The value of the ", '4', "th element of", tupleVar, "is ",tupleVar[3])

#*******************************************************************************************
#  dictionary  type : set of key:value couples

dictVar={"oeuf" :"egg","aurevoir": ["bye","goodbye"], "hello":["salut", "bonjour"], "Constantine": 25, "Algeirs": 16 }  

print ("The type of the value: ", dictVar, " is: ",type(dictVar))
print ("The value of the key", 'oeuf', " in the dictionary", dictVar, "is ",dictVar["oeuf"])
