import poloniex
import time
import threading
global bought
global BalBTC
global BalCUR
global Ticker
global SellPrice

#count = 0
polo = poloniex.Poloniex('Put your API key here')
balance = polo.returnBalances()
bought = False #CHOOSE WHETHER YOU HAVE OTHER CURRENCY ALREADY BOUGHT. TRUE IF YES AND FALSE IF NOT
alpha = 2
EMEDelay = 60
CUR = 'DGB' # SET YOUR CURRENCY HERE
CURC = 'BTC_'+CUR
Ticker = polo.returnTicker()

print(time.time())
print(polo.returnBalances()["BTC"])
def buy():
        BalBTC = float(balance['BTC'])
        BalCUR = float(balance[CUR])
        Ticker = polo.returnTicker()
        print("buy")
        BuyPrice = float(Ticker[CURC]['last'])
        buying = polo.buy(CURC,BuyPrice, float(polo.returnBalances()['BTC'])/BuyPrice)
        time.sleep(10)
        return buying
def sell():
        BalBTC = float(balance['BTC'])
        BalCUR = float(balance[CUR])
        Ticker = polo.returnTicker()
        print("Sell")
        SellPrice = float(Ticker[CURC]['last'])
        selling = polo.sell(CURC,SellPrice, float(polo.returnBalances()[CUR]))
        #orderNumber = polo.sell(CURC,SellPrice*0.998, BalCUR)['orderNumber']
        time.sleep(10)
        return selling
       
                
  
def price2A():
        Ticker = polo.returnTicker()
        global Price2A
        Price2A = float(Ticker[CURC]['last'])
def price2B():
        Ticker = polo.returnTicker()
        global Price2B
        Price2B = float(Ticker[CURC]['last'])
def price2C():
        Ticker = polo.returnTicker()
        global Price2C
        Price2C = float(Ticker[CURC]['last'])
def price2D():
        Ticker = polo.returnTicker()
        global Price2D
        Price2D = float(Ticker[CURC]['last'])
def price2E():
        Ticker = polo.returnTicker()
        global Price2E
        Price2E = float(Ticker[CURC]['last'])
def price2F():
        Ticker = polo.returnTicker()
        global Price2F
        Price2F = float(Ticker[CURC]['last'])

def printBalance():
        print("Bitcoin Balance",balance['BTC'],CUR + " Balance",balance[CUR])
def price1A():
        Ticker = polo.returnTicker()
        global Price1A
        Price1A = float(Ticker[CURC]['last'])
def price1B():
        Ticker = polo.returnTicker()
        global Price1B
        Price1B = float(Ticker[CURC]['last'])
def price1C():
        Ticker = polo.returnTicker()
        global Price1C
        Price1C = float(Ticker[CURC]['last'])
def price1D():
        Ticker = polo.returnTicker()
        global Price1D
        Price1D = float(Ticker[CURC]['last'])
def price1E():
        Ticker = polo.returnTicker()
        global Price1E
        Price1E = float(Ticker[CURC]['last'])
def price1F():
        Ticker = polo.returnTicker()
        global Price1F
        Price1F = float(Ticker[CURC]['last'])

def price3A():
        Ticker = polo.returnTicker()
        global Price3A
        Price3A = float(Ticker[CURC]['last'])
def price3B():
        Ticker = polo.returnTicker()
        global Price3B
        Price3B = float(Ticker[CURC]['last'])
def price3C():
        Ticker = polo.returnTicker()
        global Price3C
        Price3C = float(Ticker[CURC]['last'])
def price3D():
        Ticker = polo.returnTicker()
        global Price3D
        Price3D = float(Ticker[CURC]['last'])
def price3E():
        Ticker = polo.returnTicker()
        global Price3E
        Price3E = float(Ticker[CURC]['last'])
def price3F():
        Ticker = polo.returnTicker()
        global Price3F
        Price3F = float(Ticker[CURC]['last'])
while True:
     

    print("BTC " + polo.returnBalances()["BTC"]+ " " + CUR + " "+ polo.returnBalances()[CUR])
    price1A()
    time.sleep(EMEDelay)
    price1B()
    time.sleep(EMEDelay)
    price1C()
    time.sleep(EMEDelay)
    price1D()
    time.sleep(EMEDelay)
    price1E()
    time.sleep(EMEDelay)
    price1F()
    time.sleep(EMEDelay)
    EME1 = (Price1F -(Price1A+Price1B+Price1C+Price1D+Price1E)/5)*alpha+(Price1A+Price1B+Price1C+Price1D+Price1E)/5
    print(EME1)

    price2A()
    time.sleep(EMEDelay)
    price2B()
    time.sleep(EMEDelay)
    price2C()
    time.sleep(EMEDelay)
    price2D()
    time.sleep(EMEDelay)
    price2E()
    time.sleep(EMEDelay)
    price2F()
    time.sleep(EMEDelay)

    price3A()
    time.sleep(EMEDelay)
    price3B()
    time.sleep(EMEDelay)
    price3C()
    time.sleep(EMEDelay)
    price3D()
    time.sleep(EMEDelay)
    price3E()
    time.sleep(EMEDelay)
    price3F()
    time.sleep(EMEDelay)
    
    EME2 = (Price2F -(Price2A+Price2B+Price2C+Price2D+Price2E)/5)*alpha+(Price2A+Price2B+Price2C+Price2D+Price2E)/5
    EME3 = (Price3F -(Price3A+Price3B+Price3C+Price3D+Price3E)/5)*alpha+(Price3A+Price3B+Price3C+Price3D+Price3E)/5

    print(EME2)
    Grad = (EME3-((EME2+EME1)/2))/((EME2+EME1)/2)*100
    print(Grad)
    # if gradCUR1 > CUR2 and gradCUR1 > CUR3 and gradCUR1 > CUR4 and
    # gradCUR1 > CUR5 and gradCUR1 > CUR5 and
    if (Grad >0.1 and bought == False and polo.returnOpenOrders(CURC) == []):
        buy()
        if (polo.returnOpenOrders(CURC) == []):
                bought = True
    
        else:
                openOrder = int(polo.returnOpenOrders(CURC)['orderNumber'])
                print(openOrder)
                polo.cancelOrder(openOrder)
       
        
        #curbought = CUR1
    if Grad <0 and bought == True:
        sell()
        if (polo.returnOpenOrders(CURC) == []):
                bought = False
    
        else:
                openOrder = int(polo.returnOpenOrders(CURC)['orderNumber'])
                print(openOrder)
                polo.cancelOrder(openOrder)
    #count +=1


    
    

    
