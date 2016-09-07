import pandas as pd

def compare_coeffs2(file1, file2):
	'''Compares calculated coefficients betweeen two different models
	Requirements = two input csv files with four columns - 
		Order, Term, Coefficient and Standard Error''' 
	df1 = pd.read_csv(file1, sep = ",", index_col = 1)
	df1.columns = ['Order-1', 'Coefficient-1', 'Std_error-1']
	df2 = pd.read_csv(file2, sep = ",", index_col = 1)
	df2.columns = ['Order-2', 'Coefficient-2', 'Std_error-2']
	df = pd.merge(df1, df2, how = 'outer')
	df.to_csv("coeff_compar2.csv")

compare_coeffs("coefficients_afterdoubles.csv", "coeff_singlesend.csv")