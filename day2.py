print('Welcomme to the tip calculator!')
bill = float(input('What was the total bill? $'))
tip = float(input('how much tip would you like to give? 10, 12, or 15? '))
people = float(input('how many people are splitting the bill? '))

tip_amount = float((tip/100.00)*bill)

print('Each person should pay: $'+str((bill+tip_amount)/people))


# data types :
print(5/3) # 5 divided by 3
print(5//3) # 5 divided by 3, but only the int part is shown without rounding off
print(5**3) # 5 to the power of 3
print(round(34.3233232323, 2)) # no. to be rounded off, upto how many digits 
      

