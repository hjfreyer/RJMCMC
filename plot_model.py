import tensorflow as tf
import numpy as np

import pipeline

import matplotlib as mpl
mpl.use('agg')
import matplotlib.pyplot as plt

saveable_model = pipeline.NewSaveableModel(129)
loader = tf.train.Saver()

with tf.Session() as sess:
    fiel = tf.train.latest_checkpoint('/tmp/')
    print(fiel)
    loader.restore(sess, fiel)
    vs = saveable_model.vs.eval()
    deps = saveable_model.deps.eval()



rnd_sd = 10


deps = np.concatenate((np.arange(0,10,0.2), np.arange(10,60,1), np.arange(60,201,5)))
model = pipeline.Model(vs = np.array([3.4, 4.5]), all_deps = deps,
                       idep = np.array([60, 80]),
                       std_rf = 0, lam_rf = 0, std_swd = 0)

rf_obs = pipeline.SynthesiseRF(pipeline.MakeFullModel(model))
swd_obs = pipeline.SynthesiseSWD(pipeline.MakeFullModel(model), 1/np.arange(0.02,0.1, 0.01))
all_lims = pipeline.Limits(
        vs = (0.5,5.5), dep = (0,200), std_rf = (0,0.05),
        lam_rf = (0.05, 0.5), std_swd = (0,0.15))

actual_model = pipeline.SaveModel(pipeline.MakeFullModel(model),deps)

fig = plt.figure(); plt.title("Suite of Velocity models")
plt.gca().invert_yaxis()
plt.plot(actual_model,deps,'r-',linewidth=3)
plt.plot(vs,deps,'c-',linewidth=1)
fig.savefig('plot.png')

plt.figure(); plt.title('Receiver Function - real: red; synth: grey')
rft = np.arange(0,rf_obs.dt*rf_obs.amp.size,rf_obs.dt)
plt.plot(rft, rf_obs.amp, 'r-', linewidth=2)
synth_rf = pipeline.SynthesiseRF(out[5])
plt.plot(rft,synth_rf.amp, '-',color = '0.25', linewidth=1)
