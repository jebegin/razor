import logging
import os
import time


def configure_logging(location=None, rpyc=False):
    console_formatter = logging.Formatter(
        '[%(asctime)s ' + '%(levelname)s:%(lineno)d] %(message)s',
        '%m-%d-%Y %H:%M:%S')
    file_formatter = logging.Formatter(
        '[%(asctime)s %(module)s ' + '%(levelname)s:%(lineno)d] %(message)s',
        '%m-%d-%Y %H:%M:%S')

    home = os.path.expanduser("~")
    path = location if location else home
    filename = 'test_results_' + time.strftime('%Y-%m-%d_%H.%M.%S')
    if rpyc:
        filename += '.rpyc.log'
    else:
        filename += '.log'

    log_file = os.path.join(path, filename)

    console_handler = logging.StreamHandler()
    # console_handler.flush()
    file_handler = logging.FileHandler(log_file, mode='w')

    console_handler.setFormatter(console_formatter)
    file_handler.setFormatter(file_formatter)

    console_handler.setLevel(logging.INFO)
    file_handler.setLevel(logging.DEBUG)

    log = logging.getLogger()

    log.setLevel(logging.DEBUG)

    if log.handlers == []:
        log.addHandler(console_handler)
    log.addHandler(file_handler)

    log.info('Results file: %s' % log_file)

    return log
