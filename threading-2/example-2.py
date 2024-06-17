import concurrent.futures
import time
import requests

start = time.perf_counter()

URL = "https://mytests.uz/api/user/"

def get_data(user_id):
    url = URL+str(user_id)
    respons = requests.get(url)
    return respons.text

# ikkinchi usul (birinchidan tez, uchinchidan bazan sekin bazan tez(katta malumotlarni olishda 3 dan tez bolishi mumkin))
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = range(200)
    results = executor.map(get_data, secs)

    for result in results:
        print(result)

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} second(s)")
