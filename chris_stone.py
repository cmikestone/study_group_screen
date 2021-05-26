
import yaml

def dict_list():
    user_data = [
         {'first_name': 'Christopher',
          'last_name': 'Stone',
          'company': 'WWT',
          'email': 'christopher.stone@wwt.com',
          'github_username': 'cmikestone'}
]
    return(user_data)
    
'''User specific data dictionary'''

def main():
    list_data = dict_list()

    with open('/Users/stonech/DevNet/user_data.yaml', 'w') as file:
        converted = yaml.dump(list_data, file)

'''Convert the dictionary to a YAML file'''

if __name__ == '__main__':
    main()