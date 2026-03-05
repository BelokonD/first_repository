#include <iostream>
#include "ParkingSystem.h"

int main() {
    ParkingSystem system;

    Fine f1("AA1234BB", 200);
    Fine f2("BC5678CD", 500);
    Fine f3("AE9012EF", 300);

    system.addFine(f1);
    system.addFine(f2);
    system.addFine(f3);

    std::cout << "Total fines: " << system.calculateTotal() << " ₴" << std::endl;

    return 0;
}
