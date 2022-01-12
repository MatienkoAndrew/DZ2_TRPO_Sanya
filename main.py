from PyQt5 import QtCore, QtGui, QtWidgets
from src.TransactionScript.MainWindowImp import MainForm


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainForm = MainForm()
    mainForm.show()
    sys.exit(app.exec_())

# CREATE TABLE Plants (
# id SERIAL PRIMARY KEY,
# name TEXT,
# length INT,
# weight INT
# );
