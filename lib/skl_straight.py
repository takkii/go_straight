from dask.dataframe.io.io import from_pandas
import gc
import multiprocessing
import os
import pandas as pd
import threading
import traceback
import yaml
import warnings

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from typing import Optional

warnings.filterwarnings('ignore')


def main():
    try:
        # Settings, use vim-plug path.
        plug_config: Optional[str] = '~/config/load.yml'
        plug_main: Optional[str] = 'Home_File'

        # Use vim-plug, Set the dictionary.
        if os.path.exists(os.path.expanduser(plug_config)):
            with open(os.path.expanduser(plug_config)) as yml:
                config = yaml.safe_load(yml)

            # Get Receiver/Ruby Method Complete.
            with open(os.path.expanduser(config[plug_main])) as r_meth:
                data_main = list(r_meth.readlines())

            pd_ruby = pd.Series(data_main)
            s_r = pd_ruby.sort_index()
            multi_pro = multiprocessing.cpu_count()
            ddf = from_pandas(data=s_r, npartitions=multi_pro)
            data_array = ddf.to_dask_array(lengths=True)
            data = data_array.compute()
            data_main = list(map(lambda s: s.rstrip(), data))

            le = LabelEncoder()
            le.fit(data_main)
            data_num = le.transform(data_main)
            data_dummies_x = pd.get_dummies(data_num)
            feature_x = data_dummies_x.loc[:, '0':'3332']  # type: ignore[misc]

            x = feature_x.values
            y = data_dummies_x[3332].values
            z = train_test_split(x, y, random_state=0)

            x_train, x_test, y_train, y_test = z
            logreg = LogisticRegression()
            logreg.fit(x_train, y_train)

            print(f"テストスコア: {round(logreg.score(x_test, y_test)*100)}%\n")

        # Config Folder not found.
        else:
            raise ValueError("None, Please Check the Config Folder")

    # TraceBack.
    except Exception:
        # Load/Create LogFile.
        except_folder: Optional[str] = 'SKL_Folder_load'
        except_file: Optional[str] = 'SKL_File_load'
        skl_straight: Optional[str] = os.path.expanduser(config[except_folder])
        debug_word: Optional[str] = os.path.expanduser(config[except_file])

        # Load the dictionary.
        if os.path.isdir(skl_straight):
            with open(debug_word, 'a') as log_py:
                traceback.print_exc(file=log_py)

                # throw except.
                raise RuntimeError from None

        # skl_straight Foler not found.
        else:
            raise ValueError("None, Please Check the skl_straight Folder.")

        # Custom Exception.
    except ValueError as ext:
        print(ext)
        raise RuntimeError from None

    # Once Exec.
    finally:
        # GC collection.
        gc.collect()


def dev_main():
    try:
        # Settings, Comment out when using Home_File.
        plug_config: Optional[str] = '~/config/load.yml'
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
            multi_pro = multiprocessing.cpu_count()
            ddf = from_pandas(data=sort_r, npartitions=multi_pro)
            data_array = ddf.to_dask_array(lengths=True)
            data = data_array.compute()
            data_main = list(map(lambda s: s.rstrip(), data))

            le = LabelEncoder()
            le.fit(data_main)
            # num_ran = range(0, 3333)

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
            z = train_test_split(x, y, random_state=0)

            # print("x.shape {} y.shape {}".format(x.shape, y.shape))
            # print(data_dummies_x.head())

            # print("\n")

            x_train, x_test, y_train, y_test = z
            logreg = LogisticRegression()
            logreg.fit(x_train, y_train)

            # x_pred = logreg.fit(x_train, y_train).predict(x_test)
            # print(x_pred)

            print(f"テストスコア: {round(logreg.score(x_test, y_test)*100)}%\n")

        # Config Folder not found.
        else:
            raise ValueError("None, Please Check the Config Folder")

    # TraceBack.
    except Exception:
        # Load/Create LogFile.
        except_folder: Optional[str] = 'SKL_Folder_load'
        except_file: Optional[str] = 'SKL_File_load'
        skl_straight: Optional[str] = os.path.expanduser(config[except_folder])
        debug_word: Optional[str] = os.path.expanduser(config[except_file])

        # Load the dictionary.
        if os.path.isdir(skl_straight):
            with open(debug_word, 'a') as log_py:
                traceback.print_exc(file=log_py)

                # throw except.
                raise RuntimeError from None

        # skl_straight Foler not found.
        else:
            raise ValueError("None, Please Check the skl_straight Folder.")

        # Custom Exception.
    except ValueError as ext:
        print(ext)
        raise RuntimeError from None

    # Once Exec.
    finally:
        # GC collection.
        gc.collect()


# Thread call, list.
class skl_straight(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def start(self):
        main()

    def develop(self):
        dev_main()


Thread = skl_straight()

# main thread
start = Thread.start()

# develop thread
# dev_start = Thread.develop()
