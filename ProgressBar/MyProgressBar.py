from kivy.clock import Clock
from kivy.uix.progressbar import ProgressBar


# https://stackoverflow.com/questions/52186990/progress-bar-in-kivy-cant-update-using-loop
class MyProgressBar(ProgressBar):
    def __init__(self, *args, **kwargs):
        super(MyProgressBar, self).__init__(*args, **kwargs)
        # self.update_bar_trigger = Clock.create_trigger(self.update_bar)
        # self.update_bar_trigger = Clock.create_trigger(lambda dt: self.update_bar(), 1)
        # Clock.schedule_once(self.update_bar)

    def update_bar(self, step):
        if self.value <= 100:
            self.value += step

