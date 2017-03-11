import pytest
import rpyc
import logging
import vagrant

from razor.common.logger import configure_logging

log = logging.getLogger(__name__)

def pytest_addoption(parser):
    parser.addoption("--box",
                     action="store",
                     required=True,
                     help="Name of vagrant box.")
    parser.addoption("--hostname",
                     action="store",
                     required=True,
                     help="Hostname of the endpoint.")


@pytest.fixture(name='endpoint', scope='session')
def setup_endpoint(request):

    v = vagrant.Vagrant(root=endpoint_dir)
    v.up(provider='vmware_fusion', provision_with=['shell'])
    ip_address = v.hostname()
