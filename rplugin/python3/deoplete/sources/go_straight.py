import dask.dataframe as dd
import gc
import multiprocessing
import os
import pandas as pd
import random
import re
import sys
import yaml
import traceback
import warnings

from deoplete.source.base import Base
from operator import itemgetter
from typing import Optional

warnings.filterwarnings('ignore')


# GitHub: use config repo.
class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'go_straight'
        self.filetypes = ['ruby']
        mark_synbol = [
            '[GST]',  '[Go Straight]', 'go straight', 'GST',
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
            # It doesn't support python4 yet.
            py_major = sys.version_info[0]
            py_minor = sys.version_info[1]

            # 3.5 or higher python version is required.
            if py_major == 3 and py_minor > 4:
                # Settings, Config path is true/false change.
                config_load: Optional[str] = '~/config/load.yml'
                plug_config: Optional[
                    str] = '~/.neovim/plugged/config/load.yml'

                # Settings, Loading File PATH.
                file_load: Optional[str] = 'Home_File'
                plug_load: Optional[str] = 'File_Load'

                # Home Folder, Set the dictionary.
                if os.path.exists(os.path.expanduser(config_load)):
                    with open(os.path.expanduser(config_load)) as yml:
                        config = yaml.safe_load(yml)

                    # Get Receiver/Ruby Method Complete.
                    with open(os.path.expanduser(config[file_load])) as r_meth:
                        data: Optional[list] = list(r_meth.readlines())
                        data_ruby: Optional[list] = [s.rstrip() for s in data]
                        complete: Optional[list] = data_ruby
                        complete.sort(key=itemgetter(0))
                        return complete

                # Use vim-plug, Set the dictionary.
                elif os.path.exists(os.path.expanduser(plug_config)):
                    with open(os.path.expanduser(plug_config)) as yml:
                        config = yaml.safe_load(yml)

                    # Get Receiver/Ruby Method Complete.
                    with open(os.path.expanduser(config[plug_load])) as r_meth:
                        # pandas and dask
                        index_ruby: Optional[list] = list(r_meth.readlines())
                        pd_ruby = pd.Series(index_ruby)
                        st_r = pd_ruby.sort_index()
                        ddf = dd.from_pandas(
                            data=st_r, npartitions=multiprocessing.cpu_count())
                        data_array = ddf.to_dask_array(lengths=True)
                        data = data_array.compute()
                        data_py: Optional[list] = [s.rstrip() for s in data]

                        # sort and itemgetter
                        data_py.sort(key=itemgetter(0))
                        return data_py

                # Config Folder not found.
                else:
                    raise ValueError("None, Please Check the Config Folder")
            else:
                raise ValueError("Python Version Check, 3.5 or higher.")

        # TraceBack.
        except Exception:
            # Load/Create LogFile.
            except_folder: Optional[str] = 'SKL_Folder_load'
            except_file: Optional[str] = 'SKL_File_load'
            skl_str: Optional[str] = os.path.expanduser(config[except_folder])
            debug_word: Optional[str] = os.path.expanduser(config[except_file])

            # Load the dictionary.
            if os.path.isdir(skl_str):
                with open(debug_word, 'a') as log_py:
                    traceback.print_exc(file=log_py)

                    # throw except.
                    raise RuntimeError from None

            # skl_straight Foler not found.
            else:
                raise ValueError("None, Please Check the go_straight Folder.")

        # Custom Exception.
        except ValueError as ext:
            print(ext)
            raise RuntimeError from None

        # Once Exec.
        finally:
            # GC collection.
            gc.collect()
