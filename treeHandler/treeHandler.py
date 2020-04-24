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
			dict: Dictionary with all the file names as key and their folder path as value

		Examples
			If you want to get all the images('.jpg','.png') from all the subdirectories
			of "mainFolder"
			>>> from treeHandler import treeHandler
			>>> th=treeHandler()
			>>> fileDict=th.getFiles('mainFolder',['jpg','png'],caseSensitive=False)

		"""
		listFiles=[]
		listPaths=[]
		try:
			for root, dirs, files in os.walk(folderPath):
				for fil in files:
					listFiles.append(fil)
					listPaths.append(root)

			fileDict=dict(zip(listFiles,listPaths))
			for frmt in formatList:
				if caseSensitive:
					fileDict = {k:v for (k,v) in outDict.items() if k.endswith(frmt)}
				else:
					fileDict={k:v for (k,v) in outDict.items() if k.lower().endswith(frmt.lower())}
		except Exception as e:
			print(e)

		return fileDict
