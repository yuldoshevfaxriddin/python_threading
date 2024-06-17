import time
import requests

start = time.perf_counter()

URL = "https://mytests.uz/api/user/"

def get_data(user_id):
    url = URL+str(user_id)
    respons = requests.get(url)
    return respons.text

# internetdan malumotlarni olish
# birinchi usul (ancha sekin)
for user_id in range(20):
    text = get_data(user_id)
    print(text)

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} second(s)")
