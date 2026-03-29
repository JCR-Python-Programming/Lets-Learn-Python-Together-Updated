msb=16_777_215,16_777_216  # most significant bits
lsb=8_388_607,8_388_608  # least significant bits

for i in range(msb[0],lsb[0],-1):
  bin=f'{i:b}'
  print('\n',len(f'{msb[0]-i:b}'),
    f'bits = Bin: {msb[0]-i:024b}\n\n',
    f'= Hex: {msb[0]-i:X}\n',
    f'= Oct: {msb[0]-i:o}\n',
    f'= Dec: {msb[0]-i:d}')

for i in range(lsb[1],msb[1]):
  bin=f'{i:b}'
  print('\n',len(f'{msb[0]:b}'),
    f'bits = Bin: {i:024b}\n\n',
    f'= Hex: {i:X}\n',
    f'= Oct: {i:o}\n',
    f'= Dec: {i:d}')

for i in range(msb[0],lsb[0],-1):
  bin=f'{i:b}'
  print('\n',len(f'{msb[0]-i:b}'),
    f'bits = Bin: {(i & 0xffffff):024b}\n\n',
    f'= Hex: -{msb[0]-i:X}\n',
    f'= Oct: -{msb[0]-i:o}\n',
    f'= Dec: -{msb[0]-i:d}')

for i in range(lsb[1],msb[1]):
  bin=f'{i:b}'
  print('\n',len(f'{msb[0]:b}'),
    f'bits = Bin: {(i & 0xffffff):024b}\n\n',
    f'= Hex: -{i:X}\n',
    f'= Oct: -{i:o}\n',
    f'= Dec: -{i:d}')
