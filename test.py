
accessed = 0
m = {0 : 0, 1 : 0, 2: 0}
m_last = {0 : 0, 1 : 0, 2: 0}
size = 1
data_count = 0
data_size = 16
col_count = 3


for i in range(43690):
    for j in range(col_count):
        addr = (i + j*43690)*data_size
        data_count += 1
        if addr - m_last[j] > 63:
            accessed += 1
            m_last[j] = addr
print(f"Column-Store Accessed {accessed}, misses {((data_count*data_size)/64)}")



accessed = 0
m = {0 : 0, 1 : 0, 2: 0}
m_last = {0 : 0, 1 : 0, 2: 0}
size = 1

data_count = 0


for i in range(43690):
    for j in range(col_count):
        addr = (i*(data_size*col_count) + data_size * j)
        data_count += 1
        if addr - m_last[0] > 63:
            accessed += 1
            m_last[0] = addr

print(f"RME-Store Accessed {accessed}, misses {((data_count*data_size)/64)}")


accessed = 0
m = {0 : 0, 1 : 0, 2: 0}
m_last = {0 : 0, 1 : 0, 2: 0}
size = 1
data_count = 0

offsets = [0,24,48]
for i in range(43690):
    for j in range(col_count):
        addr = (i*64 + data_size + offsets[j])
        data_count += 1
        if addr - m_last[0] > 63:
            accessed += 1
            m_last[0] = addr

print(f"Row-Store Accessed {accessed}, misses {((data_count*data_size)/64)}")