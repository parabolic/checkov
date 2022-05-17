import os
import platform
import sys
import unittest
import re

from checkov.common.models.consts import ckv_check_id_pattern

current_dir = os.path.dirname(os.path.realpath(__file__))


class TestCheckovPlatformOnlyPolicies(unittest.TestCase):

    def test_no_ckv_ids_api_key(self):
        checks_list_path = os.path.join(current_dir, '..', 'checkov_checks_list.txt')
        if sys.version_info[1] == 7 and platform.system() == 'Linux':
            with open(checks_list_path, encoding='utf-8') as f:
                for i, line in enumerate(f):
                    if i in [0, 1]:
                        # skip the header lines
                        continue
                    line = "".join(line.split())
                    if type(line) == str and line:
                        if line == "---":
                            # end of table
                            continue
                        check_id = line.split('|')[2]
                        ckv_ids = re.match(ckv_check_id_pattern, check_id)
                        self.assertFalse(ckv_ids)


if __name__ == '__main__':
    unittest.main()
