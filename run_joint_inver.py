# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 14:23:28 2018

@author: emily
"""

import pipeline
import os
import input_data
import pstats
import cProfile
import shutil

import tensorflow as tf

#pr = cProfile.Profile()
#pr.enable()


#def try_running():
max_it=500
rnd_sd = 10

save_name = 'MBEY_Psz'
rf_obs, swd_obs, all_lims = input_data.LoadObservations()

save_name += '_%d' % rnd_sd
suffix = None
def outdir_fn():
    if suffix is None:
        return os.path.join('output', save_name)
    else:
        return os.path.join('output', '%s_%05d' % (save_name, suffix))

while os.path.exists(outdir_fn()):
    if suffix is None:
        suffix = 0
    else:
        suffix += 1

outdir = outdir_fn()

os.mkdir(outdir)
shutil.copyfile('input_data.py', os.path.join(outdir, 'input_data.py'))
with tf.Session():
    out = pipeline.JointInversion(rf_obs, swd_obs, all_lims, max_it, rnd_sd,
                                  os.path.join(outdir, save_name), 'Ps')

#pr.disable()
#s=open(os.path.join(outdir, 'profiletimes.txt'), 'w')
#sortby = 'cumulative'
#ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
#ps.print_stats()
#s.close()
