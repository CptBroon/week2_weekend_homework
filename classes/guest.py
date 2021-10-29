class Guest:
    
    def __init__(self, name, money, fav_song):
        self.name = name
        self.wallet = money
        self.fav_song = fav_song
        self.paid_entry = False
        
    def guest_move_room(self, old_room, new_room):
        if new_room.guest_check_in(self) == True:
            old_room.guest_check_out(self)