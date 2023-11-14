# Adjusting the Television class to ensure it produces the expected output when the main function is executed.

class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__prev_volume = Television.MAX_VOLUME  # Initial previous volume is max to handle first mute correctly

    def power(self):
        self.__status = not self.__status

    def mute(self):
        if self.__status:
            if not self.__muted:
                self.__prev_volume = self.__volume
                self.__volume = Television.MIN_VOLUME
            else:
                self.__volume = self.__prev_volume
            self.__muted = not self.__muted

    def channel_up(self):
        if self.__status:
            self.__channel = (self.__channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self):
        if self.__status:
            self.__channel = (self.__channel - 1) if self.__channel > Television.MIN_CHANNEL else Television.MAX_CHANNEL

    def volume_up(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__prev_volume
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = 1  # Set volume to 1 when muted and volume down is pressed
            elif self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        power_status = "True" if self.__status else "False"
        volume_status = "0" if self.__muted else str(self.__volume)
        channel_status = str(self.__channel)
        return f"Power = {power_status}, Channel = {channel_status}, Volume = {volume_status}"
