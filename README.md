CumulusLinux
=========

[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-emby-blue.svg)](https://galaxy.ansible.com/maxlareo/cumuluslinux/)

An Ansible role to manage [Cumulus Linux](https://cumulusnetworks.com/products/cumulus-linux/) through NCLU module.

Requirements
------------

None

Role Variables
--------------

- `cl_license`: [default: `''`]: [CumulusLinux license](https://support.cumulusnetworks.com/hc/en-us/articles/205329608-Understanding-the-License-for-Cumulus-Linux-2-5-3-and-Later)
- `cl_hostname`: [default: `cumulus`]: Hostname of the device
- `cl_time_zone`: [default: `Etc/UTC`]: Timezone
- `cl_time_ntp_servers`: [default: `[]`]: NTP servers list, possibility to add iburst option
- `cl_time_ntp_source`: [default: `eth0`]: NTP source interface
- `cl_locales`: [default: `[]`]: Enable locale from locale-gen

Dependencies
------------

None

Example Playbook
----------------

```yaml
    - hosts: network_cl
      roles:
        - cumuluslinux
      vars:
        cl_license: user@company.com|thequickbrownfoxjumpsoverthelazydog312
        cl_hostname: leaf01
        cl_time_zone: Europe/Paris
        cl_time_ntp_servers:
          - 0.cumulusnetworks.pool.ntp.org iburst
          - 1.cumulusnetworks.pool.ntp.org 
          - 2.cumulusnetworks.pool.ntp.org 
          - 3.cumulusnetworks.pool.ntp.org 
        cl_time_ntp_source: eth1
        cl_locales:
          - en_US.UTF-8 UTF-8
          - fr_FR.UTF-8 UTF-8
```

License
-------

MIT

Author Information
------------------

[Maxime Lareo](https://github.com/maxlareo)

Feedback, bug-reports, requests, ...
------------------------------------

Are [welcome](https://github.com/maxlareo/ansible-cumuluslinux/issues) !
