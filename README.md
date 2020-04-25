# tree-handler

OS wrapper to grab specific/all files from all the subdirectories of the given folder, process
them with your algorithm and save the output retaining the same input structure


### Installation

You can easily install the package using

`pip install treeHandler`

### Usage
This package will help you to find all/specific files from the subdirectories of a given directory.
Thus you can process these files and save them retaining the complex tree structure.

eg:
If you have a complex tree structured folder and you need to get all the
files from the folder, use
```python
from treeHandler import treeHandler
th=treeHandler()
fileTuple=th.getFiles('inputFolder')
### fileTuple is a list of tuples with each tuple containing file names and their folder path
### eg: [('image11.jpg', 'sampleData/folder1'),('image21.jpg', 'sampleData/folder2')]

### If you need to filter specific file extensions eg: .jpg,.png
th.getFiles('inputFolder',['jpg','png'])

### If you need case sensitive (only lowercase 'jpg')
th.getFiles('inputFolder',['jpg'],caseSensitive=True)
```
The output will be obtained instantly.
## Authors

* **Sreekiran A R** - *Senior Analytics Consultant, AI Labs, Bridgei2i Analytics Solutions* -
 [Github](https://github.com/Sreekiranar) ,
[Stackoverflow](https://stackoverflow.com/users/9605907/sreekiran)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
