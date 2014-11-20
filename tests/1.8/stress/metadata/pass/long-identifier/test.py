#!/usr/bin/env python3
from ctftestsuite.stress import MetadataTestAssitant


class TestAssistant(MetadataTestAssitant):
    what = 'long identifier of {size} chars'

    def write_metadata(self, f):
        p1 = \
'''event {
	name = myevent;
	fields := struct {
		uint8_t '''

        p2 = \
''';
	};
};
'''

        f.write(self.BASIC_PROLOGUE)
        f.write(p1)

        for i in range(self.size):
            f.write('A')

        f.write(p2)


if __name__ == '__main__':
    test_assistant = TestAssistant()
    test_assistant.main()
