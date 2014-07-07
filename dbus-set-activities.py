#!/usr/bin/env python3
# This file is /home/me/test-dbus.py
# Remember to make it executable if you want dbus to launch it
# It works with both Python2 and Python3

from gi.repository import Gtk
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
import subprocess

class MyDBUSService(dbus.service.Object):
    def __init__(self):
        bus_name = dbus.service.BusName('org.fixscreen', bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, '/org/fixscreen')

    @dbus.service.method('org.fixscreen')
    def setActivities(self, windowId, activities):
        cmd = "xprop -id {} -f _KDE_NET_WM_ACTIVITIES 8s -set _KDE_NET_WM_ACTIVITIES \"{}\"".format(windowId, activities)
        print(cmd)
        subprocess.call(cmd, shell=True)
        # Gtk.main_quit()   # Terminate after running. Daemons don't use this.
        return

DBusGMainLoop(set_as_default=True)
myservice = MyDBUSService()
Gtk.main()
