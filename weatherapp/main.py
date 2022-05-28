# <a target="_blank" href="https://icons8.com/icon/1MUqfGWx3fZS/partly-cloudy-day">Partly Cloudy Day</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>

from kivy.core.window import Window

Window.size = (350, 450)
city_helper ="""
MDTextField:
    hint_text: "Enter city name"
    helper_text: "eg: Columbus or Chicago,us"
    helper_text_mode: "on_focus"
    pos_hint: {'center_x':0.3,'center_y':0.9}
    size_hint_x: None
    width:400

    mode:"fill"


"""
# navigation_helper = """
# Screen:
#     MDNavigationLayout:
#         ScreenManager:
#             Screen:
#                 BoxLayout:
#                     orientation: 'vertical'
#                     MDToolbar:
#                         title: "Navigation Drawer"
#                         elevation: 10
#                         left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
#                     Widget:
#         MDNavigationDrawer:
#             id: nav_drawer
#"""
# <a target="_blank" href="https://icons8.com/icon/1MUqfGWx3fZS/partly-cloudy-day">Partly Cloudy Day</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>

from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.screen import MDScreen
from kivy.uix.image import Image
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from pyowm import OWM
from kivy.lang import Builder


#5386fe8b412f65c8fe185582a8a170a7


class Weatherapp(MDApp):

    def build(self):
        #screen = Builder.load_string(navigation_helper)
        screen = MDScreen()
        i1 = Image(source='./things/images/icons8-partly-cloudy-day-48.png',pos_hint={'center_x':0.5,'center_y':0.75})
        self.l1 = MDLabel(text='', pos_hint={'center_x': 0.7, 'center_y': 0.8},font_style='H4')
        self.l2 = MDLabel(text='Weather Status:', pos_hint={'center_x': 0.7, 'center_y': 0.5})
        self.l3 = MDLabel(text='Wind Speed: Wind Gust Speed:', pos_hint={'center_x': 0.7, 'center_y': 0.6})
        self.l4 = MDLabel(text='Humidity:', pos_hint={'center_x': 0.7, 'center_y': 0.7})
        self.l5 = MDLabel(text='Temperature: Feels_Like:', pos_hint={'center_x': 0.7, 'center_y': 0.4})
        self.city = Builder.load_string(city_helper)
        b1 = MDRectangleFlatButton(text='Search',pos_hint={'center_x':0.7,'center_y':0.9},on_release=self.showresults)
        screen.add_widget(self.city)
        screen.add_widget(self.l1)
        screen.add_widget(i1)
        screen.add_widget(b1)
        screen.add_widget(self.l2)
        screen.add_widget(self.l3)
        screen.add_widget(self.l4)
        screen.add_widget(self.l5)
        return screen
    def showresults(self,obj):
        try:
            owm = OWM('5386fe8b412f65c8fe185582a8a170a7')
            mgr = owm.weather_manager()

            # Search for current weather in London (Great Britain) and get details
            observation = mgr.weather_at_place(self.city.text)
            w = observation.weather
            a = str(self.city.text)
            self.l1.text = a.capitalize() 
            self.city.text = ''
            self.l2.text = f'Weather Status: {w.detailed_status}'
            self.l3.text = f'Wind Speed: {w.wind()["speed"]}\n Wind Degree: {w.wind()["deg"]} '
            self.l4.text = f'Humidity: {w.humidity}'
            self.l5.text = f'Temperature: {w.temperature("fahrenheit")["temp"]},\n Feels_Like:{w.temperature("fahrenheit")["feels_like"]}'
        except:
            self.dialog = MDDialog(title='invalid input',
                                   text='invaild input , format is different , or we might be expercing problems to test that type Fort Mill,us and press search if it does not work contact stuffpython8@gmail.com', size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                            ]
                                   )
            self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

Weatherapp().run()
