import pyinputplus as pyin

totalcost = 0
receipt = {}
menu = {
    'bread':{'wheat bread': 1,'white bread': 0.5,'sourdough bread' : 3},
    'protein':{'chicken':1, 'turkey':2, 'ham': 0.5, 'tofu':0.3},
    'cheese':{'cheddar':0.5, 'swiss':1, 'mozzarella':2, },
    'cond':{'mayo':.1, 'mustard': .2, 'lettuce':.5, 'tomato':.8, }
}

print('Enter type of bread')
bread = pyin.inputMenu(list(menu['bread']))
receipt[bread] = menu['bread'][bread]
menu['bread'][bread] += totalcost