# dgtk.py
#
# Copyright (C) Zach Tibbitts 2006 <zach@collegegeek.org>
# 
# Deluge is free software.
# 
# You may redistribute it and/or modify it under the terms of the
# GNU General Public License, as published by the Free Software
# Foundation; either version 2 of the License, or (at your option)
# any later version.
# 
# dgtk.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with main.py.  If not, write to:
# 	The Free Software Foundation, Inc.,
# 	51 Franklin Street, Fifth Floor
# 	Boston, MA  02110-1301, USA.

import dcommon
import gettext
import pygtk
pygtk.require('2.0')
import gtk
import gtk.glade


## Right now this only supports PyGTK's native 
## tray library.  I will add egg support into
## this class at a later time.
class TrayIcon:
	def __init__(self, parent):
		self.parent = parent
		self.tray = gtk.StatusIcon()
		## uncomment later
		##self.gladefile = dcommon.get_glade("dgtkpopups.glade")
		self.tray.set_from_file(dcommon.get_pixmap("deluge32.png"))
		self.tray.set_tooltip("Deluge Bittorrent Client")
		

class AboutDialog:
	def __init__(self):
		gtk.about_dialog_set_url_hook(dcommon.open_url_in_browser)
		self.abt = gtk.AboutDialog()
		self.abt.set_name(dcommon.PROGRAM_NAME)
		self.abt.set_version(dcommon.PROGRAM_VERSION)
		self.abt.set_website("http://deluge-torrent.org")
		self.abt.set_icon_from_file(dcommon.get_pixmap("deluge32.png"))
		self.abt.set_logo(gtk.gdk.pixbuf_new_from_file(
				dcommon.get_pixmap("deluge256.png")))
	
	def show(self, arg=None):
		self.abt.show_all()
		self.abt.run()
		self.abt.hide_all()

class DelugeColumn(gtk.TreeViewColumn):
	def __init__(self, title=None, renderer=None):
		gtk.TreeViewColumn.__init__(self, title, renderer)
	
	def set_value(self, arg):
		pass
	
	def show(self):
		self.set_visible(True)
	
	def hide(self):
		self.set_visible(False)
		
class TextColumn(DelugeColumn):
	def __init__(self, title=None):
		DelugeColumn.__init__(self, title, gtk.CellRendererText())
	
	def set_value(self, string):
		pass

class ToggleColumn(DelugeColumn):
	def __init__(self, title=None):
		DelugeColumn.__init__(self, title, gtk.CellRendererToggle())
	
	def set_value(self, value):
		pass

class ProgressColumn(DelugeColumn):
	def __init__(self, title=None):
		DelugeColumn.__init__(self, title, gtk.CellRendererProgress())
	
	def set_value(self, progress):
		pass