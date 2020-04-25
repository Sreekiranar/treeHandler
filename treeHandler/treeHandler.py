import os

class treeHandler:
	'''	OS wrapper to grab files from a tree structured folders, process
	them with your algorithm and save the output retaining the same input structure'''
	def __init__(self):
		pass

	def getFiles(self,folderPath,formatList=[],caseSensitive=False):
		"""Function to get the list of filepaths present in the tree structured folder given.
		   You can also specify the formats required by providing a list in formatList

		Args:
			folderPath (str):Input folder path
			formatList (list):list of extensions of files of interest (eg: ['jpg','pdf'])
			caseSensitive (boolean): if the extensions given have to be case sensitive or not (False by default)
		Returns:
			list: list of tuples with each tuple containing file names and their folder path

		Examples
			If you want to get all the images('.jpg','.png') from all the subdirectories
			of "mainFolder"
			>>> from treeHandler import treeHandler
			>>> th=treeHandler()
			>>> fileTuple=th.getFiles('mainFolder',['jpg','png'],caseSensitive=False)

		"""
		listTuple=[]
		try:
			for root, dirs, files in os.walk(folderPath):
				for fil in files:
					listTuple.append((fil,root))

			for frmt in formatList:
				if caseSensitive:
					listTuple = [(fname,fpath) for (fname,fpath) in listTuple if fname.endswith(frmt)]
				else:
					listTuple = [(fname,fpath) for (fname,fpath) in listTuple if fname.lower().endswith(frmt.lower())]
		except Exception as e:
			print(e)

		return listTuple
