#! python
#coding=utf-8
import sys
from caffe import Net
caffe_root = your/caffe/root
sys.path.insert(0, caffe_root + 'python')

n_orig = Net('orig_model.prototxt', 'orig_model.caffemodel', 0)
n_new = Net('new_model.prototxt', 'orig_model.caffemodel', 0)
for orig_name in n_orig.params:
    #n_new.params[orig_name + '_p'] = n_orig.params[orig_name]
    n_new.params[new_name] = n_orig.params[orig_name]
n_new.save('new_model.caffemodel')
