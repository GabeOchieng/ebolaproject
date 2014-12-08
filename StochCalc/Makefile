CXXFLAGS = -g -Wall -std=c++11

.PHONY: all clean
all: StochCalc

StochCalc: StochCalc.o
	$(CXX) $(CXXFLAGS) -o StochCalc StochCalc.cc

clean:
	$(RM) *.o
	$(RM) StochCalc