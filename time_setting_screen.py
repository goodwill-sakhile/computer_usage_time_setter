from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
Builder.load_string("""
<TimeSettingScreen>:
    name:"time_setting_screen"
    MDBoxLayout:
        orientation:"vertical"
        spacing:10
        Widget:
        MDBoxLayout:
            size_hint_y:None
            height:"150dp"
            Widget:
            MDBoxLayout:
                size_hint_x:None
                width:"350dp"
                spacing:10
                MDBoxLayout:
                    orientation:"vertical"
                    radius:[10, 10, 10, 10]
                    md_bg_color:[0, 255/float(255), 154/float(255), 1]
                    MDBoxLayout:
                        Widget:
                        MDIconButton:
                            size_hint:None, None
                            size:"40dp", "40dp"
                        Widget:
                    MDLabel:
                        text:"00"
                        text_size:self.size
                        halign:"center"
                        valign:"middle"
                        font_size:"30dp"
                        color:[1, 1, 1, 1]
                    MDBoxLayout:
                        Widget:
                        MDIconButton:
                            size_hint:None, None
                            size:"40dp", "40dp"
                        Widget:
                MDBoxLayout:
                    orientation:"vertical"
                    radius:[10, 10, 10, 10]
                    md_bg_color:[0, 255/float(255), 154/float(255), 1]
                    MDBoxLayout:
                        Widget:
                        MDIconButton:
                            size_hint:None, None
                            size:"40dp", "40dp"
                        Widget:
                    MDLabel:
                        text:"00"
                        text_size:self.size
                        halign:"center"
                        valign:"middle"
                        font_size:"30dp"
                        color:[1, 1, 1, 1]
                    MDBoxLayout:
                        Widget:
                        MDIconButton:
                            size_hint:None, None
                            size:"40dp", "40dp"
                        Widget:
            Widget:
        MDBoxLayout:
            size_hint_y:None
            height:"30dp"
            Widget:
            MDBoxLayout:
                size_hint_x:None
                width:"350dp"
                spacing:5
                MDBoxLayout:
                    MDLabel:
                        text:"hours"
                        text_size:self.size
                        halign:"center"
                        valign:"middle"
                MDBoxLayout:
                    MDLabel:
                        text:"minutes"
                        text_size:self.size
                        halign:"center"
                        valign:"middle"
            Widget:
        MDBoxLayout:
            size_hint_y:None
            height:"60dp"
            padding:5
            Widget:
            MDBoxLayout:
                size_hint_x:None
                width:"350dp"
                radius:[10, 10, 10, 10]
                md_bg_color:[0, 0/float(255), 0/float(255), 1]
                MDLabel:
                    text:"Start Count"
                    text_size:self.size
                    font_size:"20dp"
                    halign:"center"
                    valign:"middle"
                    color:[1, 1, 1, 1]
            Widget:
        Widget:
""")
class TimeSettingScreen(MDScreen):
    pass
