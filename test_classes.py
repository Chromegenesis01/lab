import pytest
from classes import *

def test_power(self):
    assert power(self) == 'on'
    assert power(self) == 'false'

def test_channel_up(self):
    assert channel_up(self) == 1
    assert channel_up(self) == 2
    assert channel_up(self) == 3
    assert channel_up(self) == 0

def test_channel_down(self):
    assert channel_down(self) == 3
    assert channel_down(self) == 2
    assert channel_down(self) == 1
    assert channel_down(self) == 0

def test_volume_up(self):
    assert test_volume_up(self) == 1
    assert test_volume_up(self) == 2
    assert test_volume_up(self) == 2

def test_volume_down(self):
    assert test_volume_down(self) == 2
    assert test_volume_down(self) == 1
    assert test_volume_down(self) == 0
    assert test_volume_down(self) == 0



