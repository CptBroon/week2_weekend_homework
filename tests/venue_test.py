import unittest

from classes.guest import Guest
from classes.venue import Venue
from classes.room import Room
from classes.song import Song

class TestVenue(unittest.TestCase):
    
    def setUp(self):
        room1 = Room("Rock room", 7)
        room2 = Room("Pop room", 5)
        rooms_list = [room1, room2]
        self.venue = Venue("CodeClan Caraoke", rooms_list, 10)
        
    def test_venue_has_name(self):
        self.assertEqual("CodeClan Caraoke", self.venue.name)
        
    def test_venue_has_rooms(self):
        self.assertLess(0, len(self.venue.rooms))
        
    def test_venue_has_entry_fee(self):
        self.assertEqual(10, self.venue.entry_fee)