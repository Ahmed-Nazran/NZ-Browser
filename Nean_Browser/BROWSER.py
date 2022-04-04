from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys
#pip install PyQt5
import impoFile

x="\p".replace("p","")

class Main(QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(impoFile.__file__.replace("impoFile.py","Neanpage.html").replace(x,"/")))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        nav = QToolBar()
        self.addToolBar(nav)
        self.setStyleSheet("background-color: black; color: white; font-size: 20px")

        back = QAction('<-', self)
        back.triggered.connect(self.browser.back)
        nav.addAction(back)

        forward = QAction('->', self)
        forward.triggered.connect(self.browser.forward)
        nav.addAction(forward)

        reload = QAction('⟳', self)
        reload.triggered.connect(self.browser.reload)
        nav.addAction(reload)

        home = QAction('⌂', self)
        home.triggered.connect(self.navigate)
        nav.addAction(home)

        self.url = QLineEdit()
        self.url.returnPressed.connect(self.nav_url)
        nav.addWidget(self.url)

        self.browser.urlChanged.connect(self.update)

    def navigate(self):
        self.browser.setUrl(QUrl('https://www.google.com/'))

    def nav_url(self):
        url = self.url.text()
        self.browser.setUrl(QUrl(url))

    def update(self, q):
        self.url.setText(q.toString())
        
app = QApplication(sys.argv)
QApplication.setApplicationName('Nean Browser')
window = Main()
app.exec_()