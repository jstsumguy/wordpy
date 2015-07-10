''' Word runs multiple analytics on any number of files and outputs the results in a pretty table format '''

from collections import Counter
import re
import sys
import os

''' Exceptions '''
class UsageException(Exception):
	pass

class FileNotFoundException(Exception):
	pass


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
						spec = FileSpec(file)
						lines = f.readlines()
						for line in lines:
							words = line.split()
							word_count += len(words)
							line_count += 1
					with open(str(self._output), 'w') as out:
						out.write('File name: {0} \n'.format(file))
						out.write('Word count: {0} \n'.format(word_count))
						out.write('Line count: {0} \n'.format(line_count))

						#f.write('Frequent words: %s') % (file.frequent)
				except Exception as ex:
					print str(ex)

class FileSpec(object):

	def __init__(self, file):
		self._file = file
		self.word_count = 0
		self.line_count = 0
		self.words = []

	def __str__(self):
		return 'File {0}, word-count {1}, line-count {2}'.format(self._file, self.word_count, self.line_count)

	def frequent(self, words=5):
		# todo get most frequent words
		pass


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