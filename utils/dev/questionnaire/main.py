import pandas as pd
import numpy as np
from parse import *
from question import *
import sys


def main():

	data = pd.read_csv("../../../dataset/inscr_db.csv")

	print 'You can choose one of these options:'
	# best so we can use 2 more correlation between variables plus new careears have been created.
	print '\t1 - use 3 last years of data.'
	#more data!
	print '\t2 - using all 10 last years of data.' 
	print '\t3 - specify year.'
	year = raw_input()

	print 'You can choose one of these options:'
	print '\t1 - answer questionary'
	print '\t2 - pass filename'

	opt = raw_input()
	if opt == 1:
		query = getInstance()
	else:
		query = pd.read_csv( filename )



main()
