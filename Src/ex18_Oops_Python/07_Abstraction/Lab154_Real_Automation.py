from abc import ABC, abstractmethod


class browsermanager:
    @abstractmethod

    def start(self):
        pass
    def stop(self):
        print("Stopping the browser")

class chromebrowser(browsermanager):

    def start(self):
        print("We are starting chrome")

tc=chromebrowser()
tc.start()
tc.stop()