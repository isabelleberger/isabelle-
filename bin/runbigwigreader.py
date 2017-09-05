from bx.intervals.io import GenomicIntervalReader
from bx.bbi.bigwig_file import BigWigFile
import numpy as np

bw = BigWigFile(open('dm6.27way.phastCons.bw'))
mySummary = bw.query("chr1", 10000, 10500, 1)
myInterval = bw.get("chr1", 10000, 10500)
myArrayInterval = bw.get_as_array("chr1", 10000, 10500)

print mySummary
print myInterval

