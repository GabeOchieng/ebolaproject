CXXFLAGS = -g -Wall -std=c++11

.PHONY: all clean
all: StochCalc

StochCalc: StochCalc.cc
	$(CXX) $(CXXFLAGS) -o StochCalc StochCalc.cc

clean:
	$(RM) *.o *.out
	$(RM) StochCalc