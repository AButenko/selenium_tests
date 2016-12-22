import contextlib
import logging
import os
import time

# This is logging.Logger instance fof logging in tests and framework.
framework_logger = None


# TODO need to fix logging system - log each module to separate folder (do i need this?)
def init_logger(folder, file):
    """
    Pytest fixture, executes in scope of module.
    Creates logging file for this module.
    Args:
        folder:     folder to keep log files of this run.
        file:       name of logger file.
    Returns: logging.Logger instance.

    """
    global framework_logger

    # create folder for log files if not exists
    with contextlib.suppress(FileExistsError):
        os.mkdir(folder)

    # create formatter
    formatter = logging.Formatter('%(asctime)-15s | %(lineno)-05d:%(filename)-20s | %(levelname)-8s | %(message)s')

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # add formatter to ch
    ch.setFormatter(formatter)

    logname = folder + file + '_' + time.strftime("%Y%m%d%H%M%S")
    # create file handler and set level to debug
    fh = logging.FileHandler(logname + '.log')
    fh.setLevel(logging.DEBUG)
    # add formatter to fh
    fh.setFormatter(formatter)


    # create logger
    framework_logger = logging.getLogger(logname)
    # add handlers to logger
    framework_logger.addHandler(ch)
    framework_logger.addHandler(fh)

    return framework_logger