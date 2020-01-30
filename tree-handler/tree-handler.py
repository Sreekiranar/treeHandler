import os
from MakeTreeDir import MAKETREEDIR

class treeHandler:
	'''	OS wrapper to grab files from a tree structured folders, process
	them with your algorithm and save the output retaining the same input structure'''
	def __init__(self):
		pass

	def getFiles(self,folderPath,formatList=[],caseSensitive=False):
		"""Function to get the list of filepaths present in the tree structured folder given
		   You can also specify the formats required by providing a list in formatList

		Args:
			folderPath (str):Input folder path
			formatList (list):list of extensions of files of interest (eg: ['jpg','pdf'])
			caseSensitive (boolean): if the extensions given have to be case sensitive or not (False by default)
		Returns:
			list: List of all the paths of files in the given folder

		Examples
			If you want to get all the images('.jpg','.png') from all the subdirectories
			of "mainFolder"
			>>> from tree-handler import treeHandler
			>>> th=treeHandler()
			>>> imageList=th.getFiles('mainFolder',['jpg','png'],caseSensitive=False)


		"""
		listFiles=[]
		for root, dirs, files in os.walk(folderPath):
		    for fil in files:
		        listFiles.append(os.path.join(root,fil))

		for format in formatList:
			if not caseSensitive:
				listFiles=list(filter(lambda x:x.lower().endswith(format.lower())))
			else:
				listFiles=list(filter(lambda x:x.endswith(format))

		return listFiles
