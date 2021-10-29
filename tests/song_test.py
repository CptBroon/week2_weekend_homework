import unittest

from classes.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song1 = Song("In too deep", "Blink-182", 3)
        self.song2 = Song("Mountains", "Biffy Clyro", 3)
        self.song3 = Song("bad guy", "Billie Eilish", 3)
        self.song4 = Song("Temperature", "Sean Paul", 4)
        
    def test_song_has_name(self):
        self.assertEqual("Mountains", self.song2.track_name)
        
    def test_song_has_artist_name(self):
        self.assertEqual("Blink-182", self.song1.artist_name)
        
    def test_song_has_length(self):
        self.assertEqual(3, self.song1.length)