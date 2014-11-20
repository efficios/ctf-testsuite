import argparse
import shutil
import sys
import os


class MetadataTest:
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
            MetadataTest._perror('wrong size: {}'.format(args.size))

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
            MetadataTest._perror('invalid action: "{}"'.format(self._action))

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
