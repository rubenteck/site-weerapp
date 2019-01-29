import csv
reader = csv.reader(open(r"stations.csv"), delimiter=',')
readerTwo = csv.reader(open(r"weatherdata.csv"), delimiter=',')
filtered = filter(lambda p: 'UNITEDSTATES' == p[2], reader)
# headers
#csv.writer(open(r"stations-us.csv", 'w'), delimiter=',').writerow(h for h in headers)
#csv.writer(open(r"stations-us.csv", 'w'), delimiter=',').writerows(filtered)

with open(r"stations-us.csv", 'w') as filteredfile:
    csv_output = csv.writer(filteredfile)
    headers = ["stn", "name", "country", "latitude", "longitude", "elevation"]
    csv_output.writerow(headers)
    csv_output.writerows(filtered)

with open(r"stations-us.csv", "r") as filter_station, open(r"weatherdata-us.csv", 'w') as filteredWeather:
    csv_output = csv.writer(filteredWeather)
    filtered_reader = csv.reader(filter_station)
    headers = ["station", "date", "time", "temp", "dewp", "stp", "slp", "visib", "wdsp",
               "prcp", "sndp", "cldc", "wnddir", "frost", "rain", "snow", "hail", "thunder", "tornado"]
    csv_output.writerow(headers)
    stns = []
    for row in filtered_reader:
        stns.append(row[0])
    for row in readerTwo:
        if row[0] in stns:
            csv_output.writerow(row)
