import pandas as pd


def average_data():
    path = '../dataset/disease'

    df = pd.read_csv('%s/BC.csv' % path, header=0)

    df_h = df[(df.stage == 'h')]
    df_bc = df[(df.stage != 'h')]

    df = pd.read_csv('%s/HCC.csv' % path, header=0)

    df_h = pd.concat([df_h, df[(df.stage == 'h')]])
    df_hcc = df[(df.stage != 'h')]

    path = '../dataset/avg-disease'

    df_test_h = df_h.sample(n=3)
    df_test_h.to_csv('%s/test_h.csv' % path)

    df_test_bc = df_bc.sample(n=3)
    df_test_bc.to_csv('%s/test_bc.csv' % path)

    df_test_hcc = df_hcc.sample(n=3)
    df_test_hcc.to_csv('%s/test_hcc.csv' % path)

    df_h.drop(df_test_h.index).mean().to_csv('%s/train_h.csv' % path)
    df_hcc.drop(df_test_hcc.index).mean().to_csv('%s/train_bc.csv' % path)
    df_bc.drop(df_test_bc.index).mean().to_csv('%s/train_hcc.csv' % path)
