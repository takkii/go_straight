import os
import re
import traceback
from os.path import expanduser

import pandas as pd
from deoplete.source.base import Base

# ------------------------------- KEYWORD -------------------------------------------------------------------------


home = expanduser("~")

d1 = os.path.expanduser("~/.config/nvim/.cache/dein/repos/github.com/takkii/ruby-dictionary3/")
d2 = os.path.expanduser("~/.config/nvim/repos/github.com/takkii/ruby-dictionary3/")
d3 = os.path.expanduser("~/.cache/dein/repos/github.com/takkii/ruby-dictionary3/")

if os.path.exists(d1):
    ruby_method = open(os.path.expanduser(
        "~/.config/nvim/.cache/dein/repos/github.com/takkii/ruby-dictionary3/autoload/source/ruby_method_deoplete"))
    rubymotion_method = open(os.path.expanduser(
        "~/.config/nvim/.cache/dein/repos/github.com/takkii/ruby-dictionary3/autoload/source/rubymotion_method"))
elif os.path.exists(d2):
    ruby_method = open(os.path.expanduser(
        "~/.config/nvim/repos/github.com/takkii/ruby-dictionary3/autoload/source/ruby_method_deoplete"))
    rubymotion_method = open(
        os.path.expanduser("~/.config/nvim/repos/github.com/takkii/ruby-dictionary3/autoload/source/rubymotion_method"))
elif os.path.exists(d3):
    ruby_method = open(os.path.expanduser(
        "~/.cache/dein/repos/github.com/takkii/ruby-dictionary3/autoload/source/ruby_method_deoplete"))
    rubymotion_method = open(
        os.path.expanduser("~/.cache/dein/repos/github.com/takkii/ruby-dictionary3/autoload/source/rubymotion_method"))
else:
    print("Don't forget, Install dein plugin manager github repo takkii/ruby-dictionary3.")

index_ruby = list(ruby_method.readlines()) + list(rubymotion_method.readlines())
Seri = pd.Series(index_ruby)
sort_ruby = Seri.sort_index()
data_ruby = list(map(lambda s: s.rstrip(), sort_ruby))
ruby_method.close()
rubymotion_method.close()


# ------------------------------- KEYWORD -------------------------------------------------------------------------

class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'go_straight'
        self.filetypes = ['ruby']
        self.mark = '[Go_Straight!]'
        rubymatch = [r'\.[a-zA-Z0-9_?!]*|[a-zA-Z]\w*::\w*']
        regexmatch = [r'[<a-zA-Z(?: .+?)?>.*?<\/a-zA-Z>]']
        self.input_pattern = '|'.join(rubymatch + regexmatch)
        self.rank = 500

    def get_complete_position(self, context):
        m = re.search('[a-zA-Z0-9_?!]*$', context['input'])
        return m.start() if m else -1

    def gather_candidates(self, context):
        try:
            dic = data_ruby
            dic_sort = sorted(dic, key=lambda dic: dic[0])
            return dic_sort
        except Exception:
            traceback.print_exc()
