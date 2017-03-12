import pytest
import logging

log = logging.getLogger(__name__)


@pytest.mark.usefixtures('sensor')
class TestEndpoint:
    def test_endpoint(self, sensor):
        log.info('Verify sensor is install on Linux Ubuntu 12.04 LTS')
        assert 'linux' in sensor.get_system().lower()
        assert 'ubuntu' in sensor.get_distribution_name().lower()
        assert '12.04' in sensor.get_distribution_version()
        log.info('The endpoints distribution is: {} {} {}'.format(
            sensor.get_system(),
            sensor.get_distribution_name(),
            sensor.get_distribution_version()))
