import csv
import gc
import multiprocessing
import os
import re
import random
import yaml
import traceback
from operator import itemgetter

import dask.dataframe as dd
import pandas as pd
from deoplete.source.base import Base


# GitHub: config version is v1.3.3
class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'go_straight'
        self.filetypes = ['ruby']
        mark_synbol = [
            '[Ghost]', '[go_straight]', '[GST]', '[まっすぐ]', '[ゴースト]',
            '[Go Straight]', '[直進]', 'GOST', 'go_straight', 'GST', 'Ghost',
            'Go Straight', 'Go_Straight'
        ]
        self.mark = str(random.choice(mark_synbol))
        ruby_match = [r'\.[a-zA-Z0-9_?!]*|[a-zA-Z]\w*::\w*']
        slash_no_match = [r'[;/[^¥/]\*/]']
        self.input_pattern = '|'.join(ruby_match + slash_no_match)
        self.rank = 500

    def get_complete_position(self, context):
        m = re.search('[a-zA-Z0-9_?!]*$', context['input'])
        return m.start() if m else -1

    def gather_candidates(self, context):
        try:
            # use dein plugin manager.
            d1 = os.path.expanduser(
                "~/.vim/.cache/dein/repos/github.com/takkii/config/dict/")
            d2 = os.path.expanduser(
                "~/.vim/repos/github.com/takkii/config/dict/")
            d3 = os.path.expanduser(
                "~/.cache/dein/repos/github.com/takkii/config/dict/")
            d4 = os.path.expanduser(
                "~/.config/nvim/.cache/dein/repos/github.com/takkii/config/dict/"
            )
            d5 = os.path.expanduser(
                "~/.config/nvim/repos/github.com/takkii/config/dict/")

            # use vim-plug plugin manager.
            v1 = os.path.expanduser("~/.vim/plugged/takkii/config/dict/")
            v2 = os.path.expanduser("~/.neovim/plugged/takkii/config/dict/")

            # Manually set the dictionary.
            with open(os.path.expanduser("~/config/load.yml")) as yml:
                config = yaml.safe_load(yml)
            a1 = os.path.expanduser(config['Folder_Load'])

            # dein plugin manager path.
            if os.path.isdir(a1):
                ruby_method = open(os.path.expanduser(
                    config['File_Load']))
            elif os.path.isdir(d1):
                ruby_method = open(
                    os.path.expanduser(
                        "~/.vim/.cache/dein/repos/github.com/takkii/config/dict/ruby_dict.csv"
                    ))
            elif os.path.isdir(d2):
                ruby_method = open(
                    os.path.expanduser(
                        "~/.vim/repos/github.com/takkii/config/dict/ruby_dict.csv"
                    ))
            elif os.path.isdir(d3):
                ruby_method = open(
                    os.path.expanduser(
                        "~/.cache/dein/repos/github.com/takkii/config/dict/ruby_dict.csv"
                    ))
            elif os.path.isdir(d4):
                ruby_method = open(
                    os.path.expanduser(
                        "~/.config/nvim/.cache/dein/repos/github.com/takkii/config/dict/ruby_dict.csv"
                    ))
            elif os.path.isdir(d5):
                ruby_method = open(
                    os.path.expanduser(
                        "~/.config/nvim/repos/github.com/takkii/config/dict/ruby_dict.csv"
                    ))

            # vim-plug plugin manager path.
            elif os.path.isdir(v1):
                ruby_method = open(
                    os.path.expanduser(
                        "~/.vim/plugged/takkii/config/dict/ruby_dict.csv"))
            elif os.path.isdir(v2):
                ruby_method = open(
                    os.path.expanduser(
                        "~/.neovim/plugged/takkii/config/dict/ruby_dict.csv"))

            # Automatically search the dictionary not found.
            else:
                print("Please, Check the path of go_straight.")

            # pandas and dask
            index_ruby = list(ruby_method.readlines())
            pd_ruby = pd.Series(index_ruby)
            sort_ruby = pd_ruby.sort_index()
            ddf = dd.from_pandas(data=sort_ruby,
                                 npartitions=multiprocessing.cpu_count())
            data_array = ddf.to_dask_array(lengths=True)
            data = data_array.compute()
            data_ruby = list(map(lambda s: s.rstrip(), data))
            ruby_method.close()

            # sort and itemgetter
            dic = data_ruby
            dic.sort(key=itemgetter(0))
            return dic

        except Exception:
            traceback.print_exc()
        except OSError as e:
            print(e)
        except ZeroDivisionError as zero_e:
            print(zero_e)
        except TypeError as type_e:
            print(type_e)
        except FileNotFoundError as file_not:
            print(file_not)
        finally:
            gc.enable()
