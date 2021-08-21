from model_entity import Reference
from features import *

reference_list = read_datas()

for x in reference_list:
    x.print()