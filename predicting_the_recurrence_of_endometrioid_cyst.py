import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Калькулятор риска рецидивирования эндометриоидных кист яичников'
        self.left = 100
        self.top = 100
        self.width = 500
        self.height = 500

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Создание меток и текстовых полей для ввода данных
        self.label1 = QLabel('размер кисты:', self)
        self.label1.move(50, 50)
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(150, 50)
        self.textbox1.resize(200, 25)

        self.label2 = QLabel('Ki-67:', self)
        self.label2.move(50, 90)
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(150, 90)
        self.textbox2.resize(200, 25)

        self.label3 = QLabel('NF-kβ p65z:', self)
        self.label3.move(50, 130)
        self.textbox3 = QLineEdit(self)
        self.textbox3.move(150, 130)
        self.textbox3.resize(200, 25)

        self.label4 = QLabel('СОХ-2:', self)
        self.label4.move(50, 170)
        self.textbox4 = QLineEdit(self)
        self.textbox4.move(150, 170)
        self.textbox4.resize(200, 25)

        # Создание кнопки для расчета риска
        self.button = QPushButton('Рассчитать', self)
        self.button.move(150, 220)
        self.button.clicked.connect(self.on_click)

        # Создание метки для вывода результата расчета
        self.label_result = QLabel('', self)
        self.label_result.move(50, 260)
        self.label_result.resize(400, 100)

        self.show()

    def on_click(self):
        try:
            # Получение данных из текстовых полей
            size_of_cyst = float(self.textbox1.text())
            ki_67 = float(self.textbox2.text())
            nf_kβ_p65z = float(self.textbox3.text())
            soh_2 = float(self.textbox4.text())

            # Расчет риска и вывод результата
            z = 0.11 * size_of_cyst - 0.05 * ki_67 + 0.17 * nf_kβ_p65z + 0.43 * soh_2 - 1.16
            p = 1 / (1 + pow(2.71828, -z))

            if (p >= 0.48):
                self.label_result.setText("Высокий риск рецидивирования эндометриоидных кист яичников")
            else:
                self.label_result.setText("Низкий риск рецидивирования эндометриоидных кист яичников")

        except ValueError:
            self.label_result.setText("Ошибка: пожалуйста, введите числовые значения во все поля")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window... ')