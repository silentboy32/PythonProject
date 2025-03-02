import random

print('''
 ######           ##          ## #       ###    #####
 ##                 ####        ##  #    #  ##    ##
 ##    ##       ##   ##      ##   #  #   ##    #####
 ######     #######    ##      #    ##    ##                     ##    ##         ##   ##            ##   #####
________________________________________________________################################
________________________________________________________
  ''')
while True:
	user_input = int(input(" 1. For Play \n 2. For Exit \n ##_____"))
	print()
	us = ["Rock","Paper","Scissor"]
	us_count = 0
	chcount = 0
	if user_input == 1:
		print("Game Starts......")
		print()
		for loop in range(1,6):
			computer = random.choice(us)
			user = int(input(f" 1. Rock \n 2. Paper \n 3.Scissor \n Enter {loop}th Choice:__"))
			print()
			
			if user ==1:
				ser="Rock"
			elif user ==2:
				ser = "Paper"
			else:
				ser = "Scissor"
			print(f"You Selected {ser}.\n Computer selected {computer}")
			print()	
			if ser == computer:
				print(f"You {ser}\n computer {computer} \nValue is Same \n Session {loop}th Draw !!")
				print()
			
			elif ( ser=="Scissor" and computer=="Paper") or ( ser == "Paper" and computer =="Rock") or ( ser=="Rock" and  computer =="Scissor"):
				print("You Won !")
				us_count+=2
				print("Your Point__",us_count)
				print("Computer Point__",chcount)
				print()
			
			else:
				chcount+=2
				print()
				print("Computer Won !")
				print("Your Point__",us_count)
				print("Computer Point__",chcount)
				print()
		
		print(f" Your Point__{us_count}.\nComputer Point__{chcount}.")	
		if us_count >= chcount:
			print(f"Final !{us_count} \n You Won The Match")
		else:
			print(f"Final ! {chcount}\n Computer Won The Match")
	else:
		exit()