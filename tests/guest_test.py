import unittest

from classes.venue import Venue
from classes.room import Room
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.room1 = Room("Rock room", 7)
        self.room2 = Room("Pop room", 5)
        self.guest1 = Guest("Almas", 50, "Mountains")
        self.guest2 = Guest("Martin", 40, "In too deep")
        
    def test_guest_has_name(self):
        self.assertEqual("Martin", self.guest2.name)
        
    def test_guest_has_money(self):
        self.assertEqual(50, self.guest1.wallet)
        
    def test_guest_has_fav_song(self):
        self.assertEqual("In too deep", self.guest2.fav_song)
        
    def test_guest_move_room(self):
        self.room1.guest_check_in(self.guest1)
        self.assertEqual(1, len(self.room1.current_guests))
        self.assertEqual(0, len(self.room2.current_guests))
        
        self.guest1.guest_move_room(self.room1, self.room2)
        self.assertEqual(0, len(self.room1.current_guests))
        self.assertEqual(1, len(self.room2.current_guests))