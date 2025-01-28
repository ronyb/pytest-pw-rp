import os

from reportportal_client import RPLogger


def attach_file(rp_logger: RPLogger, log_message: str, file_to_attach_path: str, mime: str = "application/octet-stream"):

    file_name = os.path.basename(file_to_attach_path)

    with open(file_to_attach_path, "rb") as file:
        file_content = file.read()

    rp_logger.info(
        log_message,
        attachment={
            "name": file_name,
            "data": file_content,
            "mime": mime,
        },
    )