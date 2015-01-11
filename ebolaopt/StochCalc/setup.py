from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import os
import sys


StochCalc_version = "OpenMP"

if StochCalc_version == "OpenMP":
    extra_compile_args = ["-std=c++11", "-fopenmp", "-O3"]
    extra_link_args=["-std=c++11", "-lgomp"]
    setup_sources=["StochLib.pyx", "ModelParams.cc",
                   "StochParams.cc", "StochCalc.cc"]

# http://blog.michael.kuron-germany.de/2013/02/using-c11-on-mac-os-x-10-8/
# Additional configuration if running Mac OS X
# TODO: add warnings if compiler is not up to date
if sys.platform == 'darwin':
    os.environ["CC"] = "clang-mp-3.5"
    os.environ["CXX"] = "clang-mp-3.5"
    extra_compile_args.append("-stdlib=libc++")
    extra_link_args.append("-lc++")
 
setup(
    name = 'Demos',
    ext_modules=[ 
        Extension("StochLib", 
                  sources=setup_sources, 
                  language="c++",
                  extra_compile_args=extra_compile_args,
                  extra_link_args=extra_link_args),
        ],
    cmdclass = {'build_ext': build_ext},
    )

