import struct
record_format = 'i20sif'
record_size = struct.calcsize(record_format)
with open("records.bin", "rb") as file:
    file.seek(record_size)
    data = file.read(record_size)