from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from time_setting_screen import TimeSettingScreen
root = Builder.load_string("""
<MainBox>:
    orientation:"vertical"
    md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
    MDBoxLayout:
        size_hint_y:None
        height:"150dp"
        md_bg_color:[0, 0, 0, 1]
        orientation:"vertical"
        MDBoxLayout:
            padding:"10dp", "10dp"
            MDLabel:
                text:"Time_Counter"
                font_size:"25dp"
                text_size:self.size
                halign:"left"
                valign:"top"
                color:[1, 1, 1, 1]
        MDBoxLayout:
            padding:"10dp", "5dp"
            spacing:10
            MDBoxLayout:
                radius:[10, 10, 10, 10]
                md_bg_color:[1, 1, 1, 1]
                MDLabel:
                    text:"Terminal 1"
                    text_size:self.size
                    halign:"center"
                    valign:"middle"
                    color:[0, 0, 0, 1]
            MDBoxLayout:
                radius:[10, 10, 10, 10]
                md_bg_color:[0, 154/float(255), 255/float(255), 1]
                MDLabel:
                    text:"Terminal 2"
                    text_size:self.size
                    halign:"center"
                    valign:"middle"
                    color:[0, 0, 0, 1]
    MDBoxLayout:
        ScreenManager:
            TimeSettingScreen:
""")
class MainBox(MDBoxLayout):
    pass
class TimeUsageApp(MDApp):
    def build(self):
        root = MainBox()
        return root
if __name__ == "__main__":
    TimeUsageApp().run()