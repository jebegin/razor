import pytest
import logging

log = logging.getLogger(__name__)


@pytest.mark.usefixtures('endpoint')
class TestEndpoint:
    def test_endpoint(self, endpoint):
        log.info('Endpoint IP address is: {}'.format(endpoint.hostname()))
        assert 1
