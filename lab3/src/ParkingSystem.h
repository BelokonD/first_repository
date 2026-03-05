#ifndef PARKINGSYSTEM_H
#define PARKINGSYSTEM_H

#include <vector>
#include "Fine.h"

class ParkingSystem {
private:
    std::vector<Fine> fines;

public:
    void addFine(const Fine& fine);
    double calculateTotal() const;
};

#endif
