import time
import requests
import threading

start = time.perf_counter()

URL = "https://mytests.uz/api/user/"

def get_data(user_id):
    url = URL+str(user_id)
    respons = requests.get(url)
    print(respons.text)

# uchinchi usul(birinchi va ikkinchidan tez(katta malumotlarni olishda 2 dan sekin bolishi mumkin)) 
threads = []
for user_id in range(200):
    t = threading.Thread(target=get_data, args=[user_id])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} second(s)")
