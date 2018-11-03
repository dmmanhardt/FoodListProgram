# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 16:21:36 2018

@author: MANHARDTD
"""

import datetime

# outputs contents of grocery_df as text file with current date in title
# to current working directory

# what to do if there is already a file with same name? currently
# overrides old file

def output_grocery_list(grocery_df):
    # find date to add to name of text file
    directory = os.getcwd()
    current_date = datetime.datetime.today().strftime("%Y-%m-%d")
    filename = ("Grocery List %(date)s.txt" % {"date":current_date})
    save_file = os.path.join(directory, filename)
    np.savetxt(save_file, grocery_df.values, fmt = "%s")