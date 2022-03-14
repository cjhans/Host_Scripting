#Caleb Hansen, Dylan Lydic, Travis Walter, Tefera Hanamariam Gedlu

import csv, logging as log
log.basicConfig(level=log.DEBUG, format=' %(asctime)s -%(levelname)s -  %(message)s')

openAccessCSV = open('accesslog.csv')
dictReadAccessCSV = csv.DictReader(openAccessCSV)

log.debug(dictReadAccessCSV)

#print(dictReadAccessCSV)

for line in dictReadAccessCSV:
    print('IP: ' + line['IP'])