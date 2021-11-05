
   
import rumps
class PomodoroApp(object):
    def __init__(self):
        self.config = {
            "app_name": "SmartBar",
            "start1": "Start a Long Break timer(15 min)",
            "start2": "Start a Short Break timer(5 min)",
            "start3": "Start a Academic hour timer(45 min)",
            "pause": "Pause Timer",
            "continue": "Continue Timer",
            "stop": "Stop Timer",
            "break_message": "Time is up! Take a break :)",
            "interval1": 900,
            "interval2": 300,
            "interval3": 2700,
        }
        self.app = rumps.App(self.config["app_name"])
        self.timer = rumps.Timer(self.on_tick, 1)
        self.interval1 = self.config["interval1"]
        self.interval2 = self.config["interval2"]
        self.interval3 = self.config["interval3"]
        self.set_up_menu()
        self.start_pause_button2 = rumps.MenuItem(title=self.config["start2"], callback=self.start_timer2)
        self.start_pause_button1 = rumps.MenuItem(title=self.config["start1"], callback=self.start_timer1)
        self.start_pause_button3 = rumps.MenuItem(title=self.config["start3"], callback=self.start_timer3)
        self.stop_button = rumps.MenuItem(title=self.config["stop"], callback=None)
        self.app.menu = [self.start_pause_button2, self.start_pause_button1, self.start_pause_button3, self.stop_button]
    def set_up_menu(self):
        self.timer.stop()
        self.timer.count = 0
        self.app.title = '◎'
    def on_tick(self, sender):
        time_left = sender.end - sender.count
        mins = time_left // 60 if time_left >= 0 else time_left // 60 + 1
        secs = time_left % 60 if time_left >= 0 else (-1 * time_left) % 60
        if mins == 0 and time_left < 0:
            rumps.notification(title=self.config["app_name"], subtitle=self.config["break_message"], message='')
            self.stop_timer()
            self.stop_button.set_callback(None)
            exit()
            exit()
        else:
            self.stop_button.set_callback(self.stop_timer)
            self.app.title = 'Timer: {:2d}:{:02d} left'.format(mins, secs)
        sender.count += 1
    def start_timer1(self, sender):
        self.start_pause_button2.set_callback(None)
        self.start_pause_button3.set_callback(None)
        if sender.title.lower().startswith(("start", "continue")):
            if sender.title == self.config["start1"]:
                self.timer.count = 0
                self.timer.end = self.interval1
            sender.title = self.config["pause"]
            self.timer.start()
        else:
            sender.title = self.config["continue"]
            self.timer.stop()
    def start_timer2(self, sender):
        self.start_pause_button1.set_callback(None)
        self.start_pause_button3.set_callback(None)
        if sender.title.lower().startswith(("start", "continue")):
            if sender.title == self.config["start2"]:
                self.timer.count = 0
                self.timer.end = self.interval2
            sender.title = self.config["pause"]
            self.timer.start()
        else:
            sender.title = self.config["continue"]
            self.timer.stop()
    def start_timer3(self, sender):
        self.start_pause_button1.set_callback(None)
        self.start_pause_button2.set_callback(None)
        if sender.title.lower().startswith(("start", "continue")):
            if sender.title == self.config["start3"]:
                self.timer.count = 0
                self.timer.end = self.interval3
            sender.title = self.config["pause"]
            self.timer.start()
        else:
            sender.title = self.config["continue"]
            self.timer.stop()
    def stop_timer(self, sender):
        self.set_up_menu()
        self.timer.stop()
        self.stop_button.set_callback(None)
        self.start_pause_button1.set_callback(self.start_timer1)
        self.start_pause_button2.set_callback(self.start_timer2)
        self.start_pause_button3.set_callback(self.start_timer3)
        self.start_pause_button1.title = self.config["start1"]
        self.start_pause_button2.title = self.config["start2"]
        self.start_pause_button3.title = self.config["start3"]
    def run(self):
        self.app.run()
if __name__ == '__main__':
    app = PomodoroApp()
    app.run()
