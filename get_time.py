from datetime import datetime
from datetime import date

time_now = datetime.now()
date_today = date.today()

tempo_atual = time_now.strftime("%H:%M:%S")
data_atual = date_today.strftime("%d/%m/%Y")

print("Data: ", data_atual)
print("Hora atual: ", tempo_atual)
