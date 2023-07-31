import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QCheckBox, QComboBox, QScrollArea, \
    QVBoxLayout
from PyQt5.QtCore import Qt

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Дифференцированный подход к проведению двухэтапной превенции преэклампсии'
        self.left = 100
        self.top = 100
        self.width = 1250
        self.height = 900

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.sub_block = QLabel("ФАКТОРЫ ВЫСОКОГО РИСКА ПРЕЭКЛАМПСИИ:", self)
        self.sub_block.move(20, 10)

        self.check_box1 = QCheckBox("ПЭ в личном анамнезе", self)
        self.check_box1.move(20, 30)
        self.check_box1.resize(320, 40)

        self.check_box2 = QCheckBox("Хроническая артериальная гипертензия", self)
        self.check_box2.move(20, 60)
        self.check_box2.resize(320, 40)

        self.check_box3 = QCheckBox("Системная красная волчанка", self)
        self.check_box3.move(20, 90)
        self.check_box3.resize(320, 40)

        self.check_box4 = QCheckBox("Прегестационный сахарный диабет 1 или 2 типа", self)
        self.check_box4.move(20, 120)
        self.check_box4.resize(320, 40)

        self.check_box5 = QCheckBox("Хроническое заболевание почек", self)
        self.check_box5.move(20, 150)
        self.check_box5.resize(320, 40)

        self.check_box6 = QCheckBox("Антифосфолипидный синдром", self)
        self.check_box6.move(20, 180)
        self.check_box6.resize(320, 40)

        self.sub_block1 = QLabel("ФАКТОРЫ УМЕРЕННОГО РИСКА ПРЕЭКЛАМПСИИ:", self)
        self.sub_block1.move(350, 10)

        self.check_box7 = QCheckBox("Отсутствие родов в анамнезе", self)
        self.check_box7.move(350, 30)
        self.check_box7.resize(500, 40)

        self.check_box8 = QCheckBox("Возраст ≥ 35 лет", self)
        self.check_box8.move(350, 60)
        self.check_box8.resize(500, 40)

        self.check_box9 = QCheckBox("Интервал между беременностями > 10 лет", self)
        self.check_box9.move(350, 90)
        self.check_box9.resize(500, 40)

        self.check_box10 = QCheckBox("ИМТ > 30 кг/м^2", self)
        self.check_box10.move(350, 120)
        self.check_box10.resize(500, 40)

        self.check_box11 = QCheckBox("Отягощенный ПЭ семейный анамнез (мать, сестра)", self)
        self.check_box11.move(350, 150)
        self.check_box11.resize(500, 40)

        self.check_box12 = QCheckBox("Социально-демографические характеристики \n"
                                     "(афроамериканская раса или низкий социально- \n"
                                     "экономический статус)", self)
        self.check_box12.move(350, 185)
        self.check_box12.resize(800, 50)

        self.check_box13 = QCheckBox('Наличие в анамнезе родов маловесным \n'
                                     'для гестационного возраста плодом', self)
        self.check_box13.move(350, 230)
        self.check_box13.resize(500, 50)

        self.sub_block2 = QLabel("ВЫЯВЛЕНИЕ ПРЕДИАБЕТА (АНКЕТА FINDRISK)", self)
        self.sub_block2.move(750, 10)

        self.label1 = QLabel('Возраст (полных лет)', self)
        self.label1.move(750, 40)
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(900, 40)
        self.textbox1.resize(100, 20)

        self.label2 = QLabel('Рост (см)', self)
        self.label2.move(750, 70)
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(810, 70)
        self.textbox2.resize(100, 20)

        self.label3 = QLabel('Вес (кг)', self)
        self.label3.move(930, 70)
        self.textbox3 = QLineEdit(self)
        self.textbox3.move(980, 70)
        self.textbox3.resize(100, 20)

        self.label4 = QLabel('Окружность талии (см)', self)
        self.label4.move(750, 100)
        self.textbox4 = QLineEdit(self)
        self.textbox4.move(900, 100)
        self.textbox4.resize(100, 20)

        self.label5 = QLabel('Частота потребления фруктов', self)
        self.label5.move(750, 130)
        self.combobox1 = QComboBox(self)
        self.combobox1.addItems(['Каждый день', 'Не каждый день'])
        self.combobox1.move(950, 130)
        self.combobox1.resize(150, 20)

        self.label6 = QLabel('Ежедневные физические упражнения \n'
                             'по 30 мин или 3 часа в течение недели', self)
        self.label6.move(750, 160)
        self.combobox2 = QComboBox(self)
        self.combobox2.addItems(['Да', 'Нет'])
        self.combobox2.move(1000, 170)
        self.combobox2.resize(100, 20)

        self.label7 = QLabel('Регулярный прием лекарства для \n'
                             'снижения артериального давления', self)
        self.label7.move(750, 200)
        self.combobox3 = QComboBox(self)
        self.combobox3.addItems(['Нет', 'Да'])
        self.combobox3.move(1000, 210)
        self.combobox3.resize(100, 20)

        self.label8 = QLabel('Обнаружение когда-либо уровня \n'
                             'глюкозы выше нормы', self)
        self.label8.move(750, 240)
        self.combobox4 = QComboBox(self)
        self.combobox4.addItems(['Нет', 'Да'])
        self.combobox4.move(1000, 250)
        self.combobox4.resize(100, 20)

        self.label9 = QLabel('Наличие сахарного диабета 1 или 2 типа \n'
                             'у родственников', self)
        self.label9.move(750, 280)
        self.combobox5 = QComboBox(self)
        self.combobox5.addItems(['Нет',
                                 'Да (бабушка/дедушка \nтетя/дядя/двоюродные \nбратья или сестры)',
                                 'Да (родители/брат или \nсестра/собственный ребенок)'])
        self.combobox5.move(1000, 290)
        self.combobox5.resize(200, 20)

        self.label10 = QLabel('Нарушение углеводного обмена', self)
        self.label10.move(50, 330)
        self.combobox6 = QComboBox(self)
        self.combobox6.addItems(['Нет',
                                 'Нарушенная толерантность к глюкозе',
                                 'Нарушенная гликемия натощак'])
        self.combobox6.move(250, 330)
        self.combobox6.resize(250, 20)

        self.label11 = QLabel('Гликированный гемоглобин (%)', self)
        self.label11.move(550, 330)
        self.textbox5 = QLineEdit(self)
        self.textbox5.move(750, 330)
        self.textbox5.resize(100, 20)

        self.button = QPushButton('Рассчитать', self)
        self.button.move(600, 360)
        self.button.clicked.connect(self.pe_form)
        self.button.clicked.connect(self.calc_prediabetes)
        self.button.clicked.connect(self.update_text)

        self.label_result = QLabel('', self)
        self.label_result.move(50, 350)
        self.label_result.resize(400, 100)

        self.label_result2 = QLabel('', self)
        self.label_result2.move(50, 370)
        self.label_result2.resize(800, 100)

        self.widget = QWidget(self)
        self.widget.move(40, 420)
        self.widget.resize(1130, 440)

        layout = QVBoxLayout(self.widget)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        layout.addWidget(scroll_area)
        scroll_widget = QWidget()
        scroll_area.setWidget(scroll_widget)
        scroll_layout = QVBoxLayout(scroll_widget)
        self.scroll_label = QLabel("Рекомендовано:")
        self.scroll_label.setAlignment(Qt.AlignLeft)
        self.scroll_label.setWordWrap(True)
        scroll_layout.addWidget(self.scroll_label)

        self.show()

    def pe_form(self):
        check_boxes_severe_pe = [self.check_box1, self.check_box2, self.check_box3,
                                 self.check_box4, self.check_box5, self.check_box6]
        check_boxes_mild_pe = [self.check_box7, self.check_box8, self.check_box9,
                               self.check_box10, self.check_box11, self.check_box12,
                               self.check_box13]
        severe_pe = 0
        mild_pe = 0
        for check_box in check_boxes_severe_pe:
            if check_box.isChecked():
                severe_pe += 1
        for check_box in check_boxes_mild_pe:
            if check_box.isChecked():
                mild_pe += 1
        if (severe_pe > 0) or (mild_pe > 1):
            self.label_result.setText("Беременная высокого риска преэклампсии")
        elif mild_pe == 1:
            self.label_result.setText("Беременная среднего риска преэклампсии")
        else:
            self.label_result.setText("Беременная низкого риска преэклампсии")

    def calc_prediabetes(self):
        try:
            counter_prediabetes = 0
            # возраст
            if float(self.textbox1.text()) < 45:
                counter_prediabetes += 0
            elif float(self.textbox1.text()) < 54:
                counter_prediabetes += 2
            else:
                counter_prediabetes += 3
            # индекс массы тела
            imt = float(self.textbox3.text()) / ((float(self.textbox2.text()) / 100) ** 2)
            if imt < 25:
                counter_prediabetes += 0
            elif imt < 30:
                counter_prediabetes += 1
            else:
                counter_prediabetes += 3
            # окружность талии
            if float(self.textbox4.text()) < 80:
                counter_prediabetes += 0
            elif float(self.textbox4.text()) < 88:
                counter_prediabetes += 2
            else:
                counter_prediabetes += 3
            # потребление фруктов
            if self.combobox1.currentText() == 'Каждый день':
                counter_prediabetes += 0
            else:
                counter_prediabetes += 1
            # ежедневные физические упражнения
            if self.combobox2.currentText() == 'Да':
                counter_prediabetes += 0
            else:
                counter_prediabetes += 2
            # регулярный прием лекарств
            if self.combobox3.currentText() == 'Нет':
                counter_prediabetes += 0
            else:
                counter_prediabetes += 2
            # глюкоза выше нормы
            if self.combobox4.currentText() == 'Нет':
                counter_prediabetes += 0
            else:
                counter_prediabetes += 5
            # СД у родственников
            if self.combobox5.currentText() == 'Нет':
                counter_prediabetes += 0
            elif self.combobox5.currentText() == 'Да (бабушка/дедушка \nтетя/дядя/двоюродные \nбратья или сестры)':
                counter_prediabetes += 3
            else:
                counter_prediabetes += 5
            # вывод результата
            if (counter_prediabetes < 12) and (self.combobox6.currentText() == 'Нет') and (float(self.textbox5.text()) < 6.0):
                self.label_result2.setText("У пациентки признаков предиабета нет")
            elif (14 < counter_prediabetes) or (6.4 < (float(self.textbox5.text()))):
                self.label_result2.setText("У пациентки признаки сахарного диабета")
            else:
                self.label_result2.setText("У пациентки признаки предиабета")
        except ValueError:
            self.label_result2.setText("Ошибка: пожалуйста, введите числовые значения во все поля анкеты FINDRISK")

    def update_text(self):
        rec_h_r = """Рекомендовано:
Превентивные мероприятия на догестационном этапе:

1. Прием Метформина. Суточная доза – 1000 мг после или во время приема пищи, разделенная на 2 приема (при отсутствии противопоказаний);
2. Модификация образа жизни:
- увеличение физической активности умеренной интенсивности (быстрая ходьба, плавание, велосипед, танцы – продолжительностью 30-60 минут предпочтительно ежедневно, суммарной продолжительностью не менее 150 минут в неделю
- коррекция диеты:
- рекомендуется максимальное ограничение жиров (прежде всего животного происхождения) и сахаров; умеренное (в размере половины привычной порции) – продуктов, состоящих преимущественно из сложных углеводов (крахмалов) и белков; неограниченное потребление продуктов с минимальной калорийностью (в основном богатых водой и клетчаткой овощей);
- рекомендуется потребление углеводов в составе овощей, цельнозерновых, молочных продуктов, в противовес другим источникам углеводов, содержащих дополнительно насыщенные или трансжиры, сахара или натрий;
- рекомендуется включать в рацион продукты, богатые моно- и полиненасыщенными жирными кислотами (рыба, растительные масла);
- не рекомендуется употребление алкогольных напитков;
3. Общепринятая прегравидарная подготовка согласно клиническому протоколу МАРС:
- дотация фолиевой кислоты по 400 мкг/сут., per os, во время еды, запивая достаточным количеством воды;
- дотация препаратов йода по 150 мкг, per os, утром, после еды;
- прием витамина D по 1000 МЕ 1 раз в день, per os, после завтрака;
- соблюдение интергенетического интервала не менее 2-х и не более 5 лет;
- нормализация режима сна и бодрствования (отход ко сну не позднее 23:00 и его длительность 7-8 ч).

Гестационный этап профилактических мероприятий:

Карбогенопрофилактика
Регулируемые дыхательные тренировки путём дыхания через гиперкапникатор ТДИ-01 по следующей схеме: 4 курса с интервалом 4 недели: с 8 по 11 нед., с 16 по 19 нед., с 24 по 27 нед., с 32 по 35 нед. беременности.
Рекомендовано при:
- наличии факторов риска дефицита эндогенного карбогена (возраст более 35 лет, экстрагенитальная патология, в т.ч. метаболический синдром, малоподвижный образ жизни, стресс, реологические и сосудистые расстройства);
- при отказе от медикаментозного профилактического агента (при ранней постановке на учет в ЖК – в 7-8 нед.)

Низкие дозы ацетилсалициловой кислоты
Дозировка 150 мг/сут., после приема пищи, на ночь, с 12 по 36 нед. гестации.
Рекомендовано при:
- наличии согласия на прием медикаментозного профилактического агента
"""
        rec_m_r = """Рекомендовано:
Превентивные мероприятия на догестационном этапе:

1. Модификация образа жизни:
- увеличение физической активности умеренной интенсивности (быстрая ходьба, плавание, велосипед, танцы – продолжительностью 30-60 минут предпочтительно ежедневно, суммарной продолжительностью не менее 150 минут в неделю
- коррекция диеты:
- рекомендуется максимальное ограничение жиров (прежде всего животного происхождения) и сахаров; умеренное (в размере половины привычной порции) – продуктов, состоящих преимущественно из сложных углеводов (крахмалов) и белков; неограниченное потребление продуктов с минимальной калорийностью (в основном богатых водой и клетчаткой овощей);
- рекомендуется потребление углеводов в составе овощей, цельнозерновых, молочных продуктов, в противовес другим источникам углеводов, содержащих дополнительно насыщенные или трансжиры, сахара или натрий;
- рекомендуется включать в рацион продукты, богатые моно- и полиненасыщенными жирными кислотами (рыба, растительные масла);
- не рекомендуется употребление алкогольных напитков;
2. Общепринятая прегравидарная подготовка согласно клиническому протоколу МАРС:
- дотация фолиевой кислоты по 400 мкг/сут., per os, во время еды, запивая достаточным количеством воды;
- дотация препаратов йода по 150 мкг, per os, утром, после еды;
- прием витамина D по 1000 МЕ 1 раз в день, per os, после завтрака;
- соблюдение интергенетического интервала не менее 2-х и не более 5 лет;
- нормализация режима сна и бодрствования (отход ко сну не позднее 23:00 и его длительность 7-8 ч).

Гестационный этап профилактических мероприятий:

Карбогенопрофилактика
Регулируемые дыхательные тренировки путём дыхания через гиперкапникатор ТДИ-01 по следующей схеме: 4 курса с интервалом 4 недели: с 8 по 11 нед., с 16 по 19 нед., с 24 по 27 нед., с 32 по 35 нед. беременности.
Рекомендовано при:
- наличии факторов риска дефицита эндогенного карбогена (возраст более 35 лет, экстрагенитальная патология, в т.ч. метаболический синдром, малоподвижный образ жизни, стресс, реологические и сосудистые расстройства);
"""
        rec_l_r = """Рекомендовано:
Превентивные мероприятия на догестационном этапе:

1. Общепринятая прегравидарная подготовка согласно клиническому протоколу МАРС:
- дотация фолиевой кислоты по 400 мкг/сут., per os, во время еды, запивая достаточным количеством воды;
- дотация препаратов йода по 150 мкг, per os, утром, после еды;
- прием витамина D по 1000 МЕ 1 раз в день, per os, после завтрака;
- соблюдение интергенетического интервала не менее 2-х и не более 5 лет;
- нормализация режима сна и бодрствования (отход ко сну не позднее 23:00 и его длительность 7-8 ч).

Гестационный этап профилактических мероприятий не показан.
"""
        if self.label_result.text() == "Беременная высокого риска преэклампсии":
            self.scroll_label.setText(rec_h_r)
        elif self.label_result.text() == "Беременная среднего риска преэклампсии":
            self.scroll_label.setText(rec_m_r)
        elif self.label_result.text() == "Беременная низкого риска преэклампсии":
            self.scroll_label.setText(rec_l_r)
        else:
            self.scroll_label.setText("Проверьте правильность введенных данных")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window... ')