 #!/usr/bin/env python
import pygtk
pygtk.require('2.0')
import gtk
import webbrowser

class TextEntry:

    def enter_callback_b(self, widget, entry_b):
        entry_text_b = entry_b.get_text()
        query = "http://duckduckgo.com/?q=%s" % entry_text_b.replace(" ", "+")
        webbrowser.open_new_tab(query)
        exit()
        return

    # Main program to draw GUI
    def __init__(self):

        # create a new window
        app_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        app_window.set_size_request(500, 100)
        app_window.set_border_width(10)
        app_window.set_title("Ducky")
        app_window.set_position(gtk.WIN_POS_CENTER_ALWAYS)
        app_window.connect("delete_event", lambda w,e: gtk.main_quit())

        # Set default text in text entry box
        entry_checker_default_b = "Search DuckDuckGo"

        # Text label
        hbox_b = gtk.HBox(False, 0)
        app_window.add(hbox_b) # attach HBox to window

        # Generate text entry box
        entry_b = gtk.Entry()
        entry_b.set_max_length(80)
        entry_b.set_width_chars(60)
        entry_b.connect("activate", self.enter_callback_b, entry_b)
        entry_b.set_text(entry_checker_default_b)
        entry_b.select_region(0, len(entry_b.get_text()))
        entry_b.show()
        hbox_b.pack_start(entry_b, False, False, 0) 

        hbox_b.show()
        app_window.show()
        return

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    TextEntry()
    main()
