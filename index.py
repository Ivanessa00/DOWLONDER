from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

from PyQt5.uic import loadUiType
import urllib.request
import pafy



ui, _ = loadUiType('main.ui')


class MainApp(QMainWindow, ui):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.InitUI()
        self.Buttons()

    def InitUI(self):
        pass

    def Buttons(self):
        self.pushButton.clicked.connect(self.Download)
        self.pushButton_2.clicked.connect(self.Browse)
        self.pushButton_4.clicked.connect(self.Download_Video)
        self.pushButton_5.clicked.connect(self.Save_Browse)

    def Progress(self, num, size, size_1):
        result = num * size
        if size_1 > 100:
            download_percentage = result * 100 / size_1
            self.progressBar.setValue(download_percentage)
            QApplication.processEvents()

    def Browse(self):
        save_location = QFileDialog.getSaveFileName(self, caption='save as', directory='.', filter='All Files')
        self.lineEdit_2.setText(str(save_location[0]))

    #https://download.sublimetext.com/Sublime%20Text%20Build%203211%20x64%20Setup.exe

    def Download(self):
        print("Cкачивание")

        download_url = self.lineEdit.text()
        save_location = self.lineEdit_2.text()

        if download_url == '' or save_location == "":
            QMessageBox.warning(self, "Ошибка", 'Проверьте ссылку или путь сохранения')
        else:

            try:
                urllib.request.urlretrieve(download_url, save_location, self.Progress)
            except Exception:
                QMessageBox.warning(self, "Ошибка", 'Проверьте ссылку или путь сохранения')
                return

        QMessageBox.information(self, "Загрузка завершена", 'Загрузка завершена успешно')

        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.progressBar.setValue(0)

    def Save_Browse(self):
        pass

    def Save_Browse(self):

        save_location = QFileDialog.getSaveFileName(self, caption='save as', directory='.', filter='video_name.mp4')
        self.lineEdit_4.setText(str(save_location[0]))

    ###################
    # Для видео с ютуба

    def Download_Video(self):

        video_url = self.lineEdit_3.text()
        save_location = self.lineEdit_4.text()

        if video_url == "" or save_location == "":
            QMessageBox.warning(self, "Ошибка", 'Проверьте ссылку или путь сохранения')
        else:
            video = pafy.new(video_url)
            video_stream = video.videostreams
            #urllib.request.urlretrieve(video_url, save_location, self.Video_Progress)
            download = video_stream.download(filepath=save_location, callback=self.Video_Progress)


    def Video_Progress(self, total ,received, ratio, rate, time):
        data = received
        if total > 0:
            download_percentage = data * 100 / total
            self.progressBar_2.setValue(download_percentage)
            QApplication.processEvents()

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()