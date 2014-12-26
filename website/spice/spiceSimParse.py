from subprocess import call
from sys import argv 
from spiceToCSV import *

call(["ngspice", "-b", argv[1], "-o", argv[1].rsplit('.')[0]+'.out'])
parse_spice(fileName=argv[1].rsplit('.')[0]+'.out')
