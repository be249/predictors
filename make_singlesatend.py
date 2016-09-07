def make_singlesatend(inputfile):
    '''Creates new predictor list with all single terms that feature in interaction
    terms appended to the end

    Requirements: input file = list of predictors'''

    file = open("singles_at_end.csv", "w")
    file.close
    file = open("singles_at_end.csv", "r+")
    predictors = []
    working = []
    options = []

    #list of possible single substitutions (based on data from previous substitutions)
    possible_singles = ['AT131', 'AT138', 'AV272', 'DE135', 'DE158', 'DE188', 'DE190', 'DG053', 'DG078', 'DG124', 'DG172', 'DG275', 'DN031', 'DN053', 'DN133', 'DN216', 'EG135', 'EK135', 'EK156', 'FS219', 'FY219', 'GK135', 'HN075', 'IM067', 'IN145', 'IR208', 'IS145', 'IT121', 'IT214', 'IV088', 'IV112', 'IV196', 'IV213', 'KN122', 'KN145', 'KR050', 'KR201', 'KR220', 'LQ226', 'LS157', 'NS045', 'NS133', 'NS145', 'NS193', 'NS209', 'NS278', 'NT262', 'NT276', 'PS227', 'PS289', 'PT143', 'SY219']
    
    #open latest predictors csv file
    lastpredict = open(inputfile, "r")

    #add each item in the latest predictors file to a list of predictors and to a final predictors.csv file
    for line in lastpredict:
    	file.write(line)
    	working.append(line)

    #make sure predictors don't have "\n" in their name, and add them to predictors list
    for item in working:
    	output = item.replace("\n", "")
    	predictors.append(output)

    #add additional single terms back into the predictors list
    for item in predictors:
        #separate out interaction terms into their constitent parts
        if len(item) > 5:
            stage1 = item.replace(":", "_")
            stage2 = stage1.replace("\n", "")
            new_options = stage2.split(':' and '_')
            #see if single term from interaction terms should be included in predictors
            for new_item in new_options:
                if new_item not in predictors:
                    if new_item in possible_singles:
                        file.write("\n")
                        file.write(new_item)
                        #predictors.append(new_item) 
    file.close()
    
    #print singles at end predictor list to screen
    print predictors 

#run function
make_singlesatend("predictors_51.csv")	
