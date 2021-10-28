import  random
twpunkty = float(0)
btpunkty = float(0)

while True:
	ty = float(input("🪨-1, 📄-2, ✂️-3 ❌-4:"))
	bot = float(random.randrange(3))
	
	if (bot==1 and ty==1):
		print("remis")
		
	elif (bot==1 and ty==2):
		print("Punkt wędruje do ciebie.")
		twpunkty += 1
		print(twpunkty ,"-", btpunkty)
		
	elif (bot==1 and ty==3):
		print("Punkt wędruje do przeciwnika.")
		btpunkty += 1
		print(twpunkty ,"-", btpunkty)
		
	elif (bot==2 and ty==1):
		print("Punkt wędruje do przeciwnika.")
		btpunkty += 1
		print(twpunkty ,"-", btpunkty)
		
	elif (bot==2 and ty==2):
		print("remis")
		
	elif (bot==2 and ty==3):
		print("Punkt wędruje do ciebie.")
		twpunkty += 1
		print(twpunkty ,"-", btpunkty)
	
	elif (bot==3 and ty==1):
		print("Punkt wędruje do ciebie.")
		twpunkty += 1
		print(twpunkty ,"-", btpunkty)
		
	elif (bot==3 and ty==2):
		print("Punkt wędruje do przeciwnika.")
		btpunkty += 1
		print(twpunkty ,"-", btpunkty)
		
	elif (bot==3 and ty==3):
		print("remis")
		
	elif (bot==0 and ty<4):
		print("remis")
		
	elif(ty==4):
		break
		
	else:
		print("Nie ma takiej komendy")
		
	
	
