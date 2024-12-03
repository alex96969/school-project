import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap
import webbrowser as wb
from PyQt5 import QtGui
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtCore import QUrl



FNAME_RIS = 'Фото/Фон.jpg'
Standart = 'Фото/Стандарт01.jpg'
Latina = 'Фото/Латина01.jpg'


class Project(QMainWindow):
    def __init__(self):
        super(Project, self).__init__()
        uic.loadUi('ui/First.ui', self)
        self.pixmap = QPixmap(FNAME_RIS)
        self.image.setPixmap(self.pixmap)
        self.yewqfu.clicked.connect(self.name)
        self.saity.clicked.connect(self.sait)
        self.gsf.clicked.connect(self.info)

    def name_1(self):
        uic.loadUi('ui/First.ui', self)
        self.pixmap = QPixmap(FNAME_RIS)
        self.image.setPixmap(self.pixmap)
        self.yewqfu.clicked.connect(self.name)
        self.saity.clicked.connect(self.sait)
        self.gsf.clicked.connect(self.info)

    def name(self):
        uic.loadUi('ui/Second.ui', self)
        self.pixmap = QPixmap(Standart)
        self.Standart.setPixmap(self.pixmap)
        self.pixmap = QPixmap(Latina)
        self.Latina.setPixmap(self.pixmap)
        self.Wa.clicked.connect(self.Wals)
        self.Tg.clicked.connect(self.Tango)
        self.Wv.clicked.connect(self.Vensky_vals)
        self.Sf.clicked.connect(self.Slow_fox)
        self.Qs.clicked.connect(self.Qwickstep)
        self.Sa.clicked.connect(self.Samba)
        self.Ch.clicked.connect(self.Cha_cha_cha)
        self.Rb.clicked.connect(self.Rumba)
        self.Pd.clicked.connect(self.Pasadobl)
        self.Jv.clicked.connect(self.Jive)

    def Wals(self):
        uic.loadUi('ui/Wals.ui', self)
        self.nazad.clicked.connect(self.name)
        self.saw.clicked.connect(self.wals_video)


    def Tango(self):
        uic.loadUi('ui/Tango.ui', self)
        self.nazad_2.clicked.connect(self.name)

    def Vensky_vals(self):
        uic.loadUi('ui/Venskiy.ui', self)
        self.nazad_3.clicked.connect(self.name)

    def Slow_fox(self):
        uic.loadUi('ui/Slow.ui', self)
        self.nazad_4.clicked.connect(self.name)

    def Qwickstep(self):
        uic.loadUi('ui/Qwiq.ui', self)
        self.nazad_5.clicked.connect(self.name)

    def Samba(self):
        uic.loadUi('ui/Samba.ui', self)
        self.nazad_6.clicked.connect(self.name)

    def Cha_cha_cha(self):
        uic.loadUi('ui/cha.ui', self)
        self.nazad_7.clicked.connect(self.name)

    def Rumba(self):
        uic.loadUi('ui/rumba.ui', self)
        self.nazad_8.clicked.connect(self.name)

    def Pasadobl(self):
        uic.loadUi('ui/Paso.ui', self)
        self.nazad_9.clicked.connect(self.name)

    def Jive(self):
        uic.loadUi('ui/Jive.ui', self)
        self.nazad_10.clicked.connect(self.name)


    def pause_video(self):
        self.media.pause()

    def play_video(self):
        self.media.play()

    def stop_video(self):
        self.media.stop()

    def wals_video(self):
        uic.loadUi('ui/vals_video.ui', self)
        self.media = QMediaPlayer(self)
        self.media.setVideoOutput(self.video)
        self.media.setMedia(
            QMediaContent(QUrl.fromLocalFile("Видео/wals_resized.avi.avi")))
        self.media.play()
        self.Play.clicked.connect(self.play_video)
        self.Pause.clicked.connect(self.pause_video)
        self.pbopen.clicked.connect(self.openfile)
        self.nazad.clicked.connect(self.name)
        self.Stop.clicked.connect(self.stop_video)


    def openfile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File")

        if fileName != '':
            self.media.setMedia(
                QMediaContent(QUrl.fromLocalFile(fileName)))
            self.media.play()


    def sait(self):
        wb.open('https://fdsarr.ru/dance/')

    def info(self):
        uic.loadUi('ui/info.ui', self)
        self.main_menu.clicked.connect(self.name_1)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    pro = Project()
    pro.show()
    sys.exit(app.exec())
