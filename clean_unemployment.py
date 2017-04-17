import csv
input = open('Local_Area_Unemployment_Statistics__Beginning_1976.csv', 'rb')
output = open('cleaned_unemployment.csv', 'wb')
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
	total = float(row[3])
	unemployed = float(row[5])

	if county+year not in data:
		data[county+year] = [
			county,
			year,
			total,
			unemployed
		]
	else:
		data[county+year][2] += total
		data[county+year][3] += unemployed

rows = []
for county_year in sorted(data.keys()):
	row = [
		data[county_year][0],
		data[county_year][1],
		data[county_year][3] / data[county_year][2]
	]
	rows.append(row)

header = [
	'County',
	'Year',
	'UnemploymentRate'
]

writer.writerow(header)

for row in rows:
	writer.writerow(row)


input.close()
output.close()