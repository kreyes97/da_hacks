class Address:
    def __init__(self, address1, address2, country, state, userid):
        self.address1 = address1
        self.address2 = address2
        self.country = country
        self.state = state


    def create_address(self, userid):
        address = {
            "userid"   : self.userid,
            "address1" : self.address1,
            "address2" : self.address2,
            "country"  : self.country,
            "state"    : self.state
        }
        return address


class School:
    def __init__(self, address1, address2, country, state,):
        self.address1 = address1
        self.address2 = address2
        self.country = country
        self.state = state

    def school_address(self, userid):
        dictionary_address = {
            "userid"   : self.userid,
            "address1" : self.address1,
            "address2" : self.address2,
            "country"  : self.country,
            "state"    : self.state
        }
        return dictionary_address

