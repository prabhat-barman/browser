import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        # nav
        navbar = QToolBar()
        self.addToolBar(navbar)
        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
        frwd_btn = QAction('Forward', self)
        frwd_btn.triggered.connect(self.browser.forward)
        navbar.addAction(frwd_btn)
        ref_btn = QAction('Refresh', self)
        ref_btn.triggered.connect(self.browser.reload)
        navbar.addAction(ref_btn)
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://www.google.com/'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('google killer')
window = MainWindow()
app.exec_()
