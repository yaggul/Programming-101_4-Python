import sys
import json

with open(sys.argv[1],'r') as filein:
    data = json.load(filein)

new_dict = {}

def gen_simple_dict():
    for i in data.keys():
        for j in data[i]:
            for k in j['skills']:
                if k['name'] not in new_dict.keys():
                    new_dict[k['name']] = {}
                    new_dict[k['name']].update({k['level']:j['first_name']+' '+j['last_name']})
                else:
                    new_dict[k['name']].update({k['level']:j['first_name']+' '+j['last_name']})
    return new_dict


def gen_result(my_dict):
    for k,v in new_dict.items():
        print(k+' - '+v[max(v.keys())])

gen_result(gen_simple_dict())
