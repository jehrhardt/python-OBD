########################################################################
#                                                                      #
# python-OBD: A python OBD-II serial module derived from pyobd         #
#                                                                      #
# Copyright 2004 Donour Sizemore (donour@uchicago.edu)                 #
# Copyright 2009 Secons Ltd. (www.obdtester.com)                       #
# Copyright 2014 Brendan Whitfield (bcw7044@rit.edu)                   #
#                Jan Ehrhardt (http://derjan.io)
#                                                                      #
########################################################################
#                                                                      #
# trace.py                                                             #
#                                                                      #
# This file is part of python-OBD (a derivative of pyOBD)              #
#                                                                      #
# python-OBD is free software: you can redistribute it and/or modify   #
# it under the terms of the GNU General Public License as published by #
# the Free Software Foundation, either version 2 of the License, or    #
# (at your option) any later version.                                  #
#                                                                      #
# python-OBD is distributed in the hope that it will be useful,        #
# but WITHOUT ANY WARRANTY; without even the implied warranty of       #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        #
# GNU General Public License for more details.                         #
#                                                                      #
# You should have received a copy of the GNU General Public License    #
# along with python-OBD.  If not, see <http://www.gnu.org/licenses/>.  #
#                                                                      #
########################################################################

from async import Async

def trace_obd:
    conn = Async()
    watch_supported_commands(conn)
    conn.start()

def watch_supported_commands(conn):
    commands = {} # get list of supported commands
    for c in commands:
        conn.watch(c, callback=print_response) # add command to print method

def print_command(c):
    def print_response(resp):
        print(c + ':' + resp.value)
    return print_response
