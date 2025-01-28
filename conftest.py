import glob
import logging
from time import sleep

import pytest

from reportportal_client import RPLogger

import rp_attachments


@pytest.fixture(scope="session")
def rp_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logging.setLoggerClass(RPLogger)
    return logger


@pytest.fixture(autouse=True)
def attach_pw_trace_to_rp(rp_logger: RPLogger):
    yield
    trace_files = glob.glob("test-results/**/*.zip", recursive=True)
    for trace_file in trace_files:
        rp_attachments.attach_file(rp_logger=rp_logger,
                                   log_message="Playwright Trace File",
                                   file_to_attach_path=trace_file)
