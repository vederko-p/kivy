
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


# Определение корневого Lyaout'а, на котором будут
# располагаться все остальные виджеты, вынесем в отдельный класс Container,
# для того, чтобы переопределять его свойства и методы.
# Класс Container будет наследовать свойства от класса BoxLayout.
# Экземпляр класса Container будет возвращаться методом build класса
# прилоежния - MyApp.

class Container(BoxLayout):
    pass


class MyApp(App):
    def build(self):
        bl = BoxLayout()
        # Создание кнопок
        button1 = Button(text='Hello')
        button2 = Button(text='World')
        # Размещение кнопок на layout'е
        bl.add_widget(button1)
        bl.add_widget(button2)
        return Container()

    # BoxLayout распределяет пространство между детьми поровну.


if __name__ == '__main__':
    MyApp().run()
