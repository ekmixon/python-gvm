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

from gvm.errors import RequiredArgument, InvalidArgumentType

from gvm.protocols.gmpv208 import AliveTest


class GmpCreateTargetCommandTestCase:
    def test_create_target_with_make_unique(self):
        with self.assertWarns(DeprecationWarning):
            self.gmp.create_target(
                'foo',
                port_list_id='pl1',
                make_unique=True,
                hosts=['foo', 'bar'],
            )

            self.connection.send.has_been_called_with(
                '<create_target>'
                '<name>foo</name>'
                '<hosts>foo,bar</hosts>'
                '<port_list id="pl1"/>'
                '</create_target>'
            )

        with self.assertWarns(DeprecationWarning):
            self.gmp.create_target(
                'foo',
                port_list_id='pl1',
                make_unique=False,
                hosts=['foo', 'bar'],
            )

            self.connection.send.has_been_called_with(
                '<create_target>'
                '<name>foo</name>'
                '<hosts>foo,bar</hosts>'
                '<port_list id="pl1"/>'
                '</create_target>'
            )

    def test_create_target_missing_name(self):
        with self.assertRaises(RequiredArgument):
            self.gmp.create_target(None, hosts=['foo'])

        with self.assertRaises(RequiredArgument):
            self.gmp.create_target(name=None, hosts=['foo'])

        with self.assertRaises(RequiredArgument):
            self.gmp.create_target('', hosts=['foo'])

    def test_create_target_with_asset_hosts_filter(self):
        self.gmp.create_target(
            'foo', port_list_id='pl1', asset_hosts_filter='name=foo'
        )

        self.connection.send.has_been_called_with(
            '<create_target>'
            '<name>foo</name>'
            '<asset_hosts filter="name=foo"/>'
            '<port_list id="pl1"/>'
            '</create_target>'
        )

    def test_create_target_missing_hosts(self):
        with self.assertRaises(RequiredArgument):
            self.gmp.create_target(name='foo')

    def test_create_target_with_comment(self):
        self.gmp.create_target(
            'foo', hosts=['foo'], port_list_id='pl1', comment='bar'
        )

        self.connection.send.has_been_called_with(
            '<create_target>'
            '<name>foo</name>'
            '<hosts>foo</hosts>'
            '<comment>bar</comment>'
            '<port_list id="pl1"/>'
            '</create_target>'
        )

    def test_create_target_with_exclude_hosts(self):
        self.gmp.create_target(
            'foo',
            hosts=['foo', 'bar'],
            port_list_id='pl1',
            exclude_hosts=['bar', 'ipsum'],
        )

        self.connection.send.has_been_called_with(
            '<create_target>'
            '<name>foo</name>'
            '<hosts>foo,bar</hosts>'
            '<exclude_hosts>bar,ipsum</exclude_hosts>'
            '<port_list id="pl1"/>'
            '</create_target>'
        )

    def test_create_target_with_ssh_credential(self):
        self.gmp.create_target(
            'foo', hosts=['foo'], port_list_id='pl1', ssh_credential_id='c1'
        )

        self.connection.send.has_been_called_with(
            '<create_target>'
            '<name>foo</name>'
            '<hosts>foo</hosts>'
            '<ssh_credential id="c1"/>'
            '<port_list id="pl1"/>'
            '</create_target>'
        )

    def test_create_target_with_ssh_credential_port(self):
        self.gmp.create_target(
            'foo',
            hosts=['foo'],
            port_list_id='pl1',
            ssh_credential_id='c1',
            ssh_credential_port=123,
        )

        self.connection.send.has_been_called_with(
            '<create_target>'
            '<name>foo</name>'
            '<hosts>foo</hosts>'
            '<ssh_credential id="c1">'
            '<port>123</port>'
            '</ssh_credential>'
            '<port_list id="pl1"/>'
            '</create_target>'
        )

    def test_create_target_with_smb_credential_id(self):
        self.gmp.create_target(
            'foo', hosts=['foo'], port_list_id='pl1', smb_credential_id='c1'
        )

        self.connection.send.has_been_called_with(
            '<create_target>'
            '<name>foo</name>'
            '<hosts>foo</hosts>'
            '<smb_credential id="c1"/>'
            '<port_list id="pl1"/>'
            '</create_target>'
        )

    def test_create_target_with_esxi_credential_id(self):
        self.gmp.create_target(
            'foo', hosts=['foo'], port_list_id='pl1', esxi_credential_id='c1'
        )

        self.connection.send.has_been_called_with(
            '<create_target>'
            '<name>foo</name>'
            '<hosts>foo</hosts>'
            '<esxi_credential id="c1"/>'
            '<port_list id="pl1"/>'
            '</create_target>'
        )

    def test_create_target_with_snmp_credential_id(self):
        self.gmp.create_target(
            'foo', hosts=['foo'], port_list_id='pl1', snmp_credential_id='c1'
        )

        self.connection.send.has_been_called_with(
            '<create_target>'
            '<name>foo</name>'
            '<hosts>foo</hosts>'
            '<snmp_credential id="c1"/>'
            '<port_list id="pl1"/>'
            '</create_target>'
        )

    def test_create_target_with_alive_tests(self):
        self.gmp.create_target(
            'foo',
            hosts=['foo'],
            port_list_id='pl1',
            alive_test=AliveTest.ICMP_PING,
        )

        self.connection.send.has_been_called_with(
            '<create_target>'
            '<name>foo</name>'
            '<hosts>foo</hosts>'
            '<alive_tests>ICMP Ping</alive_tests>'
            '<port_list id="pl1"/>'
            '</create_target>'
        )

    def test_create_target_invalid_alive_tests(self):
        with self.assertRaises(InvalidArgumentType):
            self.gmp.create_target(
                'foo', hosts=['foo'], port_list_id='pl1', alive_test='foo'
            )

    def test_create_target_with_reverse_lookup_only(self):
        self.gmp.create_target(
            'foo', hosts=['foo'], port_list_id='pl1', reverse_lookup_only=True
        )

        self.connection.send.has_been_called_with(
            '<create_target>'
            '<name>foo</name>'
            '<hosts>foo</hosts>'
            '<reverse_lookup_only>1</reverse_lookup_only>'
            '<port_list id="pl1"/>'
            '</create_target>'
        )

        self.gmp.create_target(
            'foo', hosts=['foo'], port_list_id='pl1', reverse_lookup_only=False
        )

        self.connection.send.has_been_called_with(
            '<create_target>'
            '<name>foo</name>'
            '<hosts>foo</hosts>'
            '<reverse_lookup_only>0</reverse_lookup_only>'
            '<port_list id="pl1"/>'
            '</create_target>'
        )

    def test_create_target_with_reverse_lookup_unify(self):
        self.gmp.create_target(
            'foo', hosts=['foo'], port_list_id='pl1', reverse_lookup_unify=True
        )

        self.connection.send.has_been_called_with(
            '<create_target>'
            '<name>foo</name>'
            '<hosts>foo</hosts>'
            '<reverse_lookup_unify>1</reverse_lookup_unify>'
            '<port_list id="pl1"/>'
            '</create_target>'
        )

        self.gmp.create_target(
            'foo', hosts=['foo'], port_list_id='pl1', reverse_lookup_unify=False
        )

        self.connection.send.has_been_called_with(
            '<create_target>'
            '<name>foo</name>'
            '<hosts>foo</hosts>'
            '<reverse_lookup_unify>0</reverse_lookup_unify>'
            '<port_list id="pl1"/>'
            '</create_target>'
        )

    def test_create_target_with_port_range(self):
        self.gmp.create_target('foo', hosts=['foo'], port_range='bar')

        self.connection.send.has_been_called_with(
            '<create_target>'
            '<name>foo</name>'
            '<hosts>foo</hosts>'
            '<port_range>bar</port_range>'
            '</create_target>'
        )

    def test_create_target_with_port_list_id(self):
        self.gmp.create_target('foo', hosts=['foo'], port_list_id='pl1')

        self.connection.send.has_been_called_with(
            '<create_target>'
            '<name>foo</name>'
            '<hosts>foo</hosts>'
            '<port_list id="pl1"/>'
            '</create_target>'
        )

    def test_create_target_without_ports(self):
        with self.assertRaises(RequiredArgument):
            self.gmp.create_target('foo', hosts=['foo'])
