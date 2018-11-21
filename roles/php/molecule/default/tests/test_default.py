import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('phppackage', ['php7.0', 'php7.0-fpm'])
def test_php_installed(phppackage, host):
        assert host.package(phppackage).is_installed


def test_php_service(host):
    s = host.service('php7.0-fpm.service')
    assert s.is_running
    assert s.is_enabled


def test_fpm_socket(host):
    assert host.socket('tcp://9000').is_listening
