import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Notify', '0.7')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify
import time;


APPINDICATOR_ID = 'myappindicator'
task_list=['Dashboard-api','report-api','Dashboard-ui','report-ui']

def main():
    
    Notify.init("myapp_name")
    n = Notify.Notification.new("Time Tracker", "Started")
    n.show()
    
    def on_clicked(widget,menu):
        n = Notify.Notification.new("Time Tracker", "Started Tracking")
        #n.show()
        print "Workied"
        """for item in menu:
            print item.get_labels()
            item.deselect()
            
        menu.get_active().name()"""
        
        """if widget.get_sensitive():
            widget.set_sensitive(False)
        else:
            widget.set_sensitive(True)"""
        #print "STRING TARGET: %s" % selection_data
        """try:
            while True:
                n = Notify.Notification.new("Time Tracker", "Tracking-")
                n.show()
                time.sleep(60)
        except KeyboardInterrupt:
            print('Manual break by user')
        
        print b"""
        
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, 'whatever', appindicator.IndicatorCategory.APPLICATION_STATUS)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    
    menu = gtk.Menu()
    radiomenuitem1 = gtk.RadioMenuItem(label="RadioMenuItem 1")
    count = 0
    for i in task_list:
        if count == 0:
            
            radiomenuitem2 = gtk.RadioMenuItem(label=i, group=radiomenuitem1)
        else:
            radiomenuitem2 = gtk.RadioMenuItem(label=i, group=radiomenuitem1)
            
        radiomenuitem2.connect("activate", on_clicked,menu)
        menu.append(radiomenuitem2)
        count = count + 1
    
    
    menu.show_all()
    indicator.set_menu(menu)
    gtk.main()
    
if __name__ == "__main__":
    main()


'''from gi.repository import GObject
from gi.repository import Notify

class MyClass(GObject.Object):
    def __init__(self):

        super(MyClass, self).__init__()
        # lets initialise with the application name
        Notify.init("myapp_name")

    def send_notification(self, title, text, file_path_to_icon=""):

        n = Notify.Notification.new(title, text, file_path_to_icon)
        n.show()

my = MyClass()
my.send_notification("this is a title", "this is some text")'''