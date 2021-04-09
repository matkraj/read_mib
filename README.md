# Read MIB files to numpy

Python library to read Quantum Detectors Merlin MIB files to numpy with predifined geometry.
The file is loaded as memmap. Dataset properties are loaded directly from the MIB header (*.hdr files are not used).

Example usage:
```
import numpy as np
import mib

path = './example.mib'
data = mib.loadMib(path,scan_size=(2,1))

print("\nMerlin file shape:",data.shape)
```
> Merlin file shape: (2, 1, 256, 256)

Note: RAW datasets are not supported.
