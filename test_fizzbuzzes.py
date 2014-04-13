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

import sys
import unittest

from fizzbuzzes import FizzBuzz
from fizzbuzzes import fizzbuzzes


class AbstractFizzBuzzesTests(object):
    TEST_LIST = [
        '1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz',
        '11', 'Fizz', '13', '14', 'FizzBuzz'
    ]

    def _get_object(self):
        raise notImplementedError()

    def test_generate(self):
        fb_obj = self.get_object()
        fb_list = list(fb_obj.generate(limit=15))
        assert fb_list == self.TEST_LIST

    def test_string(self):
        TEST_STRING = "\n".join(self.TEST_LIST)
        obj = self.get_object()
        assert obj.string(limit=15) == TEST_STRING

    def test_csv_string(self):
        TEST_STRING = ",".join(self.TEST_LIST)
        obj = self.get_object()
        assert obj.string(limit=15, separator=",") == TEST_STRING

    def test_print_output(self):
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("Need to run in buffered mode. (-b or --buffer)")
        TEST_STRING = ",".join(self.TEST_LIST)
        obj = self.get_object()
        obj.print_output(limit=15, separator=",")
        output = sys.stdout.getvalue().strip()
        assert output == TEST_STRING


class FizzBuzzTestCase(unittest.TestCase, AbstractFizzBuzzesTests):
    def get_object(self):
        return FizzBuzz()


class FizzBuzzMapSliceTestCase(unittest.TestCase, AbstractFizzBuzzesTests):
    def get_object(self):
        return fizzbuzzes.FizzBuzzMapSlice()


if __name__ == '__main__':
    unittest.main()
