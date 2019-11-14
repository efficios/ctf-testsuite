import argparse
import shutil
import sys
import os


class MetadataTestAssistant:
    BASIC_PROLOGUE = \
'''/* CTF 1.8 */

typealias integer { size = 8; align = 8; signed = false; base = 10; } := uint8_t;
typealias integer { size = 32; align = 8; signed = false; base = hex; } := uint32_t;

trace {
    major = 1;
    minor = 8;
    uuid = "2a6422d0-6cee-11e0-8c08-cb07d7b3a564";
    byte_order = le;
    packet.header := struct {
        uint32_t magic;
        uint8_t uuid[16];
    };
};

'''

    def __init__(self):
        self._actions = {
            'prepare': self._prepare,
            'clean': self._clean,
        }

    @staticmethod
    def _perror(str):
        print('Error: {}'.format(str), file=sys.stderr)
        sys.exit(1)

    def _parse_args(self):
        ap = argparse.ArgumentParser()

        ap.add_argument('-s', '--size', action='store', metavar='SIZE',
                        type=int, required=True, help='size')
        ap.add_argument('action', metavar='ACTION', action='store',
                        help='action')

        # parse args
        args = ap.parse_args()

        # validate size
        if args.size < 1:
            MetadataTestAssistant._perror('wrong size: {}'.format(args.size))

        return args

    def _get_what(self):
        return self.what.format(size=self.size)

    def _prepare(self):
        # make sure everything is clean first
        self._clean()

        print('Preparing test for {}'.format(self._get_what()))

        # make test directory
        os.mkdir(self._trace_dir_path)

        # open and write metadata file
        with open(self._metadata_path, 'w') as f:
            self.write_metadata(f)

    def _clean(self):
        print('Cleaning up test for {}'.format(self._get_what()))

        try:
            shutil.rmtree(self._trace_dir_path, ignore_errors=True)
        except Exception as e:
            # ignore
            pass

    def _do_action(self):
        if self._action not in self._actions:
            msg = 'invalid action: "{}"'.format(self._action)
            MetadataTestAssistant._perror(msg)

        self._actions[self._action]()

    @property
    def size(self):
        return self._size

    def main(self):
        args = self._parse_args()
        self._size = args.size
        self._trace_dir_path = 'trace-{}'.format(args.size)
        self._metadata_path = os.path.join(self._trace_dir_path, 'metadata')
        self._action = args.action

        self._do_action()
