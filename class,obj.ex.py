class F15:
    def light(self):
        print("ok switching on light")
    def fan(self,speed):
        print("fan is on and the speed is",speed)
        self.s=speed
    def cpu(self):
        print("powering on the system")
        print(self.s)
objectname=F15()
objectname.light()
objectname.fan(5)
objectname.cpu()
