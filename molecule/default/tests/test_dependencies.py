import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


@pytest.mark.parametrize("name", [
    ("git"),
    ("python2"),
    ("python2-devel")
])
def test_packages(host, name):
    pkg = host.package(name)

    assert pkg.is_installed