from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition
from kivy.lang import Builder
from touch import TouchBox
import time
#from client_side_script import sendMessageToServer
import _thread as thread
ui  = Builder.load_string("""
<TerminalUsageTimeSetterBox>:
	id:terminal_usage_time_setter
	orientation:"vertical"
	MDBoxLayout:
		orientation:"vertical"
		MDBoxLayout:
			size_hint_y:None
			height:"90dp"
			padding:"0dp", "10dp"
			spacing:10
			Widget:
			FifteenMinutesSetButtonBox:
				root:terminal_usage_time_setter
				id:fifteen_minutes_box
				radius:[10, 10, 10, 10]
				size_hint:None, None
				size:"100dp", "70dp"
				md_bg_color:[0, 0, 0, 1]
				orientation:"vertical"
				MDBoxLayout:
					MDLabel:
						text:"15"
						font_size:"30dp"
						text_size:self.size
						halign:"center"
						valign:"middle"
						color:[1, 1, 1, 1]
				MDBoxLayout:
					size_hint_y:None
					height:"30dp"
					MDLabel:
						text:"Minutes"
						text_size:self.size
						halign:"center"
						valign:"middle"
						color:[1, 1, 1, 1]
			ThirtyMinutesSetButtonBox:
				root:terminal_usage_time_setter
				id:thirty_minutes_box
				radius:[10, 10, 10, 10]
				size_hint:None, None
				size:"100dp", "70dp"
				md_bg_color:[0, 0, 0, 1]
				orientation:"vertical"
				MDBoxLayout:
					MDLabel:
						text:"30"
						font_size:"30dp"
						text_size:self.size
						halign:"center"
						valign:"middle"
						color:[1, 1, 1, 1]
				MDBoxLayout:
					size_hint_y:None
					height:"30dp"
					MDLabel:
						text:"Minutes"
						text_size:self.size
						halign:"center"
						valign:"middle"
						color:[1, 1, 1, 1]
			OneHourSetButtonBox:
				root:terminal_usage_time_setter
				id:one_hour_box
				radius:[10, 10, 10, 10]
				size_hint:None, None
				size:"100dp", "70dp"
				md_bg_color:[0, 0, 0, 1]
				orientation:"vertical"
				MDBoxLayout:
					MDLabel:
						text:"1"
						font_size:"30dp"
						text_size:self.size
						halign:"center"
						valign:"middle"
						color:[1, 1, 1, 1]
				MDBoxLayout:
					size_hint_y:None
					height:"30dp"
					MDLabel:
						text:"Hour"
						text_size:self.size
						halign:"center"
						valign:"middle"
						color:[1, 1, 1, 1]
			Widget:
		TimeRunningBox:
			id:time_running_box
			size_hint_y:None
			height:"100dp"
			padding:"20dp", "0dp"
			MDBoxLayout:
				md_bg_color:[190/float(255), 190/float(255), 190/float(255), 1]
				radius:[10, 10, 10, 10]
				MDLabel:
					id:count_down_time_label
					text:"00:00:00"
					font_size:"50dp"
					text_size:self.size
					halign:"center"
					valign:"middle"
					color:[0, 0, 0, 1]
		Widget:
<TerminalOneScreen>:
	name:"terminal_one"
	id:terminal_one
	MDBoxLayout:
		orientation:"vertical"
		TerminalUsageTimeSetterBox:
			id:terminal_usage_time_setter_box
		MDBoxLayout:
			size_hint_y:None
			height:"50dp"
			padding:5
			StartRunningTime:
				root:terminal_one
				id:run_time_go_button
				md_bg_color:[1, 0/float(255), 0/float(255), 1]
				radius:[20, 20, 20, 20]
				MDLabel:
					text:"Start"
					text_size:self.size
					halign:"center"
					valign:"middle"
					bold:True
					color:[1, 1, 1, 1]
<TerminalTwoScreen>:
	name:"terminal_two"
	id:terminal_two
	MDBoxLayout:
		orientation:"vertical"
		TerminalUsageTimeSetterBox:
			id:terminal_usage_time_setter_box
		MDBoxLayout:
			size_hint_y:None
			height:"50dp"
			padding:5
			StartRunningTime:
				id:run_time_go_button
				root:terminal_two
				md_bg_color:[1, 0/float(255), 0/float(255), 1]
				radius:[20, 20, 20, 20]
				MDLabel:
					text:"Start"
					text_size:self.size
					halign:"center"
					valign:"middle"
					bold:True
					color:[1, 1, 1, 1]
<MainBox>:
	id:main_box
	orientation:"vertical"
	MDBoxLayout:
		size_hint_y:None
		height:"100dp"
		md_bg_color:[0/float(255), 255/float(255), 154/float(255), 1]
	MDBoxLayout:
		md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
		orientation:"vertical"
		MDBoxLayout:
			orientation:"vertical"
			MDBoxLayout:
				size_hint_y:None
				height:"120dp"
				padding:"5dp", "10dp"
				spacing:10
				TerminalOneButton:
					id:terminal_one_button
					root:main_box
					md_bg_color:[0, 154/float(255), 255/float(255), 1]
					radius:[10, 10, 10, 10]
					orientation:"vertical"
					MDBoxLayout:
						Widget:
						MDIconButton:
							size_hint:None, None
							size:"50dp", "50dp"
							icon:"monitor"
							user_font_size:"40dp"
						Widget:
					MDBoxLayout:
						MDLabel:
							text:"Terminal One"
							text_size:self.size
							halign:"center"
							valign:"middle"
							color:[1, 1, 1, 1]
				TerminalTwoButton:
					id:terminal_two_button
					root:main_box
					md_bg_color:[190/float(255), 190/float(255), 190/float(255), 1]
					radius:[10, 10, 10, 10]
					orientation:"vertical"
					MDBoxLayout:
						Widget:
						MDIconButton:
							size_hint:None, None
							size:"50dp", "50dp"
							icon:"monitor"
							user_font_size:"40dp"
						Widget:
					MDBoxLayout:
						MDLabel:
							text:"Terminal Two"
							text_size:self.size
							halign:"center"
							valign:"middle"
							color:[1, 1, 1, 1]
			MDBoxLayout:
				ScreenManager:
					id:terminals_screen_manager
					TerminalOneScreen:
					TerminalTwoScreen:
		MDBoxLayout:
			size_hint_y:None
			height:"60dp"
			spacing:5
			padding:10
			RestartTerminalButtonBox:
				radius:[10, 10, 10, 10]
				root:main_box
				md_bg_color:[0, 0, 0, 1]
				MDLabel:
					text:"Restart"
					text_size:self.size
					halign:"center"
					valign:"middle"
					color:[1, 1, 1, 1]
			ShutDownTerminalButtonBox:
				radius:[10, 10, 10, 10]
				root:main_box
				md_bg_color:[0, 0, 0, 1]
				MDLabel:
					text:"Shut down"
					text_size:self.size
					halign:"center"
					valign:"middle"
					color:[1, 1, 1, 1]
""")
class FifteenMinutesSetButtonBox(TouchBox):
	def respondToTouch(self):
		self.root.turnAllTimeSetterButtonsBlack()
		self.md_bg_color = [0, 154/float(255), 255/float(255), 1]
		self.root.ids.time_running_box.minutes =+ 15
	    #self.root.countDown(15)
class ThirtyMinutesSetButtonBox(TouchBox):
	def respondToTouch(self):
		self.root.turnAllTimeSetterButtonsBlack()
		self.md_bg_color = [0, 154/float(255), 255/float(255), 1]
		self.root.ids.time_running_box.minutes =+ 30
		#self.root.countDown(30)
class OneHourSetButtonBox(TouchBox):
	def respondToTouch(self):
		self.root.turnAllTimeSetterButtonsBlack()
		self.md_bg_color = [0, 154/float(255), 255/float(255), 1]
		self.root.countDown(60)
		self.root.ids.time_running_box.hours += 1
		self.root.ids.count_down_time_label.text = "0" + str(self.root.ids.time_running_box.hours) + ":00:00"
		self.root.ids.time_running_box.hours =+ 1
class TerminalUsageTimeSetterBox(MDBoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.count_down_time = 0
	def turnAllTimeSetterButtonsBlack(self):
		self.ids.fifteen_minutes_box.md_bg_color = [0, 0, 0, 1]
		self.ids.thirty_minutes_box.md_bg_color = [0, 0, 0, 1]
		self.ids.one_hour_box.md_bg_color = [0, 0, 0, 1]
	def countDown(self, minutes):
		self.count_down_time += minutes
		#self.ids.count_down_time_label.text = 
	def formatOneToNine(self, digit):
		if digit < 10:
			return "0" + str(digit)
		else:
			return str(digit)
	def countDownSeconds(self, seconds, minutes, hours):
		minutes = self.formatOneToNine(minutes)
		hours = self.formatOneToNine(hours)
		while seconds > 0:
			time.sleep(1)
			seconds = seconds - 1
			if seconds < 10:
				self.ids.count_down_time_label.text = hours + ":" + minutes + ":0" + str(seconds)
			else:
				self.ids.count_down_time_label.text =  hours + ":" + minutes + ":" + str(seconds)
	def countDownMinutes(self, minutes, string_hour):
		while minutes > 0:
			time.sleep(1)
			minutes = minutes - 1
			if minutes < 10:
				string_minutes  = "0" + str(minutes)
			else:
				string_minutes = str(minutes)
			self.ids.count_down_time_label.text = string_hour + ":" + string_minutes + ":" + str(59)
			self.countDownSeconds(59, string_minutes, string_hour)
class TimeRunningBox(MDBoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.hours = 0
		self.minutes = 0
		self.seconds = 60
class TerminalOneScreen(MDScreen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.ip_address = "192.168.0.23"
class TerminalTwoScreen(MDScreen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.ip_address = "192.168.0.24"
class TerminalOneButton(TouchBox):
	def respondToTouch(self):
		self.root.turnTerminalButtonsGrey()
		self.md_bg_color = [0, 154/float(255), 255/float(255), 1]
		self.root.ids.terminals_screen_manager.transition = SlideTransition(direction = "right")
		self.root.ids.terminals_screen_manager.current = "terminal_one"
class TerminalTwoButton(TouchBox):
	def respondToTouch(self):
		self.root.turnTerminalButtonsGrey()
		self.md_bg_color = [0, 154/float(255), 255/float(255), 1]
		self.root.ids.terminals_screen_manager.transition = SlideTransition(direction = "left")
		self.root.ids.terminals_screen_manager.current = "terminal_two"
class StartRunningTime(TouchBox):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.enable = True
	def respondToTouch(self):
		seconds = self.root.ids.terminal_usage_time_setter_box.ids.time_running_box.seconds
		minutes = self.root.ids.terminal_usage_time_setter_box.ids.time_running_box.minutes
		hours = self.root.ids.terminal_usage_time_setter_box.ids.time_running_box.hours
		if self.enable:
			thread.start_new_thread(self.root.ids.terminal_usage_time_setter_box.countDownSeconds, (seconds, minutes, hours))
			#self.root.ids.terminal_usage_time_setter_box.time_running_box. = 
class RestartTerminalButtonBox(TouchBox):
	def respondToTouch(self):
		pass
		#thread.start_new_thread(sendMessageToServer, (b'Restart', ))
class ShutDownTerminalButtonBox(TouchBox):
	def respondToTouch(self):
		pass 
		#thread.start_new_thread(sendMessageToServer, (b'Shutdown', ))
class MainBox(MDBoxLayout):
	def turnTerminalButtonsGrey(self):
		self.ids.terminal_one_button.md_bg_color = [190/float(255), 190/float(255), 190/float(255), 1]
		self.ids.terminal_two_button.md_bg_color = [190/float(255), 190/float(255), 190/float(255), 1]
class TerminalTimerApp(MDApp):
	def build(self):
		root = MainBox()
		return root
if __name__ == "__main__":
	TerminalTimerApp().run()