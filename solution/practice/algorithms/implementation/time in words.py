hours = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"even",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"ninteen",20:"twenty",21:"twenty one",22:"twenty two",23:"twenty three",24:"twenty four",25:"twenty five",26:"twenty six",27:"twenty seven",28:"twenty eight",29:"twenty nine"}
h = input()
m = input()
if m==30:
	print "half past "+hours[h]
elif m==15:
	print "quarter past "+hours[h]
elif m==45:
	print "quarter to "+hours[h+1]
elif m==0:
	print hours[h]+" "+"o' clock"
elif m<30:
	if m==1:
		print hours[m]+" "+"minute past "+hours[h]	
	else:
		print hours[m]+" "+"minutes past "+hours[h]
elif m>30:
	k = 60-m
	if k==1:
		print hours[k]+" "+"minute to "+hours[h+1]	
	else:
		print hours[k]+" "+"minutes to "+hours[h+1]
