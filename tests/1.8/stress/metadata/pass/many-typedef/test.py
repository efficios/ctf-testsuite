#!/usr/bin/env python3
from ctftestsuite.stress import MetadataTest


class Test(MetadataTest):
    what = '{size} typedefs'

    def write_metadata(self, f):
        p1 = \
'''/* CTF 1.8 */

typealias integer { size = 8; align = 8; signed = false; base = 10; } := uint8_t;
typealias integer { size = 32; align = 8; signed = false; base = hex; } := uint32_t;

trace {
	major = 0;
	minor = 0;
	uuid = "2a6422d0-6cee-11e0-8c08-cb07d7b3a564";
	byte_order = le;
	packet.header := struct {
		uint32_t magic;
		uint8_t uuid[16];
	};
};

'''

        typedef_fmt = \
'''typedef integer {{ size = 8; align = 8; signed = false; base = 10; }} t{name};
'''

        f.write(p1)

        for i in range(self.size):
            typedef = typedef_fmt.format(name=i)
            f.write(typedef)


if __name__ == '__main__':
    test = Test()
    test.main()
