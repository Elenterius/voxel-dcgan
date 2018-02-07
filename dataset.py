import numpy as np
import glob
import os
import util
import config

class Dataset:

    def __init__(self, path_i, path_o):
        self.index_in_epoch = 0
        self.examples_i = np.array(glob.glob(path_i))
        self.examples_o = np.array(glob.glob(path_o))
        self.num_examples = len(self.examples_i)
        seed = np.random.randint(300)
        np.random.seed(seed)
        np.random.shuffle(self.examples_i)
        np.random.seed(seed)
        np.random.shuffle(self.examples_o)
        print "dataset path for input:", path_i
        print "dataset path for target:", path_o
        print "number of examples:", self.num_examples

    def next_batch(self, batch_size):
        start = self.index_in_epoch
        self.index_in_epoch += batch_size

        if self.index_in_epoch > self.num_examples_i:
            seed = np.random.randint(300)
            np.random.seed(seed)
            np.random.shuffle(self.examples_i)
            np.random.seed(seed)
            np.random.shuffle(self.examples_o)
            start = 0
            self.index_in_epoch = batch_size
            assert batch_size <= self.num_examples

        end = self.index_in_epoch
        return self.read_data(start, end)

    def read_data(self, start, end):
        data_i = []
        data_o = []
        for fname in self.examples_i[start:end]:
            data.append(util.read_binvox(fname))
        return np.array(data_i), np.array(data_o)
