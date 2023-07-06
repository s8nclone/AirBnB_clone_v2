#!/usr/bin/python
"""
Generates a .tgz archive from the contents of the web_static folder

function: do_pack()
"""
from fabric import tasks
import datetime


@tasks
def do_pack(c):
    """Generates a .tgz archive and saves with current date
    """
    current_time = datetime.datetime.utcnow().strftime(
        "%Y%m%d%H%M%S")
    archive_name = f"archive_{current_time}.tgz"
    c.local(f"mkdir -p versions")
    c.local(f"tar -czvf versions/{archive_name} -C web_static .")
