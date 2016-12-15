import json

econ_names = json.load(open('../dataset/ecolin-mapping.json'))

names = set([k for k, v in econ_names.items() if v != ''])

bc_names = set(open('../dataset/disease/BC.csv').readline().split(','))

hcc_names = set(open('../dataset/disease/HCC.csv').readline().split(','))

print('bc matching names:', bc_names.intersection(names))
print('hcc matching names:', hcc_names.intersection(names))
