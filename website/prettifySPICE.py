# Brady Salz
# Prettify for SPICE
# Because Google hates hardware and me
# 12/25/15

# Valid Output Comments:
#	code-spice-comment  ( * <any> )
# 	code-spice-variable ( first word of net )
#	code-spice-command  ( .any, analysis )
# 	code-spice-keyword  ( any other keyword )

def addComment(spiceLine):
	startComment = '<span class="code-spice-comment">'
	endComment = '</span>'
	return startComment + ''.join(spiceLine) + endComment

def addLine(spiceLine):
	startCom = '<span class="code-spice-command">'
	startKey = '<span class="code-spice-keyword">'
	startVar = '<span class="code-spice-variable">'
	endTag = '</span>'
	
	spiceLine = spiceLine.split(' ')
	if '.' in spiceLine[0]:
		outStr = startCom + spiceLine[0] + ' ' + endTag
	else:
		outStr = startVar + spiceLine[0] + ' ' + endTag
	
	for word in spiceLine[1:]:
		validSims = ['tran', 'ac', 'dc', 'disto', 'noise', 'op',
						'pz', 'sense', 'tf', 'pss', 'pulse', 'trrandom'
						'trnoise', 'am', 'sffm', 'pwl', 'exp','sin']

		if '(' in word and ')' in word:
			# break word into v->rest of word
			words = word.split('(')
			outStr += startKey + words[0] + endTag
			outStr += '(' + ''.join(words[1:]) + ' '


		elif word.lower() in validSims:
			outStr += startCom + word + ' ' + endTag

		else:
			outStr += word + ' '

	return outStr 


def prettifySPICE(spiceFile):
	outputHTML = ''

	for line in open(spiceFile, 'r').readlines():

		line = line.strip(' ').strip('\n')

		if '*' in line:
			print 'Adding comment'
			outputHTML += addComment(line)

		else:
			outputHTML += addLine(line)

		outputHTML += '<br>'
	return outputHTML
