import numpy as np
import pandas as pd
from scipy.spatial import distance
from StringIO import StringIO

def calcdistances(inputfile, cutoff):
	''' Requirements:
			Distance matrix = x,y,z positions for each amino acid position
			input file = csv file with list of predictors - single terms in form AB123 
				and interaction terms in form AB123:CD456
			cutoff = maximum distance between two amino acids that permits an interaction
				currently thought to be in range 35-38
		
		Output:
			unreal_distances.csv = csv file with list of interaction terms and distances
				over the cutoff
			real_distances.csv = csv file with list of interaction terms and distances under
				cutoff distance
			distances.csv = csv file with complete list of interaction terms and distances
				'''

	#Opens up and creates required input and output files
	distance_matrix = pd.read_csv("distance_matrix.csv", sep = ",", index_col = 0)
	output1 = open("unreal_distances.csv", "w")
	output1.write("Unrealistic interactions\n")
	output1.write("Interaction term 1, Interaction term 2, Distance\n")
	output2 = open("real_distances.csv", "w")
	output2.write("Realistic interactions\n")
	output2.write("Interaction term 1, Interaction term 2, Distance\n")
	cutoff = float(cutoff)

	#Identifies interaction predictor terms
	file = open(inputfile, "r")
	for line in file:
		if (len(line) == 12) and (line[5] == ":"):
			a = line[:5]
			b = line[6:11]
			if a[2] == "0":
				a_pos = a[3:5]
			else:
				a_pos = a[2:5]
			if b[2] == "0":
				b_pos = b[3:5]
			else:
				b_pos = b[2:5]
			#Determines co-ordinates from distance matrix
			a_x = float(distance_matrix.loc[int(a_pos), 'x'])
			a_y = float(distance_matrix.loc[int(a_pos), 'y'])
			a_z = float(distance_matrix.loc[int(a_pos), 'z'])
			b_x = float(distance_matrix.loc[int(b_pos), 'x'])
			b_y = float(distance_matrix.loc[int(b_pos), 'y'])
			b_z = float(distance_matrix.loc[int(b_pos), 'z'])
			a_coord = (a_x, a_y, a_z)
			b_coord = (b_x, b_y, b_z)
			dist = distance.euclidean(a_coord, b_coord)

			#Prints distances to separate csv files
			if dist < cutoff:
				output2.write(a+", "+b+", "+str(dist)+"\n")
			else:
				output1.write(a+", "+b+", "+str(dist)+"\n")

	#Close files
	output1.close()
	output2.close()

	#Create combined file
	data1 = pd.read_csv("real_distances.csv", sep = ",", skiprows=range(0,2), header = None, index_col = False)
	data2 = pd.read_csv("unreal_distances.csv", sep = ",", skiprows=range(0,2), header = None, index_col = False)
	data_combined = pd.concat([data1, data2])
	data_combined.to_csv("distances.csv", index = False)

#call function with file name and cutoff distance
calcdistances("reordered_predictors_file.csv", 38.0)




