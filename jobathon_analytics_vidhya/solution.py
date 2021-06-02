import pandas as pd
from sklearn import svm, preprocessing
from time import time

def encode_features(df_train):
    df_train.Credit_Product = df_train.Credit_Product.fillna('No')

    features = ['Gender', 'Region_Code', 'Occupation', 'Channel_Code', 'Is_Active', 'Credit_Product']
    # df_combined = pd.concat([df_train[features], df_test[features]])

    for feature in features:
        le = preprocessing.LabelEncoder()
        le = le.fit(df_train[feature])
        df_train[feature] = le.transform(df_train[feature])
    return df_train


if __name__ == '__main__':
    train = pd.read_csv(filepath_or_buffer='train_s3TEQDk.csv')
    train = train.drop(['ID'], axis=1)
    t1 = time()
    print(f'Starts at {t1}')
    # x = train[(train.Is_Lead == 1) & (train.Is_Active == 'Yes')]
    # print(x)
    # print(f'No of cases where given that is_lead is 1 the person is active are {len(x)}')
    # y = train[train.Is_Lead == 1]
    # print(f'Total cases: {len(y)}')
    clf = svm.SVC()
    print(train.dtypes)
    pd.set_option("display.max_columns", None)
    #
    # print(pd.unique(train.Credit_Product))

    train = encode_features(train)

    x_train = train.drop(['Is_Lead'], axis=1)
    y_train = train['Is_Lead']

    clf.fit(x_train, y_train)

    # so by printing we know one third of the data is of those who are lead and remaing are
