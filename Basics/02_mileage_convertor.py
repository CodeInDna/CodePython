print("How many kilometers did you run today?")
kms = float(input()) #input fn return string, so convert it to float
miles = round(kms/1.60934, 2)	#converting kms to miles #round upto 2 decimal
print(f"That is equal to {miles} miles")	