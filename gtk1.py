import pygtk
pygtk.require('2.0')
import gtk

class WelcomeMsg:
    def __init__(self):
       window = gtk.Window()
       window.set_title('Welcome')
       window.set_border_width(10)
       window.set_size_request(200, 100)
       window.connect("destroy", self.quit)

       vbox = gtk.Vbox()
       window.add(vbox)

       button = gtk.Button('Press Me!')
       button.connect("Clique aqui", self.printMessage, "Welcome...")

       vbox.pack_start(button, True, True, 0)

       button = gtk.Button("Close")
       button.connect("Clique nele", self.quit)
       vbox.pack_start(button, True, True, 5)

       window.show_all()

    def printMessage(self, widget, data):
        print data

    def quit(self, widget):
        gtk.main_quit()

    def  main(self):
       gtk.main()

if __name__ =='__main__':
    p = WelcomeMsg()
    p.main()
