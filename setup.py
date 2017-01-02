
from setuptools import setup, find_packages
from os import walk
from os.path import join, dirname, sep
import os
import glob

packages = find_packages()

package_data = {'nogo': ['*.json',
                         '*.sgf',
                         '*.py'], }

data_files = []

# By specifying every file manually, package_data will be able to
# include them in binary distributions. Note that we have to add
# everything as a 'pythonforandroid' rule, using '' apparently doesn't
# work.
def recursively_include(results, directory, patterns):
    for root, subfolders, files in walk(directory):
        for fn in files:
            if not any([glob.fnmatch.fnmatch(fn, pattern) for pattern in patterns]):
                continue
            filename = join(root, fn)
            directory = 'pythonforandroid'
            if directory not in results:
                results[directory] = []
            results[directory].append(join(*filename.split(sep)[1:]))

recursively_include(package_data, 'noGo', ['*.py'])
recursively_include(package_data, 'noGo/games', ['*.json', '*.sgf'])
recursively_include(package_data, 'noGo/collections', ['*.json'])

import sys
print('argv is', sys.argv)

setup(name='noGo2',
      version='0.5',
      description='SGF editor for Android',
      author='Alexander Taylor',
      author_email='alexanderjohntaylor@gmail.com',
      url='https://github.com/inclement/noGo', 
      license='GPL3', 
      install_requires=[],
      entry_points={
          'console_scripts': [
              'noGo2 = noGo.main:run',
              'nogo2 = noGo.main:run',
              ],
          },
      packages=packages,
      package_data=package_data,
      )
