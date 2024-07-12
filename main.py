import degiroapi
import os

from degiroapi.product import Product
from degiroapi.order import Order
from degiroapi.utils import pretty_json

dg = degiroapi.DeGiro()
dg.login()