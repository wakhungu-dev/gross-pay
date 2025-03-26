from random import randint
from time import sleep
while True:
    temperature = randint(0, 100)
    if temperature > 90:
        color = 'red'
    elif temperature < 70 and temperature >= 70:
        color = 'yellow'
    elif temperature < 70 and temperature >= 50:
        color = 'green' 
    else:
        color = 'blue'

    page = f"""<meta http-equiv="refresh" content="2">
    <h1>Temp sensor</h1>
    <p style="color:{color};">Temperature: {temperature}</p>
    """
    with open("index.html", "w") as f:
        f.write(page)   

        print(temperature)
        print(color)
        sleep(1)
             
