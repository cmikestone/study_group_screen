#!/usr/bin/python3

import yaml

'''User specific data dictionary'''

user_data = dict([
    ('first_name', 'Christopher'),
    ('last_name', 'Stone'),
    ('company', 'WWT'),
    ('email', 'christopher.stone@wwt.com'),
    ('github_username', 'cmikestone')
])

#'''Convert the dictionary to a YAML file'''

#yaml_file = open("/Users/stonech/DevNet/user_data.yaml", "w")
#print (yaml.dump(user_data), file=yaml_file) 
#yaml_file.close()


'''Convert the dictionary to a YAML file'''

with open(r'/Users/stonech/DevNet/user_data.yaml', 'w') as file:
    converted = yaml.dump(user_data, file)