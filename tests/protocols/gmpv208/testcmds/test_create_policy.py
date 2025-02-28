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


class GmpCreatePolicyTestCase:
    def test_create_policy(self):
        self.gmp.create_policy('foo')

        self.connection.send.has_been_called_with(
            '<create_config>'
            '<copy>085569ce-73ed-11df-83c3-002264764cea</copy>'
            '<name>foo</name>'
            '<usage_type>policy</usage_type>'
            '</create_config>'
        )

    def test_create_with_policy_id(self):
        self.gmp.create_policy('foo', policy_id='p1')

        self.connection.send.has_been_called_with(
            '<create_config>'
            '<copy>p1</copy>'
            '<name>foo</name>'
            '<usage_type>policy</usage_type>'
            '</create_config>'
        )

    def test_missing_name(self):
        with self.assertRaises(RequiredArgument):
            self.gmp.create_policy(policy_id='c1', name=None)

        with self.assertRaises(RequiredArgument):
            self.gmp.create_policy(policy_id='c1', name='')
