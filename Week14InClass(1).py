#Caleb Hansen, Dylan Lydic, Travis Walter, Tefera Hanamariam Gedlu

import json, logging as log
log.basicConfig(level=log.DEBUG, format=' %(asctime)s -%(levelname)s -  %(message)s')

oppendjson=open('sample.json')
loadedjson=json.load(oppendjson)

log.debug('At index [0]:' + str(loadedjson[0]))
log.debug('At index [1]:' + str(loadedjson[1]))
log.debug('At index [2]:' + str(loadedjson[2]))

print('The drug: ' + loadedjson[0]['product_name'])
print('Came from: ' + loadedjson[0]['supplier'])
print('It will cost: ' + loadedjson[0]['unit_cost'])

print('The drug: ' + loadedjson[1]['product_name'])
print('Came from: ' + loadedjson[1]['supplier'])
print('It will cost: ' + loadedjson[1]['unit_cost'])

print('The drug: ' + loadedjson[2]['product_name'])
print('Came from: ' + loadedjson[2]['supplier'])
print('It will cost: ' + loadedjson[2]['unit_cost'])