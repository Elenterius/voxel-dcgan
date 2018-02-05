import tensorflow as tf
import numpy as np
import util
import config
from model import *

def interp(l, r, n_samples):
    return np.array([
        l + step_i / (n_samples - 1) * (r - l)
        for step_i in range(n_samples)])

def make_latent_manifold(corners, n_samples):
    left = interp(corners[0], corners[1], n_samples)
    right = interp(corners[2], corners[3], n_samples)

    embedding = []
    for row_i in range(n_samples):
        embedding.append(interp(left[row_i], right[row_i], n_samples))
    return np.vstack(embedding)

netG = Generator()

z = tf.placeholder(tf.float32, [config.batch_size, config.nz])
train = tf.placeholder(tf.bool)

x = netG(z, train, config.nsf, config.nvx)

t_vars = tf.trainable_variables()
varsG = [var for var in t_vars if var.name.startswith('G')]

saver = tf.train.Saver(varsG + tf.moving_average_variables())

config_proto = tf.ConfigProto()
config_proto.gpu_options.allow_growth = True

with tf.Session(config=config_proto) as sess:
    saver.restore(sess, config.params_path)
    batch_z = np.random.uniform(-1, 1, [4, config.nz]).astype(np.float32)
    batch_z = make_latent_manifold(batch_z, 6)
    batch_z = batch_z[:config.batch_size,:]
    x_g = sess.run(x, feed_dict={z:batch_z, train:False})
    for i, data in enumerate(x_g):
        util.save_binvox("out/{0}.binvox".format(i), data[:, :, :, 0] > 0.9)
