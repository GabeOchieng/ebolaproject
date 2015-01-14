Installation
============

Dependencies
------------

EbolaOpt requires:

* gcc4.8 or higher
* python2.7
* numpy
* scipy
* matplotlib
* PyQt (optional)

If you do not already have python2.7, numpy, scipy, and matplotlib, the Anaconda 
distribution is a convenient way to install them.

How to Install
--------------

On Unix machines (e.g. Linux or Mac OS X), download EbolaOpt-0.1.tar.gz 
from our github repository at https://github.com/altafang/ebolaproject and
go into the directory into which you downloaded it. Then execute::

    tar -xvf EbolaOpt-0.1.tar.gz
    cd EbolaOpt-0.1/
    python setup.py install
    
If you do not have root permissions, you can do the following instead of
"python setup.py install"::

    python setup.py install --home=$HOME
    export PYTHONPATH=$PYTHONPATH:$HOME/lib/python
    
    
Extra tips for installation on Mac OS X
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If your built-in version of gcc is out of date, you can update it by installing
gcc4.9 using MacPorts::

    sudo port install gcc49
    
Now change the g++ and gcc symbolic links to point to the new version::

    sudo mv /usr/bin/gcc /usr/bin/gcc_old
    sudo ln -s /opt/local/bin/gcc-mp-4.9 /usr/bin/gcc
    sudo mv /usr/bin/g++ /usr/bin/g++_old
    sudo ln -s /opt/local/bin/g++-mp-4.9 /usr/bin/g++
    
Testing
-------

Now you should be ready to use EbolaOpt. To test, execute::

    cd ebolaopt/tests/
    python test_optimization.py
    
You can also test that installation worked by going into any directory 
(except directories that contain a directory called ebolaopt), and at the python
command prompt, execute::

    import ebolaopt
    ebolaopt.optimize()
    

