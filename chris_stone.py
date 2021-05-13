#!/usr/bin/env python3

import yaml

'''User specific data dictionary'''

user_data = [
    {'first_name': 'Christopher',
    'last_name': 'Stone',
    'company': 'WWT',
    'email': 'christopher.stone@wwt.com',
    'github_username': 'cmikestone'}
]

'''Convert the dictionary to a YAML file'''

with open('/Users/stonech/DevNet/user_data.yaml', 'w') as file:
    converted = yaml.dump(user_data, file)