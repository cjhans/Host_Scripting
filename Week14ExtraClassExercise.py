#Caleb Hansen, Dylan Lydic, Travis Walter, Tefera Hanamariam Gedlu
import random, logging as log

log.basicConfig(level=log.DEBUG, format=' %(asctime)s -%(levelname)s -  %(message)s')
randominput=int(input('How manyrandom IP addresses do you want?: '))


rand=0
while rand < randominput:
    IPadd=random.randint(0,255)
    IPadd2=random.randint(0,255)
    log.debug('Number stored in IPadd: ' + str(IPadd))
    log.debug('Number stored in IPadd2: ' + str(IPadd2))
    print('192.168.' + str(IPadd)+'.' + str(IPadd2))
    rand += 1
