import screenshot
import csv

if __name__ == "__main__":
	f = open('input.csv')
	csv_f = csv.reader(f)
	firstline = True
	for row in csv_f:
		if firstline:
				firstline = False
				continue
		url = row[4]
		#url = input('What URL?')
		pic = screenshot.takepic(url)
		ratio = screenshot.analysepic(pic)

	
