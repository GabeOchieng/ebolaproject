from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
 
setup(
    name = 'Demos',
    ext_modules=[ 
        Extension("StochLib", 
                  sources=["StochLib.pyx", "ModelParams.cc", 
                           "StochParams.cc", "StochCalc.cc"], 
                  language="c++",
                  extra_compile_args=["-std=c++11"],
                  extra_link_args=["-std=c++11"]),
        ],
    cmdclass = {'build_ext': build_ext},
    )
