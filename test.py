# myname = 'Joseph'
# text = f'My name is {myname}.'
# print(text)

# Menampilkan tgl dan waktu saat ini
from datetime import datetime
today = datetime.now()
# print(today)

# Menggunakan format
date = today.strftime("%Y-%m-%d %H:%M:%S")
print(date)