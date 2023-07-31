import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QScrollArea


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Контроль эффективности профилактических мероприятий у беременных высокого риска преэклампсии'
        self.left = 100
        self.top = 100
        self.width = 500
        self.height = 500

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Создание меток и текстовых полей для ввода данных
        self.label1 = QLabel('Инсулин (мкЕД/мл):', self)
        self.label1.move(50, 50)
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(230, 45)
        self.textbox1.resize(200, 25)

        self.label2 = QLabel('Мочевая кислота (мкмоль/л):', self)
        self.label2.move(50, 90)
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(230, 85)
        self.textbox2.resize(200, 25)

        self.label3 = QLabel('С-реактивный белок (мг/л):', self)
        self.label3.move(50, 130)
        self.textbox3 = QLineEdit(self)
        self.textbox3.move(230, 125)
        self.textbox3.resize(200, 25)

        self.label4 = QLabel('Агрегация тромбоцитов \nс коллагеном (%):', self)
        self.label4.move(50, 170)
        self.textbox4 = QLineEdit(self)
        self.textbox4.move(230, 170)
        self.textbox4.resize(200, 25)

        self.label5 = QLabel('ФРП (пг/мл):', self)
        self.label5.move(50, 215)
        self.textbox5 = QLineEdit(self)
        self.textbox5.move(230, 210)
        self.textbox5.resize(200, 25)

        # Создание кнопки для расчета риска
        self.button = QPushButton('Рассчитать', self)
        self.button.move(180, 250)
        self.button.clicked.connect(self.on_click)

        # Создание метки для вывода результата расчета
        self.widget = QWidget(self)
        self.widget.move(40, 280)
        self.widget.resize(400, 200)

        layout = QVBoxLayout(self.widget)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        layout.addWidget(scroll_area)
        scroll_widget = QWidget()
        scroll_area.setWidget(scroll_widget)
        scroll_layout = QVBoxLayout(scroll_widget)
        self.scroll_label = QLabel("")
        self.scroll_label.setAlignment(Qt.AlignLeft)
        self.scroll_label.setWordWrap(True)
        scroll_layout.addWidget(self.scroll_label)

        self.show()

    def on_click(self):
        try:
            # Получение данных из текстовых полей
            insulin = float(self.textbox1.text())
            uric_acid = float(self.textbox2.text())
            crp = float(self.textbox3.text())
            agr_plt = float(self.textbox4.text())
            plgf = float(self.textbox5.text())

            # Расчет риска и вывод результата
            z = 0.012 * insulin + 0.134 * uric_acid + 0.009 * crp + 0.033 * agr_plt - 0.065 * plgf + 0.001
            p = 1 / (1 + pow(2.71828, -z))

            if (p >= 0.38):
                self.scroll_label.setText("""Недостаточная эффективность профилактических мероприятий.
Варианты дальнейших действий:
1. Замена НДАСК* на карбогенопрофилактику, проведение контрольного обследования через 4-6 недель и усиление \
своевременных диагностических мероприятий в отношении ранней диагностики преэклампсии (ведение дневника самоконтроля \
АД, подсчет количества ночных пробуждений для мочеиспускания, СМАД**). 
2. Усиление одного метода другим (добавляем к карбогенопрофилактике + НДАСК, к НДАСК – карбогенопрофилактику), \
проведение контрольного обследования через 4-6 недель и усиление своевременных диагностических мероприятий в \
отношении ранней диагностики преэклампсии (ведение дневника самоконтроля АД, подсчет количества ночных \
пробуждений для мочеиспускания, СМАД). 


* НДАСК - низкие дозы ацетилсалициловой кислоты
** СМАД - суточное мониторирование артериального давления""")
            else:
                self.scroll_label.setText("""Продолжение профилактических мероприятий с контрольным обследованием \
через 8-10 недель.""")

        except ValueError:
            self.scroll_label.setText("Ошибка: пожалуйста, введите числовые значения во все поля")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window... ')