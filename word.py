''' Word runs multiple analytics on any number of files and outputs the results in a pretty table format '''

from collections import Counter
from exceptions import *
import re
import sys
import os

class FileParser(object):

	def __init__(self, writeto):
		if not os.path.isfile(writeto):
			raise FileNotFoundException()

		self._output = writeto
		self._error_msg = None
		self.files = []
		self.size = len(self.files)

	def add_item(self, file):
		if os.path.isfile(file):
			self.files.append(file)

	def parse(self):
		for file in self.files:		
			if os.path.isfile(file):
				try:
					word_count = 0
					line_count = 0
					words = []
					with open(file, 'r') as f:
						lines = f.readlines()
						for line in lines:
							words += line.split()
							word_count += len(words)
							line_count += 1
					with open(str(self._output), 'w') as out:
						frequent_wrds = []
						for tple in frequent(words, 5):
							print tple
							frequent_wrds.append(tple[0])
						frequent_wrds = ' '.join(frequent_wrds)
						print frequent_wrds

						out.write('File name: {0} \n'.format(file))
						out.write('Word count: {0} \n'.format(word_count))
						out.write('Line count: {0} \n'.format(line_count))
						out.write('Most Frequent: {0}\n'.format(frequent_wrds))

						#f.write('Frequent words: %s') % (file.frequent)
				except Exception as ex:
					print str(ex)

def frequent(words, count=5):
	c = Counter(words)
	return c.most_common(count)


def main():
	if sys.argv < 2:
		raise UsageException()

	fileparser = FileParser(sys.argv[-1])
	print 'output', sys.argv[-1]

	for temp in sys.argv[1:-1]:
		print temp
		if os.path.isfile(temp):
			fileparser.add_item(temp)
	fileparser.parse()

if __name__ == '__main__':
	main()