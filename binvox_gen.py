import glob
import os
import subprocess
import sys

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
