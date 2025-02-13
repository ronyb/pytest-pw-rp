from datetime import datetime
import logging
import os

import pytest
from _pytest.fixtures import FixtureRequest
from playwright.sync_api import BrowserContext
from reportportal_client import RPLogger

import rp_attachments


@pytest.fixture(scope="session")
def rp_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logging.setLoggerClass(RPLogger)
    return logger


@pytest.fixture(scope="function", autouse=True)
def strat_pw_trace_and_attach_to_rp_after_test(context: BrowserContext, request: FixtureRequest, rp_logger: RPLogger):
    """
    Starts Playwright tracing for each test, saves the trace file with a custom name
    and attaches the trace file to ReportPortal report
    """

    test_name = request.node.name
    timestamp = datetime.now().strftime("%Y.%m.%d_%H.%M.%S")
    trace_dir = "playwright-traces"
    os.makedirs(trace_dir, exist_ok=True)
    trace_file_path = os.path.join(trace_dir, f"{test_name}_{timestamp}.zip")

    # Start Playwright tracing
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield

    # Stop Playwright tracing and save it to file
    context.tracing.stop(path=trace_file_path)

    # Attach the trace file to ReportPortal
    rp_attachments.attach_file(rp_logger=rp_logger,
                               log_message="Playwright Trace File",
                               file_to_attach_path=trace_file_path)
