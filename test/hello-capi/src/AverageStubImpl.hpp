#ifndef HELLOWORLDSTUBIMPL_H_
#define HELLOWORLDSTUBIMPL_H_

#include <CommonAPI/CommonAPI.hpp>
#include <AverageStubDefault.hpp>

class AverageStubImpl : public v1::hellocapi::AverageStubDefault {
public:
    AverageStubImpl();
    virtual ~AverageStubImpl();
    virtual void findAverage(const std::shared_ptr<CommonAPI::ClientId> _client, int n1, int n2, findAverageReply_t _return);
};

#endif /* HELLOWORLDSTUBIMPL_H_ */