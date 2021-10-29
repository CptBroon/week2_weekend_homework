class Room:
    
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.current_guests = []
        self.song_list = []
        
    def guest_check_in(self, guest):
        if len(self.current_guests) < self.capacity:
            self.current_guests.append(guest)
            return True
        return False
        
    def guest_check_out(self, guest):
        self.current_guests.remove(guest)
        
    def add_song_to_room(self, song):
        self.song_list.append(song)
        
    def check_remaining_song_list_length(self):
        total_left = 0
        for song in self.song_list:
            total_left += song.length
        return total_left