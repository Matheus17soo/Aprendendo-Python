# Carregue a data atual do computador e apresente somente a data
from datetime import datetime

data = datetime.now()
data = data.date()

print(data)