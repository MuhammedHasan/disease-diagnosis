from services import NamingService, DataReader


def report_matching(a, b, a_name, b_name):
    print('%s matching %s:' % (a_name, b_name), a.intersection(b))
    print('%s matching %s len:' % (a_name, b_name), len(a.intersection(b)))
    print()


def naming_issue():

    econ_names = set(NamingService('ecolin')._names.keys())
    human_names = set(NamingService('human')._names.keys())

    dr = DataReader()
    bc_names = set(i.lower().strip() for i in dr.read_columns('BC'))
    hcc_names = set(i.lower().strip() for i in dr.read_columns('HCC'))

    report_matching(hcc_names, bc_names, 'hcc', 'bc')

    print('-' * 10, 'ecolin', '-' * 10)
    report_matching(hcc_names, econ_names, 'hcc', '')
    report_matching(bc_names, econ_names, 'bc', '')

    print('-' * 10, 'human', '-' * 10)
    report_matching(hcc_names, human_names, 'hcc', '')
    report_matching(bc_names, human_names, 'bc', '')
