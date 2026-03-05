#ifndef FINE_H
#define FINE_H

#include <string>

class Fine {
private:
    std::string carNumber;
    double amount;

public:
    Fine(std::string carNumber, double amount);

    std::string getCarNumber() const;
    double getAmount() const;
};

#endif
