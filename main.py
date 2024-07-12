import degiroapi
import os
from dotenv import load_dotenv

from degiroapi.product import Product
from degiroapi.order import Order
from degiroapi.utils import pretty_json

# Load Environment file
load_dotenv()

dg = degiroapi.DeGiro()
dg.login(os.getenv('DGUSERNAME'), os.getenv('DGPASSWORD'))

dg_tc = 1

#Getting data from Degiro
cash = dg.getdata(degiroapi.Data.Type.CASHFUNDS)
ETF = dg.search_products(os.getenv('DGETF'))
rtprice = dg.real_time_price(Product(ETF).id, dg.Interval.Type.One_Day)

if cash > int(os.getenv('DGCASH')):
    # Determin TOB
    tob_rate = 0.0012

    if (round(cash*tob_rate, 2)) >= 1300:
        tob = 1300
    else:
        tob = round(cash*tob_rate, 2)

    #Determin how many pieces to buy
    inv_ceiling = cash - tob - dg_tc
    pcs = int(inv_ceiling // pretty_json(rtprice[0]['data']['lastPrice']))

    # Execute Order
    dg.buyorder(Order.Type.MARKET, Product(ETF).id, 3, pcs)

#else:
#    x = ''