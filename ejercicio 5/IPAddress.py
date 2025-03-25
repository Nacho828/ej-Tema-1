class IPAddress:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def decompose(self):
        try:
            octets = self.ip_address.split('.')
            if len(octets) != 4 or not all(0 <= int(octet) <= 255 for octet in octets):
                raise ValueError("Invalid IP address format")
            return octets
        except ValueError as e:
            return str(e)