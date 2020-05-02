import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
includes = []
packages = []
excludes = []
include_files = [('src', 'src'), ('dll', 'lib')]

build_exe_options = {"includes": includes,
                     "packages": packages,
                     "excludes": excludes,
                     "include_files": include_files}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(name='The Gecko App',
      version='0.0.7',
      description='AIO bot',
      options={'build_exe': build_exe_options},
      executables=[Executable(script='the_gecko_app.py', base=base)])