#include "AverageStubImpl.hpp"

AverageStubImpl::AverageStubImpl() { }
AverageStubImpl::~AverageStubImpl() { }

void AverageStubImpl::findAverage(const std::shared_ptr<CommonAPI::ClientId> _client,
	int32_t n1, int32_t n2, findAverageReply_t _reply) {
    std::cout << "AverageStubImpl: Service called by ID: " << _client->hashCode() << std::endl;
    _reply(((double)n1 + (double)n2 ) / 2);
};
