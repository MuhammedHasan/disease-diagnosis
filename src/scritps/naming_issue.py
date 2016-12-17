import json

econ_names = json.load(open('../dataset/ecolin-mapping.json'))

names = set([k for k, v in econ_names.items() if v != ''])

bc_names = set(open('../dataset/disease/BC.csv').readline().split(','))

hcc_names = set(open('../dataset/disease/HCC.csv').readline().split(','))

print('bc matching database names:', bc_names.intersection(names))
print('bc matching database names len:', len(bc_names.intersection(names)))
print()

print('hcc matching database names:', hcc_names.intersection(names))
print('hcc matching database names len:', len(hcc_names.intersection(names)))
print()

print('hcc matching bc:', hcc_names.intersection(bc_names))
print('hcc matching bc len:', len(hcc_names.intersection(bc_names)))
print()
