# with open("weather_data.csv") as datafile:
#     data = datafile.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as datafile:
#
#     data = csv.reader(datafile)
#     temperature = []
#
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#
#     print(temperature)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict() # Convert data into dictionary
# print(data_dict)

# temp_list = data["temp"].to_list  # Convert data into list
# print(temp_list)

# print(data["temp"].max()) #Max is used to print maximum value in data
# print(data["temp"].mean()) #Mean is used to calculate the average of data

#Get data in cloumns
# print(data["condition"])
# print(data.condition)

#Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

#conversion of temp
# monday = data[data.day == 'Monday']
# temp_celsius = monday.temp
# print((temp_celsius * 9/5) + 32)

#create a dataframe from scratch
# data_dict1 = {
#     "students": ["Abhay", "james", "khan"],
#     "score": [76, 45, 32]
# }

# data = pandas.DataFrame(data_dict1)
# data.to_csv("New_data.csv")

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

Gray_fur = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_fur = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_fur = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

squirrel_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [Gray_fur, red_fur, black_fur]
}

squirrel_data = pandas.DataFrame(squirrel_dict)
# squirrel_data.to_csv("Squirrel_fur_details")
print(squirrel_data)