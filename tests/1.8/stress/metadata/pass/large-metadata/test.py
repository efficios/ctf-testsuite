#!/usr/bin/env python3
from ctftestsuite.stress import MetadataTestAssistant


class TestAssistant(MetadataTestAssistant):
    what = 'large metadata with {size} extra chars'

    def write_metadata(self, f):
        p1 = \
'''event {
	name = myevent;
	fields := struct {
		uint8_t f;
	};
'''
        p2 = '\n};\n'

        f.write(self.BASIC_PROLOGUE)
        f.write(p1)

        for i in range(self.size):
            f.write(' ')

        f.write(p2)


if __name__ == '__main__':
    test_assistant = TestAssistant()
    test_assistant.main()
