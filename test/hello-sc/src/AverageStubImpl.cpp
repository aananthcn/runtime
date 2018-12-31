#include "AverageStubImpl.hpp"

AverageStubImpl::AverageStubImpl() { }
AverageStubImpl::~AverageStubImpl() { }

void AverageStubImpl::findAverage(const std::shared_ptr<CommonAPI::ClientId> _client,
	int32_t n1, int32_t n2, findAverageReply_t _reply) {
    _reply((n1 + n2 ) / 2);
};