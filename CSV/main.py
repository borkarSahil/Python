#   Approach 1
# with open("./weather_data.csv", mode="r") as weather_data:
#     data_list = weather_data.readlines()
#     print(data_list)

#   Approach 2
# import csv
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # print(data)
#     temperatures = []
#     for row in data:
#         # print(row)
#         if row[1] != "temp":
#             a = int(row[1])
#             temperatures.append(a)
#     print(temperatures)

#   Approach 3
import pandas

data = pandas.read_csv("./weather_data.csv")
# print(data)
print(data["temp"])