import json

econ_names = json.load(open('../dataset/naming/ecolin-mapping.json'))
econ_names = set([k for k, v in econ_names.items() if v != ''])

human_names = json.load(open('../dataset/naming/human-mapping.json'))
human_names = set([k for k, v in human_names.items() if v != ''])

bc_names = set(open('../dataset/disease/BC.csv').readline().split(','))
hcc_names = set(open('../dataset/disease/HCC.csv').readline().split(','))


print('hcc matching bc:', hcc_names.intersection(bc_names))
print('hcc matching bc len:', len(hcc_names.intersection(bc_names)))
print()

print('-' * 10, 'ecolin', '-' * 10)
print('bc matching database names:', bc_names.intersection(econ_names))
print('bc matching database names len:',
      len(bc_names.intersection(econ_names)))
print()

print('hcc matching database names:', hcc_names.intersection(econ_names))
print('hcc matching database names len:',
      len(hcc_names.intersection(econ_names)))
print()

print('-' * 10, 'human', '-' * 10)
print('bc matching database names:', bc_names.intersection(human_names))
print('bc matching database names len:',
      len(bc_names.intersection(human_names)))
print()

print('hcc matching database names:', hcc_names.intersection(human_names))
print('hcc matching database names len:',
      len(hcc_names.intersection(human_names)))
print()
