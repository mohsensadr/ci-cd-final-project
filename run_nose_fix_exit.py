import collections
import collections.abc
collections.Callable = collections.abc.Callable

import nose
import sys

if __name__ == "__main__":
    # Run nose and store the boolean result
    success = nose.run(argv=sys.argv[1:])
    # Exit 0 if success is True, else 1
    sys.exit(0 if success else 1)

