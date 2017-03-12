import pytest
import logging

log = logging.getLogger(__name__)


@pytest.mark.usefixtures('sensor')
class TestEndpoint:
    def test_endpoint(self, sensor):
        log.info('Verify sensor is install on Linux 12.04 LTS')
        assert 'linux' in sensor.get_system().lower()
        log.info('distro: {}'.format(sensor.get_distribution()))
