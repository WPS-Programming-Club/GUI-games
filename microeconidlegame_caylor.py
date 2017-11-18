import time
import math

#heres a bunch of defaulted variables

worker = 1.0
capital = 1.0
money = 100
priceworker = 50
workerwage = 1
pricecapital = 500
loops = 0
timei = 1
timef = 1
timeelapsed = 1
userimput = ""
workerbuynum = ""
profitpc = 0
gross = 0
profit = 0
wperc = 1
factorypriceincreasercoefficient = 2

def stats():
    print "\n"
    print "Money: %f" % money
    print "Workers: %i" % worker
    print "Worker hire cost: %i" % priceworker
    print "Worker wage / s: %f" %workerwage
    print "Factories: %i" % capital
    print "Factory cost: %i" % pricecapital
    print "Gross sales / s: %f" % gross
    print "Profit / s: %f" % profit
    print "Workers/factory: %f " % wperc
    print "\n"

def reducefactoryprice():
    global pricecapital
    global money
    pricecapital *= .2
    money -= 10000

def reducefactorypriceincreaserate():
    global factorypriceincreasercoefficient
    global money
    factorypriceincreasercoefficient *= .75
    money -= 100000

def lowerminimumwage():
    global workerwage
    global money
    workerwage *= .5
    money -= 50000

Reduce_Factory_Costs = ["0: Reduce factory price: $10,000 \n", "1: Reduce rate factory prices increase: $100,000 \n", "15: Exit"]
Bribe_Govt = ["0: Lower minimum wages: $50,000 \n", "15: Exit"]

Upgrades = [Bribe_Govt, Reduce_Factory_Costs]
Upgradesgui = "\n 0: Bribing/lobbying \n 1: Factory cost reduction \n"

print " \n W e l c o m e   t o   M i c r o e c o n o m i c s   I d l e ! \n                   Type help for controls\n            For the love of god enter valid inputs \n    ps: If you somehow manage to run out of money you loose \n"
while True:
    userimput = raw_input("Enter a command: ")

    if userimput == "help":
        print"\n worker = hire a new worker \n factory = buy another factory \n upgrades = see upgrade categories (pick a category to see upgrades in category)"

    if userimput == "upgrades":
        print Upgradesgui
        upgradecategorychoice = int(raw_input("Which category would you like to see? "))
        categorychoicestr = ""
        categorychoicestr = categorychoicestr.join(Upgrades[upgradecategorychoice])
        print
        print categorychoicestr
        print

        upgradechoice = int(raw_input("Pick an upgrade or exit. "))
        if upgradecategorychoice == 0:
            if upgradechoice == 0:
                lowerminimumwage()
        if upgradecategorychoice == 1:
            if upgradechoice == 0:
                reducefactoryprice()
            if upgradechoice == 1:
                reducefactorypriceincreaserate()

    if userimput == "worker":
        workerbuynum = int(raw_input("How many workers do you want?"))
        money -= workerbuynum * priceworker
        worker += workerbuynum

    if userimput == "factory":
        money -= pricecapital
        pricecapital *= factorypriceincreasercoefficient
        capital += 1

    if loops % 2 == 0:
        timei = time.time()
    if loops % 2 == 1:
        timef = time.time()
    if loops == 0:
        timef = time.time()
        timei = time.time()

    wperc = worker / capital
    logentry = wperc * .16 + 1
    log = math.log10(logentry)
    gross = ((100 * log) - (.5 * wperc)) * capital
    profit = gross - (workerwage * worker)
    loops += 1

    timeelapsed = abs(timef - timei)
    profitpc = profit * float(timeelapsed)
    money += profitpc
    stats()
    if money < 0:
        break

print
print "Your buisness went under!"
print "%i workers were fired" % worker
print "%i factores were closed" % capital
print "Better luck next time!"
