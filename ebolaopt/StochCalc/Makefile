Args=StochCalc_omp.cc StochCalc_serial.cc StochCalc.h StochParams.cc
Args2=StochParams.h ModelParams.cc ModelParams.h setup.py StochLib.pyx
.PHONY: all clean
all: StochLib.so

StochLib.so: $(Args) $(Args2)
	python setup.py build_ext --inplace

clean:
	$(RM) *.o *.out
	$(RM) -r build
	$(RM) StochLib.so StochLib.cpp