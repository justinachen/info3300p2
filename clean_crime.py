import csv
input = open('Index_Crimes_by_County_and_Agency__Beginning_1990.csv', 'rb')
output = open('cleaned_crime.csv', 'wb')
writer = csv.writer(output)

data = {}

first = True
for row in csv.reader(input):
	if first:
		first = False
		continue

	if '' in row:
		continue

	county = row[0]
	year = row[1]
	total = int(row[2])
	violent = int(row[3])
	prop = int(row[8])
	murder = int(row[4])
	rape = int(row[5])
	robbery = int(row[6])
	assault = int(row[7])
	burglary = int(row[9])
	larceny = int(row[10])
	motor = int(row[11])

	if county+year not in data:
		data[county+year] = [
			county, 
			year, 
			total, 
			violent, 
			prop, 
			murder, 
			rape, 
			robbery, 
			assault, 
			burglary, 
			larceny, 
			motor
		]
	else:
		data[county+year][2] += total
		data[county+year][3] += violent
		data[county+year][4] += prop
		data[county+year][5] += murder
		data[county+year][6] += rape
		data[county+year][7] += robbery
		data[county+year][8] += assault
		data[county+year][9] += burglary
		data[county+year][10] += larceny
		data[county+year][11] += motor

header = [
	'County',
	'Year',
	'Total',
	'Violent Crime',
	'Property Crime',
	'Murder',
	'Rape',
	'Robbery',
	'Assault',
	'Burglary',
	'Larceny',
	'Car Theft'
]

writer.writerow(header)

for county_year in sorted(data.keys()):
	writer.writerow(data[county_year])


input.close()
output.close()