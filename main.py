import numpy as np
import mib

#example usage of Merlin mib.py library to read MIB data from file and buffer

path = './example.mib'
data = mib.loadMib(path,scan_size=(2,1))

with open(path,'rb') as f:
    buffer_mib = f.read()

data_from_buffer = mib.loadMib(buffer_mib,scan_size=(2,1))

print("\nNumpy array from file shape:",data.shape)
print("Numpy array from buffer shape:",data_from_buffer.shape)
