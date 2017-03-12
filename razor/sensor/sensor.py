import logging
import platform
import distro

log = logging.getLogger(__name__)


class Sensor(object):
    def __init__(self):
        self.system, self.node, self.release, self.version, self.machine, \
            self.processor = platform.uname()
        if 'linux' in self.system.lower():
            self.my_distro = distro.linux_distribution()
        else:
            self.my_distro = None

    def get_system(self):
        return self.system

    def get_node(self):
        return self.node

    def get_release(self):
        return self.release

    def get_version(self):
        return self.version

    def get_machine(self):
        return self.machine

    def get_processor(self):
        return self.processor

    def get_distribution(self):
        return self.my_distro
