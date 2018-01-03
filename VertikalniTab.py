from PyQt5 import QtGui, QtCore, QtWidgets

class VertikalniTab(QtWidgets.QTabBar):
    def __init__(self, *args, **kwargs):
        self.velicinaTaba = QtCore.QSize(kwargs.pop('width'), kwargs.pop('height'))
        super(VertikalniTab, self).__init__(*args, **kwargs)


    def paintEvent(self, QPaintEvent):
        painter = QtWidgets.QStylePainter(self)
        option = QtWidgets.QStyleOptionTab()

        painter.begin(self)
        for index in range(self.count()):
            self.initStyleOption(option, index)
            tabRect = self.tabRect(index)
            tabRect.moveLeft(10)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabShape, option)
            painter.drawText(tabRect, QtCore.Qt.AlignVCenter | QtCore.Qt.TextDontClip, self.tabText(index))
        painter.end()

    def tabSizeHint(self, index):
        return self.velicinaTaba