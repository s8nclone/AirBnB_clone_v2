#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of the web_static folder

function: do_pack()
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive and saves with current date
    """
    current_time = datetime.utcnow().strftime(
        "%Y%m%d%H%M%S")
    archive_name = f"web_static_{current_time}.tgz"
    local(f"mkdir -p versions")
    if local(f"tar -czvf versions/{archive_name} web_static").failed:
        return None
    return f"versions/{archive_name}"
