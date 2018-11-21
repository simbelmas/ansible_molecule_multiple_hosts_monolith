# multiple hosts test with molecule

molecule is a test framework included in ansible project availabel at https://github.com/ansible/molecule/
This repo present a multi host test with two roles:
- php : install php7.0 and php-fpn on ubuntu + run unit tests with molecule on one host in default scenario
- webfront : install nginx on ubuntu and run unit tests (scenario default) or multiple host test (dynamicfront)

The idea is to use the funtional playbook in the webfront role to test the complete stack.
This setup requires:
- ansible and molecule are installed
- vagrant, libvirt and vagrant-libvirt plugin are working

# run tests

## php
Go to the php role then `molecule test`

## front
To test front only (without dynamic site), go to webfront roel and run `molecule test`
To test full stack, go to webfront role and run `molecule test --scenario-name dynamicfront`
