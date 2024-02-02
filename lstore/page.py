PAGESIZE = 4096
PAGECAP = PAGESIZE/8

class Page:

    def __init__(self):
        self.num_records = 0
        self.data = bytearray(PAGESIZE)

    def has_capacity(self):
        return self.num_records < PAGECAP

    def write(self, value):
        #all columns are 64 bit ints so 8 bytes
        offset = self.num_records*8
        self.data[offset:offset+8] = value.to_bytes(8, 'big')
        self.num_records += 1
        return id(self.data) + offset
