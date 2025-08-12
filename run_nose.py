import collections
import collections.abc
collections.Callable = collections.abc.Callable

import nose
import sys

sys.exit(nose.run(argv=sys.argv[1:]))

