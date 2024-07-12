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

cash = dg.getdata(degiroapi.Data.Type.CASHFUNDS)