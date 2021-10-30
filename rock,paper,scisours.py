import  random
twpunkty = float(0)
btpunkty = float(0)

while True:
	ty = float(input("🪨-1, 📄-2, ✂️-3 ❌-4:"))
	bot = float(random.randrange(2))
	
	if (bot==0 and ty==1):
		print("draw")
		
	elif (bot==0 and ty==2):
		print("You Win.")
		twpunkty += 1
		print(twpunkty ,"-", btpunkty)
		
	elif (bot==0 and ty==3):
		print("Opponent Win.")
		btpunkty += 1
		print(twpunkty ,"-", btpunkty)
		
	elif (bot==1 and ty==1):
		print("Opponent Win.")
		btpunkty += 1
		print(twpunkty ,"-", btpunkty)
		
	elif (bot==1 and ty==2):
		print("draw")
		
	elif (bot==1 and ty==3):
		print("Opponent Win.")
		twpunkty += 1
		print(twpunkty ,"-", btpunkty)
	
	elif (bot==2 and ty==1):
		print("You Win.")
		twpunkty += 1
		print(twpunkty ,"-", btpunkty)
		
	elif (bot==2 and ty==2):
		print("Opponent Win.")
		btpunkty += 1
		print(twpunkty ,"-", btpunkty)
		
	elif (bot==2 and ty==3):
		print("draw")
		
	elif(ty==4):
		break
		
	else:
		print("Error")
		
	
	
