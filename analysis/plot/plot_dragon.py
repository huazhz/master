#!/usr/bin/env python
# encoding: utf-8
"""
    plot: regularization on x axis, number of k_best features on y

Created by  on 2012-01-27.
Copyright (c) 2012. All rights reserved.
"""
import sys
import os
import json
import pylab as plt
from master.libs import plot_lib as plib
from master.libs import read_data_lib as rdl
from master.libs import utils
reload(plib)
reload(rdl)

config = json.load(open(sys.argv[1]))
outpath = os.path.join(config['inpath'], 'plots')
methods = ['svr', 'svr_ens', 'forest']

# variables for results
plt.close('all')
search_res, max_overview, sc = rdl.read_paramsearch_results(config['inpath'], methods)

if config['plot_param_space']:
    for desc in search_res:
        fig = plt.figure()
        plib.plot_search_matrix(fig, search_res[desc], sc, methods)
        fig.savefig(os.path.join(outpath, desc + '.' + config['format']))


# feature selection comparison plot
fig = plt.figure()
plib.feature_selection_comparison_plot(fig, max_overview, sc)
fig.savefig(os.path.join(outpath, 'max_overview.' + config['format']))


# descriptor method performance plots
fig = plt.figure(figsize=(15,30))
plib.descriptor_performance_plot(fig, max_overview, search_res, sc)
fig.savefig(os.path.join(outpath, 'desc_compariosn.' + config['format']))
if utils.run_from_ipython():
    plt.show()





