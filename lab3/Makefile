CXX = g++
CXXFLAGS = -Wall -std=c++17

SRC = src/main.cpp src/Fine.cpp src/ParkingSystem.cpp
OBJ = $(SRC:.cpp=.o)

TARGET = parking_app

all: $(TARGET)

$(TARGET): $(OBJ)
	$(CXX) $(OBJ) -o $(TARGET)

clean:
	rm -f $(OBJ) $(TARGET)
