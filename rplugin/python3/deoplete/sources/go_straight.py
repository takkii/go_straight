import multiprocessing
import os
import re
import traceback
from operator import itemgetter

import dask.dataframe as dd
import pandas as pd
from deoplete.source.base import Base


class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'go_straight'
        self.filetypes = ['ruby']
        self.mark = '[Go_Straight!]'
        rubymatch = [r'\.[a-zA-Z0-9_?!]*|[a-zA-Z]\w*::\w*']
        self.input_pattern = '|'.join(rubymatch)
        self.rank = 500

    def get_complete_position(self, context):
        m = re.search('[a-zA-Z0-9_?!]*$', context['input'])
        return m.start() if m else -1

    def gather_candidates(self, context):
        try:
            d1 = os.path.expanduser("~/.vim/.cache/dein/repos/github.com/takkii/go_straight/dict/")
            d2 = os.path.expanduser("~/.vim/repos/github.com/takkii/go_straight/dict/")
            d3 = os.path.expanduser("~/.cache/dein/repos/github.com/takkii/go_straight/dict/")
            d4 = os.path.expanduser("~/.config/nvim/.cache/dein/repos/github.com/takkii/go_straight/dict/")
            d5 = os.path.expanduser("~/.config/nvim/repos/github.com/takkii/go_straight/dict/")

            if os.path.isdir(d1):
                ruby_method = open(os.path.expanduser(
                    "~/.vim/.cache/dein/repos/github.com/takkii/go_straight/dict/ruby_dict"))
            elif os.path.isdir(d2):
                ruby_method = open(os.path.expanduser(
                    "~/.vim/repos/github.com/takkii/go_straight/dict/ruby_dict"))
            elif os.path.isdir(d3):
                ruby_method = open(os.path.expanduser(
                    "~/.cache/dein/repos/github.com/takkii/go_straight/dict/ruby_dict"))
            elif os.path.isdir(d4):
                ruby_method = open(os.path.expanduser(
                    "~/.config/nvim/.cache/dein/repos/github.com/takkii/go_straight/dict/ruby_dict"))
            elif os.path.isdir(d5):
                ruby_method = open(os.path.expanduser(
                    "~/.config/nvim/repos/github.com/takkii/go_straight/dict/ruby_dict"))
            else:
                print("Please, Check the path of go_straight.")

            # pandas and dask
            index_ruby = list(ruby_method.readlines())
            Seri = pd.Series(index_ruby)
            sort_ruby = Seri.sort_index()
            ddf = dd.from_pandas(data=sort_ruby, npartitions=multiprocessing.cpu_count())
            data_array = ddf.to_dask_array(lengths=True)
            data = data_array.compute()
            data_ruby = list(map(lambda s: s.rstrip(), data))
            ruby_method.close()

            # sorted
            dic = data_ruby
            dic_sort = sorted(dic, key=itemgetter(0))
            return dic_sort

        except Exception:
            traceback.print_exc()
