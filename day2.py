print('Welcomme to the tip calculator!')
bill = float(input('What was the total bill? $'))
tip = float(input('how much tip would you like to give? 10, 12, or 15? '))
people = float(input('how many people are splitting the bill? '))

tip_amount = float((tip/100.00)*bill)

print('Each person should pay: $'+str((bill+tip_amount)/people))


