class I2CDevice(object):

    def __init__(self, register_address, i2c_line):
        self.register_address = register_address
        self.i2c_line = i2c_line

    # merge two values to an 8-bit register
    @staticmethod
    def merge_bits(original, value, left_bit_start, length):
        left_shift = (left_bit_start - length + 1)
        # set mask
        mask = ((0x1 << length) - 1) << left_shift
        value <<= left_shift
        value &= mask  # zero the non-target bits in value
        original &= ~mask  # zero the target bits in original value of register
        return original | value  # puts target bits in the original register

    # writes some bits to a register in I2C bus 1, leaving the other bits unchanged
    def write_bits(self, register, value, left_bit_start, length):
        original = self.read_byte(register)
        # don't do anything if reading the byte has failed
        if original is None:
            return None
        new_value = self.merge_bits(original, value, left_bit_start, length)
        return self.write_byte(register, new_value)

    # writes a word to I2C
    def write_word(self, register, value):
        value_h = value >> 8
        value_l = value & 0xFF
        self.write_byte(register, value_h)
        return self.write_byte(register+1, value_l)

    # writes a byte to a register in I2C bus 1
    def write_byte(self, register, value):
        return self.i2c_line.write_byte_data(self.register_address, register, value)

    # reads a byte from I2C bus 1
    def read_byte(self, register):
        return self.i2c_line.read_byte_data(self.register_address, register)

    # reads a word from I2C bus 1
    def read_word(self, register):
        high = self.i2c_line.read_byte_data(self.register_address, register)
        low = self.i2c_line.read_byte_data(self.register_address, register + 1)
        val = (high << 8) + low
        return val

    # converts word reading into complement of 2
    def read_word_2c(self, register):
        val = self.read_word(register)
        if val >= 0x8000:
            return -((65535 - val) + 1)
        else:
            return val