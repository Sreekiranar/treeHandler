import os

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
			tuple: (List of all folders containing files, List of all the paths of files in the given folder)

		Examples
			If you want to get all the images('.jpg','.png') from all the subdirectories
			of "mainFolder"
			>>> from treeHandler import treeHandler
			>>> th=treeHandler()
			>>> imageList=th.getFiles('mainFolder',['jpg','png'],caseSensitive=False)


		"""
		listFiles=[]
		listFolders=[]
		try:
			for root, dirs, files in os.walk(folderPath):
			    for fil in files:
			        listFiles.append(os.path.join(root,fil))

			for frmt in formatList:
				if caseSensitive:
					listFiles=list(filter(lambda x:x.endswith(frmt),listFiles))
				else:
					listFiles=list(filter(lambda x:x.lower().endswith(frmt.lower()),listFiles))
			if len(listFiles)>0:
				sep='/' if '/' in listFiles[0] else '\\'
				listFiles=list(map(lambda x:os.path.join(*x.split(sep)[1:]),listFiles))
				listFolders=list(set([findSubFolder(path,sep) for path in listFiles]))

		except Exception as e:
			print(e)

		return listFolders,listFiles

	def findSubFolder(self,path,sep):
	    index = path.rfind(sep)
	    return (path[:index] if index != -1  else '.')
