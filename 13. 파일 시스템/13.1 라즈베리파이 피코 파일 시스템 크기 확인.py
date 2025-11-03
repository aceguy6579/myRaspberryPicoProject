import os

stats = os.statvfs('/')

block_size = stats[0] # 블록 크기
total_block = stats[1] # 전체 블록의 수
free_block = stats[2] # 사용 가능한 블록의 수

print('Disk Space : ', block_size * total_block / 1024, 'kB')
print('Free Space : ', block_size * free_block / 1024, 'kB')