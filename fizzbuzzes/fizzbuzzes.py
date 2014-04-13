# Copyright (C) 2014 Will Moggridge, will@willmoggridge.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import operator
from itertools import cycle
from itertools import islice


class AbstractFizzBuzz(object):
    def generate(self, limit=100):
        raise notImplementedError()

    def string(self, limit=100, separator="\n"):
        fizzbuzz_list = list(self.generate(limit=limit))
        return str(separator).join(fizzbuzz_list)

    def print_output(self, limit=100, separator="\n"):
        print(self.string(limit=limit, separator=separator))


class FizzBuzzMapSlice(AbstractFizzBuzz):
    def generate(self, limit=100):
        fizz = ([""] * 2) + ["Fizz"]
        buzz = ([""] * 4) + ["Buzz"]
        fizzbuzz_map = map(operator.add, cycle(fizz), cycle(buzz))
        fizzbuzz_slice = islice(fizzbuzz_map, int(limit))
        for i, fb in enumerate(fizzbuzz_slice, start=1):
            yield(fb or str(i))
