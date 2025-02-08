import pandas
from pandas.core.interchange.dataframe_protocol import DataFrame

from generator.generator import count

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
#

#Code without group by and count method

# gray_data = len(data[data['Primary Fur Color'] == 'Gray'])
# cinnamon_data = len(data[data['Primary Fur Color'] == 'Cinnamon'])
# black_data = len(data[data['Primary Fur Color'] == 'Black'])
# # data = data[]
#
# # print(data[data.groupby('Primary Fur Color')].count('Unique Squirrel ID'))
# print(gray_data)
# data_dict = {
#     'fur_color': ['Gray','cinnamon','black'],
#     'count' : [gray_data,cinnamon_data,black_data]
# }

# Code with group by and count method

df = data.groupby(['Primary Fur Color'])['Unique Squirrel ID'].count()
print(df)

df.to_csv('sqirrel_count')