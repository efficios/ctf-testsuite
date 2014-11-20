#!/usr/bin/env python3
from ctftestsuite.stress import MetadataTest


class Test(MetadataTest):
    what = '{size} typedefs'

    def write_metadata(self, f):
        typedef_fmt = \
'''typedef integer {{ size = 8; align = 8; signed = false; base = 10; }} t{name};
'''

        f.write(self.BASIC_PROLOGUE)

        for i in range(self.size):
            typedef = typedef_fmt.format(name=i)
            f.write(typedef)


if __name__ == '__main__':
    test = Test()
    test.main()
