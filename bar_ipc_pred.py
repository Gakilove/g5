#!/usr/bin/env python2.7

import os
import time
import re
import argparse
import sys
import numpy as np

from extract import extract_stat
from specify import specify_stat
from check_ready import get_rand_list
from paths import *

def cat(x, y):
    return os.path.join(os.path.expanduser(x), y)


possible_dirs = [
    # part all:
    #'~/dyn_part_all2',
    #'~/dyn_bpp2',
    #'~/dyn_64_lsq_hard',
    '~/dyn_64_lsq_special3',

    # share tlb:
    #'~/dyn_share_tlb',
    #'~/dyn_share_tlb2',

    # share bp:
    #'~/dyn_share_bp',
]

#pairs = './hard.txt'
pairs = './rand.txt'

#file_name = './stat/pred_ipc_error_share_tlb.txt'
#file_name = './stat/pred_ipc_error_share_bp.txt'
#file_name = './stat/pred_ipc_error_part_all.txt'
#file_name = './stat/pred_ipc_error_part_all_64_lsq.txt'
file_name = './stat/pred_ipc_error_part_all_64_spec3.txt'

def gen_stat_path(p, hpt, lpt):
    return cat(cat(p, hpt+'_'+lpt), 'stats.txt')

result = []

for line in get_rand_list(pairs):
    error_overall = []
    error = 10000
    hpt, lpt = line
    for pd in possible_dirs:
        if os.path.isfile(gen_stat_path(pd, hpt, lpt)):
            try:
                pred_ipc = specify_stat(gen_stat_path(pd, hpt, lpt),
                                        False, 'system.cpu.HPTpredIPC::0')
            except:
                print 'Unexpected error:', sys.exc_info()
                pred_ipc = specify_stat(gen_stat_path(pd, hpt, lpt),
                                        True, 'system.cpu.HPTpredIPC::0')
            st_ipc = specify_stat(cat(cat(st_stat_dir(),
                                          hpt + '_perlbench'),
                                        'stats.txt'),
                                    False, 'system.cpu.ipc::0')
            error = (float(pred_ipc) - float(st_ipc))/float(st_ipc)
        else:
            print gen_stat_path(pd, hpt, lpt), 'is not file'

    error_overall.append(error)
    line.append(str(error))
    result.append(line)

# print 'avg:', np.mean(error_overall, axis=0), 'std:', np.std(error_overall, axis=0)
print result

with open(file_name, 'w') as f:
    for line in result:
        f.write(', '.join([x for x in line]) + '\n')
print 'saved from {} to {}'.format(possible_dirs[0], file_name)
