# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 07:31:01 2018

@author: emily
"""

import pipeline
import numpy as np


def LoadObservations():

    rf_obs = pipeline.RecvFunc(amp = np.array([0.073, 0.125, 0.102, 0.022,
                       -0.027, -0.015, 0.013, 0.011, -0.004, 0.004, 0.032, 0.037,
                       0.003, -0.037, -0.048, -0.020, 0.033, 0.080, 0.089, 0.056,
                       0.012, -0.016, -0.014, 0.003, 0.013, 0.006, -0.003, -0.003,
                       -0.000, -0.001, -0.004, -0.001, 0.007, 0.009, -0.003, -0.021,
                       -0.031, -0.027, -0.014, -0.001, 0.010, 0.018, 0.014, -0.002,
                       -0.017, -0.023, -0.024, -0.021, -0.011, -0.000, 0.004, 0.002,
                       0.004, 0.012, 0.015, 0.006, -0.004, -0.000, 0.012, 0.018,
                       0.011, -0.004, -0.011, -0.007, 0.002, 0.004, 0.001, -0.001,
                       -0.002, -0.002, -0.003, -0.003, -0.003, -0.005, -0.009, -0.014,
                       -0.017, -0.016, -0.020, -0.029, -0.032, -0.022, -0.004, 0.007,
                       0.006, -0.001, -0.005, -0.007, -0.010, -0.015, -0.012, 0.001,
                       0.014, 0.016, 0.008, -0.002, -0.011, -0.019, -0.017, -0.006,
                       0.006, 0.012, 0.013, 0.013, 0.006, -0.014, -0.033, -0.024,
                       0.009, 0.030, 0.018, -0.005, -0.011, -0.000, 0.003, -0.008,
                       -0.013, -0.002, 0.016, 0.022]), dt = 0.25, ray_param = 0.06147,
                        std_sc = 2)

    swd_obs = pipeline.SurfaceWaveDisp(period = np.array([9.0, 10.1, 11.6, 13.5,
                        16.2, 20.3, 25.0, 32.0, 40.0, 50.0, 60.0, 80.0]),
                        c = np.array([3.212, 3.215, 3.233, 3.288,
                       3.339, 3.388, 3.514, 3.647, 3.715, 3.798, 3.847, 3.937]))

    all_lims = pipeline.Limits(
        vs = (0.5,5.5), dep = (0,200), std_rf = (0,0.05),
        lam_rf = (0.05, 0.5), std_swd = (0,0.15))

    return (rf_obs, swd_obs, all_lims)