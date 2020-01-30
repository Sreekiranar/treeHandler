from setuptools import setup

with open('README.md','r') as f:
    long_description = f.read()


setup(name='tree-handler',
      version='1.0',
      description='Python OS wrapper to grab all/specific files from all the subdirectories',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='',
      authors='Sreekiran A R`',
      author_email='sreekiranar@gmail.com',
      license='MIT',
      packages=['tree-handler'],
      install_requires=['MakeTreeDir'], include_package_data=True,
      zip_safe=False)