#!/usr/bin/env python3
from ctftestsuite.stress import MetadataTest


class Test(MetadataTest):
    what = '{size} callsites'

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

event {
	name = myevent;
};

'''

        callsite_fmt = \
'''callsite {{
	name = "myevent";
	func = "myfunc{i}";
	file = "myfile{i}";
	line = {i};
	ip = 0x{i};
}};

'''

        f.write(p1)

        for i in range(self.size):
            callsite = callsite_fmt.format(i=i)
            f.write(callsite)


if __name__ == '__main__':
    test = Test()
    test.main()
