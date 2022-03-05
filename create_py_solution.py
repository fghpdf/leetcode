#!/usr/bin/python3

import sys
import os

# Detect Squares -> detect_squares
folderName = ''.join([arg.lower()+"_" for arg in sys.argv[1:]])[:-1]

folderPath = os.path.join('./py', folderName)
if not os.path.exists(folderPath):
  os.mkdir(folderPath)

filePath = os.path.join('./py', folderName, folderName+'.py')
if not os.path.exists(filePath):
  with open(filePath, 'w'): pass