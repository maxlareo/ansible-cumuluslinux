CumulusLinux
=========

[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-cumuluslinux-blue.svg)](https://galaxy.ansible.com/maxlareo/cumuluslinux/)

An Ansible role to manage [Cumulus Linux](https://cumulusnetworks.com/products/cumulus-linux/) through NCLU module.

Requirements
------------

None

Role Variables
--------------

Variable    | Description | Type | Default
------------|-------------|------|--------
`cl_license` | [CumulusLinux license](https://support.cumulusnetworks.com/hc/en-us/articles/205329608-Understanding-the-License-for-Cumulus-Linux-2-5-3-and-Later) | String | `''`
`cl_hostname` | Hostname of the device | String | `cumulus`
`cl_time_zone` | Timezone | String | `Etc/UTC`
`cl_time_ntp_servers` | NTP servers list, possibility to add iburst option | Array | `[]`
`cl_time_ntp_source` | NTP source interface | String | `eth0`
`cl_locales` | Enable locale from locale-gen | Array | `[]`
`cl_dns_nameserver_ipv4` | DNS nameserver in IPv4 | Array | `[]`
`cl_dns_nameserver_ipv6` | DNS nameserver in IPv6 | Array | `[]`

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
        cl_dns_nameserver_ipv4:
          - 9.9.9.9
          - 1.1.1.1
        cl_dns_nameserver_ipv6:
          - 2620:fe::fe
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
