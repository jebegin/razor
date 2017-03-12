import pytest
import rpyc
import logging
import vagrant
import time
import os
import shutil

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
    parser.addoption("--vagrant_template",
                     action="store",
                     required=True,
                     help="Name of the Vagrantfile template.",
                     default='endpoint_template')
    parser.addoption("--log_location",
                     action="store",
                     required=False,
                     help="Location for the log file, defaults to home "
                          "directory",
                     default=None)
    parser.addoption("--skip_destroy",
                     action="store_true",
                     required=False,
                     help="Do not destroy and clean up the VM")


@pytest.fixture(scope='session', autouse=True)
def logger(request):
    configure_logging(request.config.option.log_location)


@pytest.fixture(name='endpoint', scope='session')
def setup_endpoint(request):
    # Create a unique hostname base on input parameters
    index = int(time.time()*1000)
    hostname = "{}-{}".format(request.config.option.hostname, index)
    log.info('Endpoint hostname: {}'.format(hostname))

    # Create vagrant root in user home
    home = os.path.expanduser('~')
    vagrant_root = os.path.join(home, hostname)
    os.mkdir(vagrant_root)
    log.info('vagrant root: {}'.format(vagrant_root))

    # create a config.rb file
    with open(os.path.join(vagrant_root, 'config.rb'), 'w') as f:
        f.write("$box = '{}'\n$hostname = '{}'".format(
            request.config.option.box, hostname))

    # copy over Vagrantfile template for linux
    vagrant_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                               '..',
                                               'vagrant'))
    vagrant_file = os.path.join(vagrant_dir,
                                request.config.option.vagrant_template,
                                'Vagrantfile')
    log.info('Vagrantfile template: {}'.format(vagrant_file))
    shutil.copy(vagrant_file, vagrant_root)

    log.info('Issue vagrant up')
    v = vagrant.Vagrant(root=vagrant_root, quiet_stdout=True)
    v.up(provider='vmware_fusion', provision_with=['shell'])

    yield v

    if request.config.option.skip_destroy:
        log.info('Vagrant VM will not be destroyed and cleaned up.')
    else:
        log.info('Issue vagrant destroy')
        v.destroy()
        log.info('Removing vagrant root: {}'.format(vagrant_root))
        shutil.rmtree(vagrant_root)


@pytest.fixture(name='rpyc_conn', scope='session')
def rpyc_connection(endpoint):
    return rpyc.classic.connect(endpoint.hostname())
