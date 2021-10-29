class Venue:
    
    def __init__(self, name, rooms, entry_fee):
        self.name = name
        self.rooms = rooms
        self.entry_fee = entry_fee
        
    def enter_venue(self, guest):
        if guest.paid_entry == False:
            guest.wallet -= self.entry_fee
            guest.paid_entry = True