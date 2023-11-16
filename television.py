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
        Toggles the mute status. If the TV is currently unmuted, it mutes and saves the current volume.
        If the TV is muted, it restores the volume to the previous level.
        """
        if self.__status:
            if not self.__muted:
                self.__prev_volume = self.__volume
                self.__volume = Television.MIN_VOLUME
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
        """Increases the volume by one, not exceeding the maximum volume, and unmutes if currently muted."""
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__prev_volume
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decreases the volume by one, not going below the minimum volume. If muted, it sets volume to 1 and unmutes.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = 1
            elif self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Returns a string representation of the television's current status, including power, channel, and volume.
        :return: A string indicating the power status, channel, and volume of the television.
        """
        power_status = "True" if self.__status else "False"
        volume_status = "0" if self.__muted else str(self.__volume)
        channel_status = str(self.__channel)
        return f"Power = {power_status}, Channel = {channel_status}, Volume = {volume_status}"
