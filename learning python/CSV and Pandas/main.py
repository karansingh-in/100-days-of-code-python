# import pandas as pd
# data = pd.read_csv('./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

# grey_sq = data[data['Primary Fur Color'] == 'Gray']
# cinnamon_sq = data[data['Primary Fur Color'] == 'Cinnamon']
# black_sq = data[data['Primary Fur Color'] == 'Black']


# grey_count = grey_sq.count()
# cinnamon_count = cinnamon_sq.count()
# black_count = black_sq.count()


# new_data = {
#     'Fur color' : ['Gray', 'Cinnamon', 'Black'],
#     'count' : [grey_count.Y, cinnamon_count.Y, black_count.Y]
# }

# df = pd.DataFrame(new_data)

# df.to_csv('squirrel_count.csv', index=False)


# print(grey_sq)
# print(cinnamon_sq)
# print(black_sq)


import pandas as pd
# import turtle as t

# screen = t.Screen()
# screen.setup(600,600)
# screen.title('US states game')

# data = pd.read_csv('./50_states.csv')

# screen.addshape('blank_states_img.gif')
# t.shape('blank_states_img.gif')

# ans = screen.textinput(title='Guess the state', prompt='Enter the name of the state')
# first = ans[0].upper
# last = ans[1:].lower
# print(ans)
# print(first)
# print(last)
# screen.mainloop()

dict = {
    'name': ['karan', 'singh', 'abcd'],
    'score': [12,2,44]
}

df = pd.DataFrame(dict)
print(df)

# thsi loops through all the rows and not the traditional column way
for (key, row) in df.iterrows():
    print(row)




