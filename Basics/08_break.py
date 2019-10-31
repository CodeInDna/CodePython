####### adding a break #######
times = int(input("How many times I have to tell you? "))

for time in range(1, times):
	print("CLEAN UP YOUR ROOM")
	if time >= 4:
		print("do you even listen to me anymore?")
		break