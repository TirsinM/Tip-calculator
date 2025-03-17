print("Welcome to the tip calculator!")
total_bill=float(input("What was the total bill?$\n"))
tip=float(input("how much tip would you like to give? 10, 12, or 15? \n"))
split=int(input("How many people to split the bill?\n"))

tip_final=(total_bill*tip)/100
result=(total_bill+tip_final)/split
total_result=round(result,2)

print(f"Each person should pay: {total_result} $")
