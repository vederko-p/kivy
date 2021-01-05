
from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        return Button(text='Hello world')

    # Метод build обеспечивает на окне приложения наличие какого-либо виджета.
    # По дефолту метод build возвращает экземпляр класса виджет.


if __name__ == '__main__':
    MyApp().run()
