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
images('.jpg','.png') from the folder, use
```python
from treeHandler import treeHandler
th=treeHandler()
imageList=th.getFiles('inputFolder',['jpg','png'])

### If you need all files
th.getFiles('inputFolder')

### If you need case sensitive (only lowercase 'jpg')
th.getFiles('inputFolder',['jpg'],caseSensitive=True)
```
The output will be obtained instantly.
## Authors

* **Sreekiran A R** - *Analytics Consultant, AI Labs, Bridgei2i Analytics Solutions* -
 [Github](https://github.com/Sreekiranar) ,
[Stackoverflow](https://stackoverflow.com/users/9605907/sreekiran)

* **Anil Prasad M N** - *Project Manager, AI Labs, Bridgei2i Analytics Solutions* -
 [Github](https://github.com/anilprasadmn)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
