import requests
from requests.exceptions import Timeout, RequestException

url = "https://httpbin.org/get"

# افزودن timeout به درخواست
timeout = 10  # زمان حداکثر ۱۰ ثانیه برای اتصال و دریافت پاسخ

try:
    response = requests.get(url, timeout=timeout)
    # اگر درخواست موفق بود
    response.raise_for_status()  # چک کردن خطاهای HTTP (مثل 404، 500 و...)
    print("Request was successful!")
    print("Response Data:", response.json())
except Timeout:
    print(f"The request timed out after {timeout} seconds.")
except RequestException as e:
    print(f"An error occurred: {e}")