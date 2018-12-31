#include <iostream>
#include <string>
#include <unistd.h>
#include <CommonAPI/CommonAPI.hpp>
#include <AverageProxy.hpp>

using namespace v1::hellosc;

int main() {
    std::shared_ptr < CommonAPI::Runtime > runtime = CommonAPI::Runtime::get();
    std::shared_ptr<AverageProxy<>> myProxy = runtime->buildProxy<AverageProxy>("local", "test");

    std::cout << "Checking availability!" << std::endl;
    while (!myProxy->isAvailable())
        usleep(10);
    std::cout << "Available..." << std::endl;

    CommonAPI::CallStatus callStatus;
    int32_t n1, n2, returnValue;

    std::cout << "Enter number 1:";
    std::cin >> n1;
    std::cout << "Enter number 2:";
    std::cin >> n2;

    myProxy->findAverage(n1, n2, callStatus, returnValue);
    std::cout << "Got average value: '" << returnValue << "'\n";

    return 0;
}