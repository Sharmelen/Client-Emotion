#!/usr/bin/python
# -*- coding: utf-8 -*-

import gi
import sys
import os
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

import configparser

class Example:

    def __init__(self):

        self.gladefile = "GUI_emotionAPI.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)
        window = self.builder.get_object("winMain")
        #window.show_all()
        self.set_window("winMain")

    def set_window(self,win):
        self.window = self.builder.get_object(win)
        self.window.show_all()

    def main(self):
        Gtk.main()

    def on_window_destroy(self,*args):
        Gtk.main_quit()

    def on_mybutton_selection_changed(self, widget):

        item_input_URL = self.builder.get_object("input_URL")
        var_input_ipAddress = item_input_URL.get_text()
        sizeof_ipAddress = sys.getsizeof(var_input_ipAddress)

        filepath = widget.get_file().get_path()
        f = open( "myConfig.ini", 'w' )
        f.write( '[myVars]'+ '\n' )
        f.write( 'globalFilepath = ' + filepath + '\n' )

        if sizeof_ipAddress == 49 or sizeof_ipAddress == 68: #68, 49 equals null
            f.write( 'ip_address = http://0.0.0.0:5000' + '\n' )
        else:
            f.write( 'ip_address = '+var_input_ipAddress + '\n' )
        f.close()

        btn_proceed_sensitivity = self.builder.get_object("btn_proceed")
        #print(filepath.lower().endswith(('.jpg' ,'.jpeg','.png')))

        if filepath.lower().endswith(('.jpg' ,'.jpeg','.png')) is True:
            print("Filepath : "+ filepath+ '\n')
            btn_proceed_sensitivity.set_sensitive(True)
        else:
            x.window.hide_on_delete()
            btn_proceed_sensitivity.set_sensitive(False)
            print("Opening Error Message"+ '\n')
            x.set_window("errorWin")


    def btn_proceed_script(self,widget):
        var_tog_internet = self.builder.get_object("tog_internet")
        var_tog_local = self.builder.get_object("tog_local")

        btn_proceed_sensitivity = self.builder.get_object("btn_proceed")

        if var_tog_internet.get_active() == True:
            item_input_internet = self.builder.get_object("input_internet")
            item_input_URL = self.builder.get_object("input_URL")
            var_input_urlAddress = item_input_internet.get_text() #get http link
            var_input_ipAddress = item_input_URL.get_text()

            sizeof_ipAddress = sys.getsizeof(var_input_ipAddress)
            sizeof_urlAddress = sys.getsizeof(var_input_urlAddress)

            if sizeof_urlAddress == 49:
                x.window.hide_on_delete()
                print("Opening Error Message"+ '\n')
                x.set_window("errorWin2")

            f = open( "myConfig.ini", 'w' )
            f.write( '[myVars]'+ '\n' )
            f.write( 'globalFilepath = ' + var_input_urlAddress + '\n' )

            if sizeof_ipAddress == 49 or sizeof_ipAddress == 68:
                f.write( 'ip_address = http://0.0.0.0:5000' + '\n' )
            else:
                f.write( 'ip_address = '+var_input_ipAddress + '\n' )
            f.close()
            var_tog_internet.set_active(False)


        os.system('python3 client.py')

        print("Runing Script..")
        config = configparser.ConfigParser()
        config.read("myConfig.ini")
        get_ipAddress = config.get("myVars", "ip_address")
        get_filepath = config.get("myVars", "globalFilepath")

        print ("IP Address : " + get_ipAddress)
        print ("Filepath : " + get_filepath+ '\n')

        #os.system('python3 client.py')
        btn_proceed_sensitivity = self.builder.get_object("btn_proceed")
        btn_proceed_sensitivity.set_sensitive(False)

    def btn_back(self,widget):
        x.window.hide_on_delete()
        print("Opening Main Window"+ '\n')
        x.set_window("winMain")

    def on_internet_toggled(self, button):
        var_tog_local = self.builder.get_object("tog_local")
        var_input_local = self.builder.get_object("file_image")
        var_tog_internet = self.builder.get_object("tog_internet")
        var_input_internet = self.builder.get_object("input_internet")
        var_btn_proceed = self.builder.get_object("btn_proceed")

        if button.get_active():
            var_input_internet.set_sensitive(True)
            var_tog_local.set_active(False)
            var_btn_proceed.set_sensitive(True)
        else:
            var_tog_local.set_active(False)
            var_input_local.set_sensitive(False)
            var_input_internet.set_sensitive(False)
            var_btn_proceed.set_sensitive(False)

    def on_local_toggled(self, button):
        var_tog_local = self.builder.get_object("tog_local")
        var_input_local = self.builder.get_object("file_image")
        var_tog_internet = self.builder.get_object("tog_internet")
        var_input_internet = self.builder.get_object("input_internet")

        if button.get_active():
            var_input_local.set_sensitive(True)
            var_tog_internet.set_active(False)
        else:
            var_tog_internet.set_active(False)
            var_input_internet.set_sensitive(False)
            var_input_local.set_sensitive(False)



x = Example()
x.main()
