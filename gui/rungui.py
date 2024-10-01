from PyQt5 import QtWidgets

def run_gui():
    app = QtWidgets.QApplication([])
    window = QtWidgets.QMainWindow()
    window.setWindowTitle("My App")
    window.show()
    app.exec_()
if __name__ == '__main__':
    run_gui()