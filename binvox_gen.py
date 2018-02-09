import glob
import os
import subprocess
import sys
'''
voxsize = 32
paths = glob.glob("/media/wangyida/D0-P1/database/ShapeNetCore.v2/*/*/*/*.obj")
print("number of data:", len(paths))

with open(os.devnull, 'w') as devnull:
    for i, path in enumerate(paths):
        cmd = "binvox -d {0} -cb -e {1}".format(voxsize, path)
        ret = subprocess.check_call(cmd.split(' '), stdout=devnull, stderr=devnull)
        if ret != 0:
            print("error", i, path)
        else:
            print(i, path)
'''
paths = glob.glob("/media/wangyida/D0-P1/database/ShapeNetCore.v2/*/*/*/model_normalized.binvox")
print("number of data:", len(paths))

with open(os.devnull, 'w') as devnull:
    for i, path in enumerate(paths):
        cmd1 = "thinvox {0}".format(path)
        ret1 = subprocess.check_call(cmd1.split(' '), stdout=devnull, stderr=devnull)
        cmd2 = "mv thinned.binvox {0}".format(path+'.thinned')
        ret2 = subprocess.check_call(cmd2.split(' '), stdout=devnull, stderr=devnull)
        if ret1 != 0 or ret2 != 0:
            print("error", i, path)
        else:
            print(i, path)
