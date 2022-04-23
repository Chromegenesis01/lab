class Television:
    '''
    Creates a television class with minimum and maximum channel settings,
    as well as minimum and maximum volume settings.
    '''
    MIN_CHANNEL: int = 0  # Minimum TV channel
    MAX_CHANNEL: int = 3  # Maximum TV channel

    MIN_VOLUME: int = 0  # Minimum TV volume
    MAX_VOLUME: int = 2  # Maximum TV volume

    def __init__(self):
        '''
        creates a tv object with:
        TVchannel being set to 0,
        TVvolume being set to 0,
        TVstatus being set to off.
        '''
        self.TVchannel: int = MIN_CHANNEL
        self.TVvolume: int = MIN_VOLUME
        self.TVstatus: str  = 'off'
        pass

    def power(self):
        """
        - This method is used to turn the TV on/off.
        - If called on a TV object that is off, the TV object is turned on.
        - If called on a TV object that is on, the TV object is turned off.
        """
        if self.TVstatus == 'off':
            self.TVstatus: str = 'on'
        else:
            self.TVstatus: str = 'off'
        pass

    def channel_up(self):
        """
        - This method is used to adjust the TV channel by incrementing its value.
        - only works for TV that is on
        - If called while on MAX_CHANNEL it is set to MIN_CHANNEL
        """
        if self.TVstatus == 'on':
            if self.TVchannel < MAX_CHANNEL:
                self.TVchannel += 1
            elif self.TVchannel == MAX_CHANNEL:
                self.TVchannel = MIN_CHANNEL

        pass

    def channel_down(self):
        """
          - This method is used to adjust the TV channel by decrementing its value.
          - only works for a TV that is on.
          - If called when on the MIN_CHANNEL, it takes the TV channel to the MAX_CHANNEL.
        """
        if self.TVstatus == 'on':
            if self.TVchannel > MIN_CHANNEL:
                self.TVchannel -= 1
            elif self.TVchannel == MIN_CHANNEL:
                self.TVchannel = MAX_CHANNEL

        pass

    def volume_up(self):
        """
        - used to adjust the TV volume by incrementing its value.
        - only works for a TV that is on.
        - If called when on the MAX_VOLUME, the volume is not adjusted.
        """
        if self.TVstatus == 'on':
            if self.TVvolume < MAX_VOLUME:
                self.TVvolume += 1
            elif self.TVvolume == MAX_VOLUME:
                self.TVvolume = MAX_VOLUME
        pass

    def volume_down(self):
        """
        - used to adjust the TV volume by decrementing its value.
        - only works for a TV that is on.
        - If called when on the MIN_VOLUME, the volume is not adjusted.
        """
        if self.TVstatus == 'on':
            if self.TVvolume > MIN_VOLUME:
                self.TVvolume -= 1
            elif self.TVvolume == MIN_VOLUME:
                self.TVvolume = MIN_VOLUME
        pass

    def __str__(self):
        """
        - This method is used to return the TV status
        """
        a: str = 'False'
        if self.TVstatus == 'on':
            a = 'True'
        else:
            a = 'False'
        return f'TV status: Is on = {self.TVstatus}, Channel = {self.TVchannel}, Volume = {self.TVvolume}'
        pass