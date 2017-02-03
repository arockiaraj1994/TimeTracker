import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Notify', '0.7')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify
import time;

APPINDICATOR_ID = 'myappindicator'


class CheckNAS: 
    def __init__(self): 
      self.ind =  appindicator.Indicator.new(APPINDICATOR_ID, 'whatever', appindicator.IndicatorCategory.APPLICATION_STATUS)
      self.ind.set_status (appindicator.IndicatorStatus.ACTIVE)
      self.ind.set_attention_icon("icon1")
      self.ind.set_icon("icon2")
      self.menu_setup()

    def menu_setup(self):
      self.quit_item = gtk.MenuItem("QUIT") 
      self.quit_item.connect("activate",self.sensitive)
      self.quit_item.show()
      self.menu.append(self.quit_item)

    def sensitive(self,widget):
      if widget.get_sensitive():
        widget.set_sensitive(False)
      else:
        widget.set_sensitive(True)
    
    
    
if __name__ == "__main__":
    CheckNAS()