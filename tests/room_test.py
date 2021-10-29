import unittest

from classes.venue import Venue
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room1 = Room("Rock room", 7)
        self.room2 = Room("Pop room", 5)
        rooms_list = [self.room1, self.room2]
        self.venue = Venue("CodeClan Caraoke", rooms_list, 10)
        self.song1 = Song("In too deep", "Blink-182", 3)
        self.guest1 = Guest("Almas", 50, "Mountains")
        self.guest2 = Guest("Martin", 40, "In too deep")
        
    def test_room_has_name(self):
        self.assertEqual("Rock room", self.room1.name)
        
    def test_room_has_capacity(self):
        self.assertEqual(5, self.room2.capacity)
        
    def test_room_init_has_no_guests(self):
        self.assertEqual(0, len(self.room1.current_guests))
        
    def test_room_init_has_no_songs(self):
        self.assertEqual(0, len(self.room1.song_list))
        
    def test_guest_check_in_passes_if_under_capacity(self):
        self.assertEqual(0, len(self.room1.current_guests))
        self.room1.guest_check_in(self.guest1)
        self.assertEqual(1, len(self.room1.current_guests))
        
    def test_guest_check_in_does_nothing_if_at_capacity(self):
        for i in range(7):
            self.room1.guest_check_in(self.guest1)
        self.assertEqual(7, self.room1.capacity)
        self.assertEqual(False, self.room1.guest_check_in(self.guest2))
        
    def test_guest_check_out_works(self):
        self.room1.guest_check_in(self.guest1)
        self.assertEqual(1, len(self.room1.current_guests))
        self.room1.guest_check_out(self.guest1)
        self.assertEqual(0, len(self.room1.current_guests))
        
    def test_add_song_to_room(self):
        self.room1.add_song_to_room(self.song1)
        self.room1.add_song_to_room(self.song1)
        self.room1.add_song_to_room(self.song1)
        
        self.assertEqual(3, len(self.room1.song_list))
        
    def test_check_remaining_song_list_length(self):
        self.room1.add_song_to_room(self.song1)
        self.room1.add_song_to_room(self.song1)
        self.room1.add_song_to_room(self.song1)
        
        self.assertEqual(9, self.room1.check_remaining_song_list_length())