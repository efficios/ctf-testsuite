ctf-testsuite
=============

The Common Trace Format (CTF) test suite is intended to validate the
conformance of CTF readers.

To run the test suite:

  1. Set the `CTF_READER_BIN` environment variable to your CTF reader
    executable, e.g.:

        export CTF_READER_BIN=my-ctf-reader

  2. Execute the `run.sh` script found in the `tests/x.y` directory,
     where `x.y` is the CTF specification's version you want to check,
     e.g.:

        ( cd tests/1.8 && ./run.sh )

You may also set the `CTF_READER_OPTS` environment variable to options
to pass to the CTF reader defined by `CTF_READER_BIN`.
