import requests
from time import perf_counter
from concurrent.futures import ThreadPoolExecutor



# URL of the webpage you want to fetch
base_url = "https://multimediya.uz/multimediya/index.php?mavzu="

start = perf_counter()

for i in range(1, 13):
    # Send a GET request to the URL
    url = base_url + str(i)
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Get the content of the response
        web_content = response.content

        # Save the content to a file
        with open("html_single/" + str(i) + ".html", "wb") as f:
            f.write(web_content)
        print(f"{i}. Web content saved successfully as webpage.html")
    else:
        print("Failed to retrieve web content. Status code:", response.status_code)

finish = perf_counter()

print(f"Time: {finish - start: .3f} seconds")
# Time:  7.625 seconds


# URL of the webpage you want to fetch
base_url = "https://multimediya.uz/multimediya/index.php?mavzu="


def fetch_and_save_content(topic_number):
    url = base_url + str(topic_number)
    response = requests.get(url)

    if response.status_code == 200:
        web_content = response.content
        with open(f"html_multi/{topic_number}.html", "wb") as f:
            f.write(web_content)
        print(f"{topic_number}. Web content saved successfully as {
              topic_number}.html")
    else:
        print(f"Failed to retrieve web content for topic {
              topic_number}. Status code:", response.status_code)


start = perf_counter()

# Number of threads to use
num_threads = 5

# Create a ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=num_threads) as executor:
    # Schedule the tasks
    futures = [executor.submit(fetch_and_save_content, i)
               for i in range(1, 13)]

    # Wait for all tasks to complete
    for future in futures:
        future.result()

finish = perf_counter()

print(f"Time: {finish - start:.3f} seconds")        # 4.595 s


# import requests
# import time
# import threading
#
# x = 0
# base_url = "https://multimediya.uz/multimediya/index.php?mavzu="
#
#
# def get_html():
#     global x
#     x += 1
#     my_url = base_url + str(x)
#     response = requests.get(my_url)
#     print(my_url)
#     print(type(my_url))
#
#     if response.status_code == 200:
#         web_content = response.content
#
#         with open("html_multi/" + str(x) + ".html", "wb") as f:
#             f.write(web_content)
#         print(f"{x}. Web content saved successfully as webpage.html")
#     else:
#         print("Failed to retrieve web content. Status code:", response.status_code)
#
#
# start_time = time.perf_counter()
#
# # List of threads
# threads = []
# # base_url = "https://multimediya.uz/multimediya/index.php?mavzu="
# for i in range(1, 13):
#     # url = base_url + str(i)
#     # Create a thread for each PDF conversion task
#     t = threading.Thread(target=get_html)
#     threads.append(t)
#     t.start()
#
# # Wait for all threads to finish
# for t in threads:
#     t.join()
#
# finish = time.perf_counter()
# print(f"Time: {finish - start_time: .3f} seconds")
