import csv
import sys
from sys import argv

def find_analysis(dataFile, lineCount=0):
	# locate start of sim block
	# <Type> Analysis <time>
	i = lineCount
	while 'Analysis' not in dataFile[i]:
		i += 1
		if i >= len(dataFile):
			sys.exit('File finished parsing\n')
		
	return i

def parse_time(timeLine):
	# sort timestamp from SPICE to easier to use
	# will convert to datetime object later
	stamp = []
	stamp.append(timeLine[6]) # Time HH:MM
	stamp.append(timeLine[4]) # Mon XXX
	stamp.append(timeLine[5]) # Day XX
	stamp.append(timeLine[8][:-1]) #Year XXXX
	return stamp

def parse_spice(fileName):
	fileNameNoExt = fileName.rsplit('.')[0]


	spiceData = open(fileName).readlines()
	lineCount = 0
	fileCount = 0

	while True:
		lineCount = find_analysis(spiceData, lineCount+1)
		analysis = spiceData[lineCount].lstrip().split(' ')[0]

		timeStamp = parse_time(spiceData[lineCount].lstrip().split(' '))

		print '%s Analysis starts at line %d' % (analysis, lineCount)
		
		if analysis == 'AC':
			idx = 'frequency'

		if analysis == 'Transient':
			idx = 'time'
		
		# continue reading until find header line
		# necessary for when people use .plot or other sim options
		
		while idx not in spiceData[lineCount]:
			lineCount += 1

		cols = spiceData[lineCount].split(' ')
		cols = filter(None, cols)
		print cols
		startCol = cols.index(idx)

		# add two more at end to increment and handle --- line
		lineCount += 2

		outputFile = open(fileNameNoExt+'-'+str(fileCount)+'.csv','wb')

		outCSV = csv.writer(outputFile, delimiter=',')

		invalidWords = set(['*', 'elapsed'])

		while not set(spiceData[lineCount].lstrip().split(' ')).intersection(invalidWords):
			currLine = spiceData[lineCount].lstrip().split('\t')
			currLine = filter(None, currLine)
	
			if len(currLine) <= 1:
				lineCount +=1 
				continue


			if idx in spiceData[lineCount].lstrip().split(' '):
				lineCount += 1
				print 'Skipped line %d due to idx' % lineCount
				continue

			try:
				currLine = map(float, currLine[startCol:-1]) 
			except ValueError:
				currLine = [s.strip(',') for s in currLine]
				currLine = map(float, currLine[startCol:-1]) 

			
			outCSV.writerow(currLine)
			lineCount += 1

		outputFile.close()
		fileCount += 1