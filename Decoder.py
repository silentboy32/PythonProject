



def decoder(list):
	decoded_msg = []
	for iterator in list:
		if len(iterator) <= 3:
			decode = iterator[1:] + iterator[0]
			decoded_msg.append(decode)
			
		else:
			decode  =  iterator[::-1] + ("htr")
			decoded_msg.append(decode)
			
	massage = " ".join(decoded_msg)
	print(massage)
	
	
def incoder(list):
	#	sihthtr si terceshtr egassamhtr
	decoded_msg =[]
	for iterator in list:
		if len(iterator) <= 3:
			decode = iterator[-1] + iterator[:len(iterator)-1]
			decoded_msg.append(decode)
			
		else:
	
			decode  =  iterator[::-1]
			decods = decode[3:]
			decoded_msg.append(decods)
			
	massage = " ".join(decoded_msg)
	print(massage)

		
while True:
		print()
		print()
		input_msg = input("Put the Massage _")
		lists = input_msg.split(" ")
		usr_choice = input(""" 1 for decode \n 2 for incode \n___""")
		if usr_choice == "1":
		    decoder(lists)
		else:
			incoder(lists)			
		