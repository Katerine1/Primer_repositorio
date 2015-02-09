import random
i=1
while i<=4:
	generator=random.randint(1,20)
	print generator
	number=input("Insert a number of 1 - 20: ")
	if generator<number:
		print "Your number is higher than generated, try again"
		i+=1
	elif generator>number:
		print "Your number is lower than generated, try again"
		i+=1
	elif generator==number:
		print "You Win"
		break
print "Game over"
