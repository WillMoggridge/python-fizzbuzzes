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

from fizzbuzzes import fizzbuzzes


class FizzBuzz(object):
    TYPE_MAP_SLICE = 1

    def __init__(self, class_type=1):
        if class_type is self.TYPE_MAP_SLICE:
            self.object = fizzbuzzes.FizzBuzzMapSlice()
        else:
            raise Exception("Invalid class type")

    def generate(self, limit=100):
        return self.object.generate(limit=limit)

    def string(self, limit=100, separator="\n"):
        return self.object.string(limit=limit, separator=separator)

    def print_output(self, limit=100, separator="\n"):
        self.object.print_output(limit=limit, separator=separator)
