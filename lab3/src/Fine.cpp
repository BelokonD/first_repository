#include "Fine.h"

Fine::Fine(std::string carNumber, double amount) {
    this->carNumber = carNumber;
    this->amount = amount;
}

std::string Fine::getCarNumber() const {
    return carNumber;
}

double Fine::getAmount() const {
    return amount;
}
