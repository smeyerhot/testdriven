import os
import sys
import json


def update_json_file(url):
    full_path = os.path.abspath('services/swagger/swagger.json')
    with open(full_path, 'r') as file:
        data = json.load(file)
    data['servers'][0]['url'] = url
    with open(full_path, 'w') as file:
        json.dump(data, file)
    return True


if __name__ == '__main__':
    try:
        update_json_file(sys.argv[1])
    except IndexError:
        print('http://testdriven-staging-alb-1466309556.us-west-1.elb.amazonaws.com')
        print('USAGE: python update-spec.py URL')
        sys.exit()
