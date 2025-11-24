import subprocess
import sys

from test3 import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "test3", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
