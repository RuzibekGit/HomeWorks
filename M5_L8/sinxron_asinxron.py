import os
import requests
import asyncio

# Sinxron dasturlash bu dastur ishlashdan navbati bilan vazifani bajarsa va malum bir vazifa bajarilmaguncha keyingisiga otmaydi

# Asinxron dastur malum bir vazifa bajarilishda kutish xosil bolsa kutish vaqtida boshqa vazifani bajaradi va run time ni tezlashtiradi


url = "https://multimediya.uz/multimediya/index.php?mavzu="


def webpage(url: str):
    response = requests.get(url)
    print(response.content)

def main():
    for i in range(1, 13):
        webpage(f"{url}{i}")


# if __name__ == "__main__":
#     main()

# -----------------------------------------------------------------------------

def webpage(id: int):  # synchron program
    response = requests.get(f"{url}{id}")

    with open(f"{id}.html", "wd") as file:
        file.write(response.content)
    print(f"{id} - saved HTML")


def main():
    for i in range(1, 13):
        webpage(i)


# if __name__ == "__main__":
#     main()

# -----------------------------------------------------------------------------

async def webpage(id: int):  # asynchron program
    await asyncio.sleep(0.001)
    print(f"{id}. Start fetching...")

    response = requests.get(f"{url}{id}")

    with open(f'sinov={id}.html', 'wb') as file:
        file.write(response.content)
    print(f"{id}. saved as HTML")


async def main():
    tasks = []
    for i in range(1, 13):
        tasks.append(asyncio.create_task(webpage(i)))

    for task in tasks:
        await task

    print("Finish !... ")


if __name__ == "__main__":
    asyncio.run(main())



