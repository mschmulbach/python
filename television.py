from PyQt6 import QtWidgets, QtCore
from PyQt6.QtGui import QPixmap

from RemoteDesign import UiRemote


class Television:
    """A class to represent a television set with volume and channel controls."""

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """Initializes the television with default settings for power status, volume, and channel."""
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL
        self.__prev_volume: int = Television.MAX_VOLUME

    def power(self) -> None:
        """Toggles the power status of the television on or off."""
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Toggles the mute status. If the TV is currently unmuted, it mutes.
        If the TV is muted, it unmutes without changing the volume.
        """
        if self.__status:
            if not self.__muted:
                self.__prev_volume = self.__volume
            else:
                self.__volume = self.__prev_volume
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Increases the channel number by one, wrapping back to the minimum after reaching the maximum."""
        if self.__status:
            self.__channel = (self.__channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        """Decreases the channel number by one, wrapping to the maximum after reaching the minimum."""
        if self.__status:
            self.__channel = (self.__channel - 1) if self.__channel > Television.MIN_CHANNEL else Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """Increases the volume by one, not exceeding the maximum volume, only if unmuted."""
        if self.__status and not self.__muted:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decreases the volume by one, not going below the minimum volume, only if unmuted.
        """
        if self.__status and not self.__muted:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def get_volume(self) -> int:
        """Returns the current volume level."""
        return self.__volume

    def get_channel(self) -> int:
        """Returns the current channel number."""
        return self.__channel

    def __str__(self) -> str:
        """
        Returns a string representation of the television's current status, including power, channel, and volume.
        :return: A string indicating the power status, channel, and volume of the television.
        """
        power_status = "True" if self.__status else "False"
        volume_status = "0" if self.__muted else str(self.__volume)
        channel_status = str(self.__channel)
        return f"Power = {power_status}, Channel = {channel_status}, Volume = {volume_status}"

    def is_muted(self) -> bool:
        """Returns the mute status of the television."""
        return self.__muted

    def is_on(self) -> bool:
        """Returns the current power status of the television."""
        return self.__status


class TelevisionApp(QtWidgets.QWidget, UiRemote):
    def __init__(self) -> None:
        """
        Initializes the TelevisionApp with UI setup and connects UI elements to Television class methods.
        """
        super().__init__()
        self.powerButton = None
        self.setupui(self)  
        self.tv = Television()  

        # Connect UI elements to Television class methods
        self.powerButton.clicked.connect(self.toggle_power)
        self.muteButton.clicked.connect(self.toggle_mute)
        self.volumeUpButton.clicked.connect(self.volume_up)
        self.volumeDownButton.clicked.connect(self.volume_down)
        self.channelUpButton.clicked.connect(self.channel_up)
        self.channelDownButton.clicked.connect(self.channel_down)
        self.volumeSlider.valueChanged.connect(self.update_volume_slider)

    def toggle_power(self) -> None:
        """
        Toggles the power state of the television and updates the UI accordingly.
        """
        self.tv.power()
        if self.tv.is_on():
            self.update_channel_display()  
        else:
            self.channelDisplayLabel.clear()  
        self.update_ui()

    def toggle_mute(self) -> None:
        """
        Toggles the mute state of the television and updates the UI.
        """
        self.tv.mute()
        self.update_ui()

    def volume_up(self) -> None:
        """
        Increases the volume of the television and updates the UI.
        """
        self.tv.volume_up()
        self.update_ui()

    def volume_down(self) -> None:
        """
        Decreases the volume of the television and updates the UI.
        """
        self.tv.volume_down()
        self.update_ui()

    def channel_up(self) -> None:
        """
        Increases the television's channel and updates the channel display and the UI.
        """
        self.tv.channel_up()
        self.update_channel_display()
        self.update_ui()

    def channel_down(self) -> None:
        """
        Decreases the television's channel and updates the channel display and the UI.
        """
        self.tv.channel_down()
        self.update_channel_display()
        self.update_ui()

    def update_channel_display(self) -> None:
        """
        Updates the channel display label with the current channel's image.
        """
        channel = self.tv.get_channel()
        image_path = f"channel{channel}.PNG"
        pixmap = QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(211, 151, QtCore.Qt.AspectRatioMode.IgnoreAspectRatio)
        self.channelDisplayLabel.setPixmap(scaled_pixmap)

    def update_volume_slider(self) -> None:
        """
        Updates the volume slider to match the current volume of the television.
        """
        self.volumeSlider.setValue(self.tv.get_volume())

    def update_ui(self) -> None:
        """
        Updates the UI elements to reflect the current state of the television.
        """
        current_volume = self.tv.get_volume()
        self.volumeSlider.setValue(current_volume)
        self.volumeNumberLabel.setText(str(current_volume))
        
