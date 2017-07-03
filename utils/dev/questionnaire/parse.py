import numpy as np
import pandas as pd

# suposed to join answers of the same question in a single atribute
def concatenate_answers( dataframe ):
	print ''	

# changing careear name for its number
def parse_carrears( dataframe ):
	print dataframe['Career']
	

def especify_year( year, dataframe ):
	dataframe = dataframe[ dataframe.Year == year ]
	return dataframe

# should select a range of years.
def select_years( init, end, dataframe ):
#	dataframe = dataframe[ dataframe.Year ==  ]
	return dataframe

def calculate_probabilities( attendents_dataset, approveds_dataset ):

	columns = attendents_dataset.columns
	del columns[0]
	probs = pd.DataFrame( np.zeros((attendents_dataset.shape[0], attendents_dataset.shape[1]-1)),
				index = attendents_dataset['Career'], column = columns )

	for i in range( attendents_dataset.shape[0] ):
		for j in range( attendents_dataset.shape[1] - 1 ):
			probs.iloc[i,j] = approveds_dataset.iloc[i,j+1]/attendents_dataset.iloc[i,j+1]

	return probs

#thinking...
def naive_bayes( probs, query ):
	print''
