# -*- coding: utf-8 -*-
# Copyright (C) 2018-2021 Greenbone Networks GmbH
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gvm.errors import RequiredArgument


class GmpGetScannerTestCase:
    def test_get_scanner(self):
        self.gmp.get_scanner('s1')

        self.connection.send.has_been_called_with(
            '<get_scanners scanner_id="s1" details="1"/>'
        )

        self.gmp.get_scanner(scanner_id='s1')

        self.connection.send.has_been_called_with(
            '<get_scanners scanner_id="s1" details="1"/>'
        )

    def test_get_scanner_missing_scanner_id(self):
        with self.assertRaises(RequiredArgument):
            self.gmp.get_scanner(scanner_id=None)

        with self.assertRaises(RequiredArgument):
            self.gmp.get_scanner('')
