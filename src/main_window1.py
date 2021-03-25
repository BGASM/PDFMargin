from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class UI_PDFMarginWindow(QObject):
    def setupUi(self, PDFMarginWindow):
        if not PDFMarginWindow.objectName():
            PDFMarginWindow.setObjectName(u"PDFMarginWindow")
        PDFMarginWindow.resize(820, 600)
        self.centralwidget = QWidget(PDFMarginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mainHorizontalLayout = QHBoxLayout()
        self.mainHorizontalLayout.setObjectName(u"mainHorizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(150, 130))
        self.label.setMaximumSize(QSize(150, 130))
        font = QFont()
        font.setFamily(u"Open Sans ExtraBold")
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setWordWrap(True)

        self.mainHorizontalLayout.addWidget(self.label)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.inputHorizontalLayout = QHBoxLayout()
        self.inputHorizontalLayout.setObjectName(u"inputHorizontalLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(61, 0))

        self.inputHorizontalLayout.addWidget(self.label_2)

        self.input_lineEdit = QLineEdit(self.frame)
        self.input_lineEdit.setObjectName(u"input_lineEdit")

        self.inputHorizontalLayout.addWidget(self.input_lineEdit)

        self.browse_input_pushButton = QPushButton(self.frame)
        self.browse_input_pushButton.setObjectName(u"browse_input_pushButton")

        self.inputHorizontalLayout.addWidget(self.browse_input_pushButton)


        self.gridLayout.addLayout(self.inputHorizontalLayout, 0, 0, 1, 2)

        self.outputHorizontalLayout = QHBoxLayout()
        self.outputHorizontalLayout.setObjectName(u"outputHorizontalLayout")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(61, 0))

        self.outputHorizontalLayout.addWidget(self.label_3)

        self.output_lineEdit = QLineEdit(self.frame)
        self.output_lineEdit.setObjectName(u"output_lineEdit")

        self.outputHorizontalLayout.addWidget(self.output_lineEdit)

        self.browse_output_pushButton = QPushButton(self.frame)
        self.browse_output_pushButton.setObjectName(u"browse_output_pushButton")

        self.outputHorizontalLayout.addWidget(self.browse_output_pushButton)


        self.gridLayout.addLayout(self.outputHorizontalLayout, 1, 0, 1, 2)

        self.marginHorizontalLayout = QHBoxLayout()
        self.marginHorizontalLayout.setObjectName(u"marginHorizontalLayout")
        self.lrHorizontalLayout = QHBoxLayout()
        self.lrHorizontalLayout.setObjectName(u"lrHorizontalLayout")
        self.lr_lineEdit = QLineEdit(self.frame)
        self.lr_lineEdit.setObjectName(u"lr_lineEdit")
        self.lr_lineEdit.setMaximumSize(QSize(30, 16777215))

        self.lrHorizontalLayout.addWidget(self.lr_lineEdit)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(200, 0))

        self.lrHorizontalLayout.addWidget(self.label_4)


        self.marginHorizontalLayout.addLayout(self.lrHorizontalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.marginHorizontalLayout.addItem(self.horizontalSpacer)

        self.tbHorizontalLayout = QHBoxLayout()
        self.tbHorizontalLayout.setObjectName(u"tbHorizontalLayout")
        self.tb_lineEdit = QLineEdit(self.frame)
        self.tb_lineEdit.setObjectName(u"tb_lineEdit")
        self.tb_lineEdit.setMaximumSize(QSize(30, 16777215))

        self.tbHorizontalLayout.addWidget(self.tb_lineEdit)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(200, 0))

        self.tbHorizontalLayout.addWidget(self.label_5)


        self.marginHorizontalLayout.addLayout(self.tbHorizontalLayout)


        self.gridLayout.addLayout(self.marginHorizontalLayout, 2, 0, 1, 2)

        self.checkHorizontalLayout = QHBoxLayout()
        self.checkHorizontalLayout.setObjectName(u"checkHorizontalLayout")

        self.delete_checkBox = QCheckBox(self.frame)
        self.delete_checkBox.setObjectName(u"delete_checkBox")
        self.delete_checkBox.setMinimumSize(QSize(141, 0))

        self.checkHorizontalLayout.addWidget(self.delete_checkBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.checkHorizontalLayout.addItem(self.horizontalSpacer_2)

        self.files_checkBox = QCheckBox(self.frame)
        self.files_checkBox.setObjectName(u"files_checkBox")
        self.files_checkBox.setMinimumSize(QSize(141, 0))

        self.checkHorizontalLayout.addWidget(self.files_checkBox)


        self.gridLayout.addLayout(self.checkHorizontalLayout, 3, 0, 1, 2)

        self.horizontalSpacer_3 = QSpacerItem(535, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 4, 0, 1, 1)

        self.create_pushButton = QPushButton(self.frame)
        self.create_pushButton.setObjectName(u"create_pushButton")
        self.create_pushButton.setMinimumSize(QSize(82, 0))

        self.gridLayout.addWidget(self.create_pushButton, 4, 1, 1, 1)


        self.mainHorizontalLayout.addWidget(self.frame)


        self.verticalLayout.addLayout(self.mainHorizontalLayout)

        self.debug_textBrowser = QTextBrowser(self.centralwidget)
        self.debug_textBrowser.setObjectName(u"debug_textBrowser")

        self.verticalLayout.addWidget(self.debug_textBrowser)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.verticalLayout.addWidget(self.progressBar)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        PDFMarginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PDFMarginWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        PDFMarginWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PDFMarginWindow)
        self.statusbar.setObjectName(u"statusbar")
        PDFMarginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PDFMarginWindow)
        self.browse_input_pushButton.clicked.connect(self.inputBrowseSlot)
        self.browse_output_pushButton.clicked.connect(self.outputBrowseSlot)
        self.input_lineEdit.editingFinished.connect(self.input_text_editFinishedSlot)
        self.output_lineEdit.editingFinished.connect(self.output_text_editFinishedSlot)
        self.lr_lineEdit.editingFinished.connect(self.x_editFinishedSlot)
        self.tb_lineEdit.editingFinished.connect(self.y_editFinishedSlot)
        self.files_checkBox.stateChanged.connect(self.files_checkSlot)
        self.delete_checkBox.stateChanged.connect(self.delete_checkSlot)
        self.create_pushButton.clicked.connect(self.createSlot)

        QMetaObject.connectSlotsByName(PDFMarginWindow)
    # setupUi

    def retranslateUi(self, PDFMarginWindow):
        PDFMarginWindow.setWindowTitle(QCoreApplication.translate("PDFMarginWindow", u"PDFMarginWindow", None))
        self.label.setText(QCoreApplication.translate("PDFMarginWindow", u"PFD Margin", None))
        self.label_2.setText(QCoreApplication.translate("PDFMarginWindow", u"Input Dir", None))
        self.browse_input_pushButton.setText(QCoreApplication.translate("PDFMarginWindow", u"Browse", None))
        self.label_3.setText(QCoreApplication.translate("PDFMarginWindow", u"Output Dir", None))
        self.browse_output_pushButton.setText(QCoreApplication.translate("PDFMarginWindow", u"Browse", None))
        self.label_4.setText(QCoreApplication.translate("PDFMarginWindow", u"Left and Right Margins (inches)", None))
        self.label_5.setText(QCoreApplication.translate("PDFMarginWindow", u"Top and Bottom Margins (inches)", None))
        self.delete_checkBox.setText(QCoreApplication.translate("PDFMarginWindow", u"Delete Original Files", None))
        self.files_checkBox.setText(QCoreApplication.translate("PDFMarginWindow", u"Select Specific Files", None))
        self.create_pushButton.setText(QCoreApplication.translate("PDFMarginWindow", u"Create PDFs", None))
    # retranslateUi


    def inputBrowseSlot(self):
        print("Still using main.")
        pass



    def outputBrowseSlot(self):
        pass



    def input_text_editFinishedSlot(self):
        pass



    def output_text_editFinishedSlot(self):
        pass



    def x_editFinishedSlot(self):
        pass



    def y_editFinishedSlot(self):
        pass



    def files_checkSlot(self):
        pass



    def delete_checkSlot(self):
        pass



    def createSlot(self):
        pass
