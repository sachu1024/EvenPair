Even Pairs
Have the function EvenPairs(str) take the str parameter being passed and determine if a pair of adjacent even numbers exists anywhere in the string. If a pair exists, return the string true, otherwise return false. For example: if str is "f178svg3k19k46" then there are two even numbers at the end of the string, "46" so your program should return the string true. Another example: if str is "7r5gg812" then the pair is "812" (8 and 12) so your program should return the string true.
Examples
Input: "3gy41d216"
Output: true
Input: "f09r27i8e67"
Output: false

import numpy as num
def EvenPairs(strParam):
	index1=[]
	val=''
	val1=''
	# flag='false'
	# number=[]
	count=0
	
	

	for i in range(len(strParam)):
		
		# string_to_int = int(strParam[i],base=16)
		if strParam[i].isalpha():
			count=0
		elif int(strParam[i])%2==0:
			count+=1
			if count==1:
				val=i
			elif count==2:
				val1=i 
		if count==2:
			print(strParam[val],strParam[val+1:val1+1])
			return "True"
	
	return "False"		 
	 
print(EvenPairs('7r5gg812'))
print(EvenPairs('f178svg3k19k46'))
print(EvenPairs('3gy41d216'))