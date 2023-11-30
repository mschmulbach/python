import sys
from PyQt6 import QtWidgets
from television import TelevisionApp


def main() -> None:
    """
    Initializes and runs the Television application.

    This function creates a QApplication, initializes the TelevisionApp window,
    shows the window, and starts the application's event loop.
    """
    app = QtWidgets.QApplication(sys.argv)
    window = TelevisionApp()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
