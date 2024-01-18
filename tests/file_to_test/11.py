import argparse
import json
import yaml
ans_dict ={}
def recurse(first_file,full_path = [], recurce_deep = 0 , coren = []):

	for i in first_file:
		if recurce_deep == 0:
			coren = first_file.keys()
		if i in coren:
			full_path = []
		if type(first_file[i]) is dict:
			full_path.append(i)
		#	recurce_deep += 1
			recurse(first_file[i], full_path, recurce_deep+1, coren = coren)

		else:
			full_path.append(i)
			#recurce_deep -=1
			#print(recurce_deep)
			#print(first_file[i], full_path)
			ans_dict[tuple(full_path)] = first_file[i]
			full_path.pop(len(full_path)-1)


with open("file_recurse2.json") as fh2:
	first_file = yaml.load(fh2, Loader=yaml.FullLoader)
	ans_dict = {}
	recurse(first_file)
	ans_1 = ans_dict
	print(ans_1)



with open("file_recurse.json") as fh:
	second_file = yaml.load(fh, Loader=yaml.FullLoader)
	ans_dict = {}
	recurse(second_file)
	ans_2 = ans_dict
	print(ans_2)
result_of_sravneniya_files = []
for i in ans_1:
	if i in ans_2:
		print(i)
		if ans_1[i] == ans_2[i]:
