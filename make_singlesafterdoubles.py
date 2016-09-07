def make_singlesafterdoubles(tobesortedlist):
	'''Reorders predictors so that single terms are included directly after interaction terms'''
	#list of possible single substitutions (based on data from previous substitutions)
	possible_singles = ['AT131', 'AT138', 'AV272', 'DE135', 'DE158', 'DE188', 'DE190', 'DG053', 'DG078', 'DG124', 'DG172', 'DG275', 'DN031', 'DN053', 'DN133', 'DN216', 'EG135', 'EK135', 'EK156', 'FS219', 'FY219', 'GK135', 'HN075', 'IM067', 'IN145', 'IR208', 'IS145', 'IT121', 'IT214', 'IV088', 'IV112', 'IV196', 'IV213', 'KN122', 'KN145', 'KR050', 'KR201', 'KR220', 'LQ226', 'LS157', 'NS045', 'NS133', 'NS145', 'NS193', 'NS209', 'NS278', 'NT262', 'NT276', 'PS227', 'PS289', 'PT143', 'SY219']
	reordered_predictors = []
	predictors = tobesortedlist
	r_p_f= open("singles_after_doubles_list.csv", "w")
	for item in predictors:
		if len(item) == 5:
			reordered_predictors.append(item)
			r_p_f.write(item+"\n")
		if len(item) > 5:
			reordered_predictors.append(item)
			r_p_f.write(item+"\n")
			components_stage1 = item.replace(":", "_")
			components_stage2 = components_stage1.replace("\n", "")
			components = components_stage2.split("_")
			for component in components:
				if component not in reordered_predictors:
					if component in possible_singles:
						reordered_predictors.append(component)
						r_p_f.write(component+"\n")

	print reordered_predictors

#Call function with relevant list
#l1 = ['EK156', 'KN145', 'LS157:NS193', 'GK135', 'DE190:IT214', 'EG158_KR050', 'LQ226', 'DG124_FY094_HY155', 'AT131:KN145', 'DE158:KN145', 'DE190:EK135', 'DG172_IQ226_IT121_NS278_QR197', 'GK135:IR208', 'EK156:NT276', 'KN145:PS289', 'AT138:DE158', 'AT131', 'KN122:DG172_NS278_QR197', 'DG124:DN133', 'KR050:NS278', 'AT138:NS193', 'LQ226:NS193', 'DE190:PS289', 'LS157', 'DG135_DG172_KN145:IV196', 'GK135:KN145', 'DS133_NT262:FS219', 'GK135:IT214', 'LQ226:LS157', 'EG135:EK156', 'DG053', 'IR208:NT276', 'DG172:EK156', 'PT143', 'DG172_IL226_NS278_QR197:KN122', 'IT214:PS227', 'DS133_NT262:NS193', 'AV163_DV144_IV213_KN002_KN173_SY159', 'AT131:PS289', 'AT138:NS133', 'AV272:GK135', 'DG135_DG172_KN145:NS193', 'DG275:HN075', 'NT276:SY219', 'AT138:DG078', 'DE158', 'DE158:KR220', 'DE135:IM067', 'NS133', 'DE135:NS193', 'KN145:DG172_NS278_QR197', 'DG275:KN145', 'EK156', 'KN145', 'LS157', 'NS193', 'GK135', 'DE190', 'IT214', 'KR050', 'LQ226', 'DG124', 'AT131', 'DE158', 'EK135', 'DG172', 'IT121', 'NS278', 'IR208', 'NT276', 'PS289', 'AT138', 'KN122', 'DN133', 'IV196', 'NT262', 'FS219', 'EG135', 'DG053', 'PT143', 'PS227', 'IV213', 'NS133', 'AV272', 'DG275', 'HN075', 'SY219', 'DG078', 'KR220', 'DE135', 'IM067']
#make_singlesafterdoubles(l1)

