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

#Getting data from Degiro
cash = dg.getdata(degiroapi.Data.Type.CASHFUNDS)
IWDA = dg.search_products('IWDA.AS')
rtprice = dg.real_time_price(Product(IWDA).id, dg.Interval.Type.One_Day)

