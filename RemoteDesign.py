from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QLabel, QWidget, QPushButton


class UiRemote(object):
    def __init__(self) -> None:
        """
        Initializes the UiRemote class, setting up the default values for the UI elements.
        """
        self.powerButton: QPushButton = None

    def setupui(self, remote: QWidget) -> None:
        """
        Sets up the user interface for the remote.

        Args:
            remote (QWidget): The main widget to which UI elements are added.
        """
        remote.setObjectName("Remote")
        remote.setEnabled(True)
        remote.resize(270, 412)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(remote.sizePolicy().hasHeightForWidth())
        remote.setSizePolicy(size_policy)
        self.powerButton = QtWidgets.QPushButton(parent=remote)
        self.powerButton.setGeometry(QtCore.QRect(20, 180, 91, 32))
        self.powerButton.setObjectName("powerButton")
        self.muteButton = QtWidgets.QPushButton(parent=remote)
        self.muteButton.setGeometry(QtCore.QRect(160, 180, 91, 32))
        self.muteButton.setObjectName("muteButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=remote)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 230, 141, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.volumeUpButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.volumeUpButton.setObjectName("volumeUpButton")
        self.verticalLayout.addWidget(self.volumeUpButton)
        self.volumeLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.volumeLabel.setObjectName("volumeLabel")
        self.verticalLayout.addWidget(self.volumeLabel, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.volumeDownButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.volumeDownButton.setObjectName("volumeDownButton")
        self.verticalLayout.addWidget(self.volumeDownButton)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=remote)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(140, 230, 131, 121))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.channelUpButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.channelUpButton.setObjectName("channelUpButton")
        self.verticalLayout_2.addWidget(self.channelUpButton)
        self.channelLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.channelLabel.setObjectName("channelLabel")
        self.verticalLayout_2.addWidget(self.channelLabel, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.channelDownButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.channelDownButton.setObjectName("channelDownButton")
        self.verticalLayout_2.addWidget(self.channelDownButton)
        self.volumeSlider = QtWidgets.QScrollBar(parent=remote)
        self.volumeSlider.setGeometry(QtCore.QRect(30, 360, 211, 20))
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.volumeSlider.sizePolicy().hasHeightForWidth())
        self.volumeSlider.setSizePolicy(size_policy)
        self.volumeSlider.setMinimumSize(QtCore.QSize(211, 20))
        self.volumeSlider.setMaximumSize(QtCore.QSize(10, 20))
        self.volumeSlider.setTabletTracking(False)
        self.volumeSlider.setMaximum(2)
        self.volumeSlider.setPageStep(0)
        label_positions = [(30, "0"), (130, "1"), (230, "2")]
        for pos, text in label_positions:
            label = QLabel(parent=remote)
            label.setText(text)
            label.setGeometry(QtCore.QRect(pos, 380, 20, 20))
        self.volumeSlider.setProperty("value", 0)
        self.volumeSlider.setSliderPosition(0)
        self.volumeSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.volumeSlider.setInvertedAppearance(False)
        self.volumeSlider.setObjectName("volumeSlider")
        self.channelDisplayLabel = QtWidgets.QLabel(parent=remote)
        self.channelDisplayLabel.setGeometry(QtCore.QRect(29, 20, 211, 151))
        self.channelDisplayLabel.setText("")
        self.channelDisplayLabel.setObjectName("channelDisplayLabel")
        self.volumeNumberLabel = QtWidgets.QLabel(parent=remote)
        self.volumeNumberLabel.setGeometry(QtCore.QRect(29, 380, 211, 20))
        self.volumeNumberLabel.setObjectName("volumeNumberLabel")

        self.retranslateUi(remote)
        QtCore.QMetaObject.connectSlotsByName(remote)

    def retranslateUi(self, remote: QWidget) -> None:
        """
        Translates the UI elements of the remote.

        Args:
            remote (QWidget): The main widget containing UI elements to be translated.
        """
        _translate = QtCore.QCoreApplication.translate
        remote.setWindowTitle(_translate("Remote", "Form"))
        self.powerButton.setText(_translate("Remote", "Power"))
        self.muteButton.setText(_translate("Remote", "Mute"))
        self.volumeUpButton.setText(_translate("Remote", "+"))
        self.volumeLabel.setText(_translate("Remote", "VOLUME"))
        self.volumeDownButton.setText(_translate("Remote", "-"))
        self.channelUpButton.setText(_translate("Remote", "+"))
        self.channelLabel.setText(_translate("Remote", "CHANNEL"))
        self.channelDownButton.setText(_translate("Remote", "-"))
        self.volumeNumberLabel.setText(_translate("Remote", "  0                        1                         2"))
