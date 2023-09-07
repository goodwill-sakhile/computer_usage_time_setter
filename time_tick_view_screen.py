from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
Builder.load_string("""
<CountingTimerScreen>:
    name:"counting_time"
    MDBoxLayout:
        orientation:"vertical"
        MDBoxLayout:
            size_hint_y:None
            height:"60dp"
            padding:"0dp", "10dp"
            Widget:
            MDBoxLayout:
                size_hint:None, None
                size:"350dp", "40dp"
                MDBoxLayout:
                    md_bg_color:[0, 0, 0, 1]
                    size_hint_x:None
                    radius:[20, 20, 20, 20]
                    width:"60dp"
                    MDLabel:
                        text:"02:00"
                        text_size:self.size
                        halign:"center"
                        valign:"middle"
                        color:[1, 1, 1, 1]
                Widget:
            Widget:
        Widget:
""")
class CountingTimerScreen(MDScreen):
    pass
class Test(MDApp):
    def build(self):
        count = CountingTimerScreen()
        m = ScreenManager()
        m.add_widget(count)
        return m
if __name__ == "__main__":
    Test().run()