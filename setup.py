# Python2.7
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

extra_compile_args = ["-std=c++11", "-fopenmp", "-O3"]
extra_link_args=["-std=c++11", "-lgomp"]
setup_sources=["ebolaopt/StochCalc/StochLib.pyx", "ebolaopt/StochCalc/ModelParams.cc",
       "ebolaopt/StochCalc/StochParams.cc", "ebolaopt/StochCalc/StochCalc_omp.cc"]

setup(name='EbolaOpt',
      version='0.1',
      description='Resource allocation optimization over Ebola epidemic model',
      url='https://github.com/altafang/ebolaproject',
      packages=['ebolaopt', 'ebolaopt.StochCalc', 'ebolaopt.tests'],
      package_data={'ebolaopt':['data/constraints.csv', 'data/case_counts.csv']},
      ext_modules=[
                   Extension("StochLib",
                             sources=setup_sources,
                             language="c++",
                             extra_compile_args=extra_compile_args,
                             extra_link_args=extra_link_args),
                   ],
      cmdclass = {'build_ext': build_ext},
     )



