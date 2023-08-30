import dask.dataframe as dd
import multiprocessing
import os
import pandas as pd
import yaml
import warnings

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from typing import Optional

warnings.filterwarnings('ignore')

# Settings, Config path is true/false change.
plug_config: Optional[str] = '~/config/load.yml'

# Settings, Loading File PATH.
plug_main: Optional[str] = 'Home_File'

# Use vim-plug, Set the dictionary.
if os.path.exists(os.path.expanduser(plug_config)):
    with open(os.path.expanduser(plug_config)) as yml:
        config = yaml.safe_load(yml)

    # Get Receiver/Ruby Method Complete.
    with open(os.path.expanduser(config[plug_main])) as r_meth:
        data_main = list(r_meth.readlines())

    pd_ruby = pd.Series(data_main)
    sort_r = pd_ruby.sort_index()
    ddf = dd.from_pandas(data=sort_r, npartitions=multiprocessing.cpu_count())
    data_array = ddf.to_dask_array(lengths=True)
    data = data_array.compute()
    data_main = list(map(lambda s: s.rstrip(), data))

    le = LabelEncoder()
    le.fit(data_main)
    num_ran = range(0, 3333)

    # print(le.classes_)
    # print(le.transform(data_main))
    # print(le.inverse_transform(num_ran))

    # print(le.classes_)
    data_num = le.transform(data_main)
    # print(le.inverse_transform(num_ran))

    # print(data_main)

    data_dummies_x = pd.get_dummies(data_num)
    feature_x = data_dummies_x.loc[:, '0':'3332']  # type: ignore[misc]

    x = feature_x.values
    y = data_dummies_x[3332].values

    # print("x.shape {} y.shape {}".format(x.shape, y.shape))
    # print(data_dummies_x.head())

    # print("\n")

    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)
    logreg = LogisticRegression()
    logreg.fit(x_train, y_train)

    # x_pred = logreg.fit(x_train, y_train).predict(x_test)
    # print(x_pred)

    print(f"テストスコア: {round(logreg.score(x_test, y_test)*100)}%\n")
