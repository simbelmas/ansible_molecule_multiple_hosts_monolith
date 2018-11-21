import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nginx_install(host):
    p = host.package('nginx')
    assert p.is_installed


def test_nginx_started_enabled(host):
    s = host.service('nginx')
    assert s.is_running
    assert s.is_enabled
