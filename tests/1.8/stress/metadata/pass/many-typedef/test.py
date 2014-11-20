#!/usr/bin/env python3
from ctftestsuite.stress import MetadataTestAssistant


class TestAssistant(MetadataTestAssistant):
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
    test_assistant = TestAssistant()
    test_assistant.main()
