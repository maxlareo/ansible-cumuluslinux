from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
"""

EXAMPLES = """
vars:
  example_dict:
    key1: value1
    key2:
      key2a: value2a
    key3:
      key3a:
        key3aa: value3aa
        key3ab: value3ab
        key3ac: value3ac
      key3b:
        - value3b1
        - value3b2
tasks:
  - name: show recursive loop
    debug: msg="{{ item }}"
    with_recursive: "{{ example_dict }}"
"""

RETURN = """
  _list:
    description:
      - list of strings
    type: list
"""

from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        def recursive(src, so_far=()):
            if isinstance(src, dict):
                for key, value in src.items():
                    for i in recursive(value, so_far + (key,)):
                        yield i
            elif isinstance(src, list):
                for item in src:
                    for i in recursive(item, so_far):
                        yield i
            else:
                yield ' '.join(so_far + (str(src),))

        results = []
        for term in terms:
            results.extend(recursive(term))
        return results
