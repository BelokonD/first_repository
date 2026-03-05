#include "ParkingSystem.h"

void ParkingSystem::addFine(const Fine& fine) {
    fines.push_back(fine);
}

double ParkingSystem::calculateTotal() const {
    double total = 0;

    for (const auto& fine : fines) {
        total += fine.getAmount();
    }

    return total;
}
