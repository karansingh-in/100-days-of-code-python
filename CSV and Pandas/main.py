import pandas as pd
data = pd.read_csv('./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

grey_sq = data[data['Primary Fur Color'] == 'Gray']
cinnamon_sq = data[data['Primary Fur Color'] == 'Cinnamon']
black_sq = data[data['Primary Fur Color'] == 'Black']


grey_count = grey_sq.count()
cinnamon_count = cinnamon_sq.count()
black_count = black_sq.count()


new_data = {
    'Fur color' : ['Gray', 'Cinnamon', 'Black'],
    'count' : [grey_count.Y, cinnamon_count.Y, black_count.Y]
}

df = pd.DataFrame(new_data)

df.to_csv('squirrel_count.csv', index=False)


# print(grey_sq)
# print(cinnamon_sq)
# print(black_sq)


