import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_Squirrel_Data.csv")
squirrel_color_count = ["color", "count"]
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
	"color": ["grey","Cinnamon",'Black'],
	"scores" : [gray_count, cinnamon_count, black_count]
}

data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_count.csv")
