peanut_butter = 2
bread = 4
jelly = 1

if peanut_butter>= 1 and bread>=2 and jelly>=1:
    print "you can make a pbj"
else:
    print "you can not make a pbj"

# First Goal: Create a program that can tell you whether or not you can make a peanut butter and jelly sandwich

# Second Goal: Modify that program to tell you: if you can make a sandwich, how many you can make

peanut_butter = 4 
bread = 11
jelly = 2

if peanut_butter >= 1 and bread >= 2 and jelly >= 1:
	print "you can make a pbj"
else:
	print "you can not make a pbj"


if peanut_butter >= 1 and bread >= 2 and jelly >= 1:
	print "you can make {0} pbj sandwich".format(min(bread/2,peanut_butter,jelly))
else:
	print "you do not have enough "
if peanut_butter == 0: 
	print " you need peanut_butter"
elif bread == 0:
	print "you need bread"
elif jelly == 0:
	print "you can make a peanut_butter sandwich with no jelly"
elif bread %2 is 1:
	print "you can make open face sandwich"
elif peanut_butter >= 1 and bread >= 2 and jelly >= 1:
	print "you can make {0} pbj sandwich".format(min(bread/2,peanut_butter,jelly))
else:
	print "you do not have enough "
