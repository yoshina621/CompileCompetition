import pandas as pd
import glob
import csv


year = "2019CompetitionMID"
leags = ["SpeedRunning", "Standard"]
characters = ["ZEN", "GARNET", "LUD"]
win = {"MultiHead": 0, "Dora": 0, "ReiwaThunder": 0, "LGISTBot": 0}
remainingHP = {"MultiHead": 0, "Dora": 0, "ReiwaThunder": 0, "LGISTBot": 0}
frames = {"MultiHead": 0, "Dora": 0, "ReiwaThunder": 0, "LGISTBot": 0}

def standard(year, leags, characters, win, remainingHP):
	for chara in characters:
		path = year+"/"+chara+"_"+leags[1]+"/point"
		# print(path)
		files = glob.glob("./"+path+"/*.csv")
		print(files)
		# print(len(files))
		l = []
		for log in files:
			s = log.split("_")
			playe1 = s[2]
			playr2 = s[3]

			print(playe1)
			print(playr2)
			

			# f = open(log, 'r')
			# reader = csv.reader(f)
			# # header = next(reader)
			# for row in reader:
			# 	print(row)
			
			# # print(reader[0])

			# f.close()
			


##aaa


# df = pd.read_csv('./some.csv')

# print df       # show all column
# print df['A']  # show 'A' column


def speed_running(year, leags, characters, AI):
	pass



standard(year, leags, characters, win, remainingHP)