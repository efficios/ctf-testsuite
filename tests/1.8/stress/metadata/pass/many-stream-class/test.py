#!/usr/bin/env python3
from ctftestsuite.stress import MetadataTestAssistant


class TestAssistant(MetadataTestAssistant):
    what = '{size} stream classes'

    def write_metadata(self, f):
        p1 = \
'''/* CTF 1.8 */

typealias integer { size = 8; align = 8; signed = false; base = 10; } := uint8_t;
typealias integer { size = 32; align = 8; signed = false; base = hex; } := uint32_t;
typealias integer { size = 64; align = 8; signed = false; base = hex; } := uint64_t;

trace {
	major = 1;
	minor = 8;
	uuid = "2a6422d0-6cee-11e0-8c08-cb07d7b3a564";
	byte_order = le;
	packet.header := struct {
		uint32_t magic;
		uint8_t uuid[16];
		uint64_t stream_id;
	};
};

'''

        stream_fmt = \
'''stream {{
	id = {id};
}};

'''

        f.write(p1)

        for i in range(self.size):
            stream = stream_fmt.format(id=i)
            f.write(stream)


if __name__ == '__main__':
    test_assistant = TestAssistant()
    test_assistant.main()
