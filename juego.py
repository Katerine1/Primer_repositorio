import random #random, import fuction
# Uninitialized variable for loop "while"
j=1
while j<=4:
	generator=random.randint(1,20)
	print generator
	i=1
	#"While" for counting the turns of the game 
	while i<=4:
		number=input("Insert a number of 1 - 20: ")
	# "if" statement coming if the number is equal to the generator and show message "You win"
		if generator==number:
			print "You Win"
			again=raw_input("Do you want to play again, yes or no?: ")	
			if again=="yes":
				j+=1
				break
			elif again=="no":
		# Use "break" for exit of the loop
				j=5
				i=5
				break
	
	#"elif" comes when the number is lower than generated
		elif generator>number:
			print "Your number is lower than generated, try again"
	#When the number is lower , the loop adds a number to the counter variable "i"
			i+=1
	#"elif" comes when the number is higher than generated
		elif generator<number:
			print "Your number is higher than generated, try again"
	#When the number is higher, the loop adds a number to the counter variable "i"
			i+=1	
		#When loop end and all turns are not correct then show message "Game over"
		if i==5:
			print "Game over"
			#Variable "again" show message input to play again or not
			again=raw_input("Do you want to play again, yes or no?: ")	
			if again=="yes":
			#variable "j" counting when "again"=yes
				j+=1
			elif again=="no":
				print "Game over"
				j=5
				i=5
				break
				