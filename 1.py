import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                                QLabel, QLineEdit, QTextEdit, QComboBox,
                                QDateEdit, QRadioButton, QButtonGroup,
                                QCheckBox, QPushButton,
                                QVBoxLayout, QHBoxLayout, QFormLayout,
                                QSpacerItem, QSizePolicy)
from PySide6.QtCore import Qt, QDate, QLocale
from PySide6.QtGui import QFont

class RegistrationForm(QMainWindow): 
    def __init__(self):
        super().__init__() #เรียก constructor ของคลาสแม่ (QMainWindow) เพื่อให้หน้าต่างถูก setup ถูกต้อง
        self.setWindowTitle("Student Registration")
        self.resize(400, 600)

        central = QWidget() #สร้าง widget เปล่า ๆ เป็น “พื้นที่หลัก” สำหรับวางทุกอย่าง
        self.setCentralWidget(central) #ใน QMainWindow ต้องมี central widget ก่อนจะใส่ layout ได้

        main_layout = QVBoxLayout(central) #สร้าง layout แนวตั้ง และผูกกับ central
        main_layout.setContentsMargins(24, 18, 24, 18) #ระยะขอบ
        main_layout.setSpacing(14) #ระยะห่าง widget

        # Title
        title = QLabel("Student Registration Form")
        title_font = QFont("Arial", 16, QFont.Bold)
        title.setFont(title_font) #นำฟอนต์ไปใช้กับ QLabel
        title.setAlignment(Qt.AlignHCenter)
        main_layout.addWidget(title) #เอา title ใส่ใน layout หลัก (อยู่บรรทัดบนสุด)

        # Form layout
        form = QFormLayout()
        form.setLabelAlignment(Qt.AlignLeft) #label ฝั่งซ้ายให้ชิดซ้าย
        form.setFormAlignment(Qt.AlignTop) #ฟอร์มทั้งหมดให้ชิดด้านบน (ไม่ไปกองกลาง)
        form.setHorizontalSpacing(14) #ระยะห่างระหว่าง “คอลัมน์ label” กับ “คอลัมน์ field
        form.setVerticalSpacing(12)

        # Full Name
        self.fullname_edit = QLineEdit()
        self.fullname_edit.setText("Kornchawal Chaipah")
        form.addRow("Full Name:", self.fullname_edit)
                
        # Email
        self.email_edit = QLineEdit()
        self.email_edit.setText("kornchawal@kku.ac.th")
        form.addRow("Email:", self.email_edit)

          # Phone
        self.phone_edit = QLineEdit()
        self.phone_edit.setText("0813333333")
        form.addRow("Phone:", self.phone_edit)

        # Date of Birth (QDateEdit)
        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True) # Shows calendar dropdown
        self.date_edit.setDisplayFormat("MM/dd/yyyy")

        self.date_edit.setDate(QDate(2000, 1, 1)) # Default date
        self.date_edit.setFixedWidth(100) #ล็อกความกว้างของช่องวันที่
        form.addRow("Date of Birth:", self.date_edit)

        form.addItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Fixed))


        # Gender (RadioButtons + ButtonGroup)
        gender_row = QHBoxLayout()
        gender_row.setSpacing(18)
        gender_row.setContentsMargins(0, 0, 0, 0)  #กันช่องว่างแปลก ๆ
        gender_row.setAlignment(Qt.AlignLeft)   #ให้ชิดซ้ายเหมือนแถวอื่น

        self.gender_group = QButtonGroup(self)
        self.male_radio = QRadioButton("Male")
        self.female_radio = QRadioButton("Female")
        self.nonbinary_radio = QRadioButton("Non-binary")
        self.prefer_no_radio = QRadioButton("Prefer not to say")

        self.gender_group.addButton(self.male_radio)
        self.gender_group.addButton(self.female_radio)
        self.gender_group.addButton(self.nonbinary_radio)
        self.gender_group.addButton(self.prefer_no_radio)

        # (ให้เหมือนภาพ: Female ถูกเลือก)
        self.female_radio.setChecked(True)

        gender_row.addWidget(self.male_radio)
        gender_row.addWidget(self.female_radio)
        gender_row.addWidget(self.nonbinary_radio)
        gender_row.addWidget(self.prefer_no_radio)
        gender_row.addStretch() #.ใส่ให้ปุ่มไม่ออกมาแปลกๆ

        gender_container = QWidget()
        gender_container.setLayout(gender_row)
        form.addRow("Gender:", gender_container)

 # Program (ComboBox)
        self.program_combo = QComboBox()
        self.program_combo.addItems([
            "Computer Engineering",
            "Digital Media Engineering",
            "Environmental Engineering",
            "Electrical Engineering",
            "Semiconductor Engineering",
            "Mechanical Engineering",
            "Industrial Engineering",
            "Logistics Engineering",
            "Power Engineering",
            "Electronic Engineering",
            "Telecommunication Engineering",
            "Agricultural Engineering",
            "Civil Engineering",
            "ARIS",
        ])
        form.addRow("Program:", self.program_combo)

        # About (QTextEdit)
        self.about_edit = QTextEdit()
        self.about_edit.setMinimumHeight(100)
        form.addRow("Tell us a little bit about yourself:", self.about_edit)

        main_layout.addLayout(form)

        # Terms checkbox
        self.terms_check = QCheckBox("I accept the terms and conditions.")
        main_layout.addWidget(self.terms_check)

        # Submit button (center)
        btn_row = QHBoxLayout()
        btn_row.addStretch() #ซ้ายเพื่อดันให้ปุ่มไปกลาง
        self.submit_btn = QPushButton("Submit Registration")
        self.submit_btn.setFixedWidth(180)
        btn_row.addWidget(self.submit_btn)
        btn_row.addStretch()
        main_layout.addLayout(btn_row)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QLocale.setDefault(QLocale(QLocale.English, QLocale.UnitedStates))
    w = RegistrationForm()
    w.show()
    sys.exit(app.exec())
