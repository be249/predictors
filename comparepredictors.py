def comparepredictors(predictors1, predictors2):
	'''Compares predictors predicted by two different models.
	Separates out predicted amino acid substitutions into three sets: shared, only
		in the first model, and only in the second model'''

	file1 = open(predictors1, "r")
	file2 = open(predictors2, "r")
	set1 = []
	set2 = []
	shared_set = []
	set1_only = []
	set2_only = []

	#create lists of each set of predictors
	for line in file1:
		set1.append(line)
	for line in file2:
		set2.append(line)

	#clean up predictor lists to remove new lines
	for item in set1:
		item.replace("\n", "")
	for item in set2:
		item.replace("\n", "")

	#sort items from set1
	for item in set1:
		if item in set2:
			shared_set.append(item)
		else:
			set1_only.append(item)

	#sort items from set2
	for item in set2:
		if item in set1:
			if item not in shared_set:
				shared_set.append(item)
		else:
			set2_only.append(item)

	#create output csv file
	output = file("predictor_comparison.csv", "w")
	output.write("Items in both predictor lists:\n")
	for item in shared_set:
		output.write(item)
	output.write("\n")
	output.write("Items only in predictor file %s" % file1.name+": \n")
	for item in set1_only:
		output.write(item)
	output.write("\n"+"\n")
	output.write("Items only in predictor file %s" % file2.name+": \n")
	for item in set2_only:
		output.write(item)

	#print to terminal if you want
	#print "Items in both predictor lists: %s" % shared_set
	#print "Items only in first predictor list: %s" %set1_only
	#print "Items only in second predictor list: %s" %set2_only

#Call function
#comparepredictors("predictors.csv", "predictors_51.csv")

