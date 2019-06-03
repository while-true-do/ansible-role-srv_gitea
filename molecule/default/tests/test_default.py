import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_gitea_binary_file(host):
    file = host.file('/usr/local/bin/gitea')

    assert file.exists


def test_gitea_command(host):
    cmd = host.run('gitea --version')

    assert cmd.rc == 0


def test_gitea_config_file(host):
    file = host.file('/etc/gitea/app.ini')

    assert file.exists
    assert file.user == 'root'
    assert file.group == 'gitea'


def test_gitea_service(host):
    srv = host.service('gitea')

    assert srv.is_running
    assert srv.is_enabled
