#ifndef AVERAGESTUBIMPL_H
#define AVERAGESTUBIMPL_H

#include <CommonAPI/CommonAPI.hpp>
#include <AverageStubDefault.hpp>

class AverageStubImpl : public v1::hellosys::AverageStubDefault {
public:
    AverageStubImpl();
    virtual ~AverageStubImpl();
    virtual void findAverage(const std::shared_ptr<CommonAPI::ClientId> _client, int n1, int n2, findAverageReply_t _return);
};

#endif /* AVERAGESTUBIMPL_H */