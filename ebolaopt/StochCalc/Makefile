Args=StochCalc.cc StochCalc.h StochParams.cc StochParams.h
Args2=ModelParams.cc ModelParams.h setup.py StochLib.pyx
.PHONY: all clean
all: StochLib.so

StochLib.so: $(Args) $(Args2)
	python setup.py build_ext --inplace

clean:
	$(RM) *.o *.out
	$(RM) -r build
	$(RM) StochLib.so StochLib.cpp