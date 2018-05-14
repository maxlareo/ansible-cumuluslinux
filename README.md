CumulusLinux
=========

[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-cumuluslinux-blue.svg)](https://galaxy.ansible.com/maxlareo/cumuluslinux/)

An Ansible role to manage [Cumulus Linux](https://cumulusnetworks.com/products/cumulus-linux/) through NCLU module.

Requirements
------------

Cumulus Linux version 3.2+ only, previous releases do not support NCLU.

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
`cl_commands` | Ansible nclu atomic commands using [recursive](#recursive) lookup, permit del/add actions, played first | Hash | `{}`
`cl_interfaces` | interfaces settings from `net add interfaces` using [recursive](#recursive) lookup | Hash | `{}`
`cl_snmp` | snmp-server settings from `net add snmp-server` using [recursive](#recursive) lookup | Hash | `{}`
`cl_syslog` | syslog setings from two subarray ipv4 and ipv6, each entry need an ip + a port and optionaly a proto(udp|tcp) | Hash | `{}`

Dependencies
------------

None

Custom Lookup
-------------

### [Recursive](https://github.com/maxlareo/ansible-cumuluslinux/blob/master/lookup_plugins/recursive.py)

To manage Cumulus Linux interfaces configuration with Ansible, I coded a lookup plugin to be able to construct the variables from a hash and it will recursivly read the nested hash to transform the hash into a list of strings.

Every depth into the variables will be added to the nclu command like that:

var:
```
cl_interfaces:
  swp1:
    ip:
      address: 192.168.1.1/24
    link:
      speed: 100
  swp2:
    bridge:
      trunk:
        vlans:
          - 1-5
          - 10,12
```

results:
```
swp1 ip address 192.168.1.1/24
swp2 bridge trunk vlans 1-5
swp2 bridge trunk vlans 10,12
```

This way I find the structure of the variables more readable for complex settings.

Example Playbook
----------------

```yaml
    - hosts: leaf01
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
        cl_interfaces:
          swp1:
            ip:
              address: 192.168.1.1/24
            link:
              speed: 100
          swp2:
            bridge:
              trunk:
                vlans:
                  - 1-5
                  - 10,12
        cl_snmp:
          listening-address:
            ip:
              - 192.168.1.10
              - 192.168.1.20
          readonly-community:
            my_rocommunity:
              access: any
        cl_commands:
          add:
            vrf: mgmt
          del:
            snmp-server: all
        cl_syslog:
          ipv4:
            - ip: 192.168.1.10
              port: 5000
              proto: tcp
            - ip: 192.168.1.20
              port: 6000
          ipv6:
            - ip: 2001:db8::1
              port: 5000
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
