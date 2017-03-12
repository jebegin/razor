import logging
import platform

log = logging.getLogger(__name__)


class Sensor(object):
    def __init__(self):
        self.system, self.node, self.release, self.version, self.machine, \
            self.processor = platform.uname()
        if 'linux' in self.system.lower():
            # dist() is deprecated in python 3.7, will have to add logic to
            # to verify remote python version and use platform or distro
            self.dist_name, self.dist_version, self.dist_id = platform.dist()
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

    def get_distribution_name(self):
        return self.dist_name

    def get_distribution_version(self):
        return self.dist_version

    def get_distribution_id(self):
        return self.dist_id
