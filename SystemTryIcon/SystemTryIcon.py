
import sys
import subprocess
from PySide2 import QtWidgets, QtGui

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    """
    CREATE A SYSTEM TRAY ICON CLASS AND ADD MENU
    """
    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.setToolTip(f'Pan GPS QuickAccess: Connected')
        menu = QtWidgets.QMenu(parent)
        connect_vpn = menu.addAction("Connect to VPN")
        connect_vpn.triggered.connect(self.connect_vpn)
        connect_vpn.setIcon(QtGui.QIcon("lock.png"))

        diconnect_vpn = menu.addAction("Disconnect VPN")
        diconnect_vpn.triggered.connect(self.diconnect_vpn)
        diconnect_vpn.setIcon(QtGui.QIcon("unlock.png"))

        exit_ = menu.addAction("Exit")
        exit_.triggered.connect(lambda: sys.exit())
        # exit_.setIcon(QtGui.QIcon("icon.png"))

        menu.addSeparator()
        self.setContextMenu(menu)
        self.activated.connect(self.onTrayIconActivated)

    def onTrayIconActivated(self, reason):
        """
        This function will trigger function on click or double click
        :param reason:
        :return:
        """
        if reason == self.DoubleClick:
            self.open_notepad()
        # if reason == self.Trigger:
        #     self.open_notepad()

    def connect_vpn(self):
        """
        this function will open application
        :return:
        """

        subprocess.Popen('net start "Wacom Professional Service"', shell=True)
        self.setIcon(QtGui.QIcon('lock.png'))
        self.setToolTip('Pan GPS: Connected')
        self.showMessage('Pan GPS', 'Connected')

    def diconnect_vpn(self):
        """
        this function will open application
        :return:
        """
        subprocess.Popen('net stop "Wacom Professional Service"', shell=True)
        self.setIcon(QtGui.QIcon('unlock.png'))
        self.setToolTip('Pan GPS: Disconnected')
        self.showMessage('Pan GPS', 'Disconnected')

def main():
    app = QtWidgets.QApplication(sys.argv)

    w = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtGui.QIcon("lock.png"), w)
    tray_icon.show()
    # tray_icon.showMessage('VFX Pipeline', 'Hello "Name of logged in ID')
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()