#!/usr/bin/env python3
from ctftestsuite.stress import MetadataTestAssitant


class TestAssistant(MetadataTestAssitant):
    what = '{size} callsites'

    def write_metadata(self, f):
        p1 = \
'''event {
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

        f.write(self.BASIC_PROLOGUE)
        f.write(p1)

        for i in range(self.size):
            callsite = callsite_fmt.format(i=i)
            f.write(callsite)


if __name__ == '__main__':
    test_assistant = TestAssistant()
    test_assistant.main()
