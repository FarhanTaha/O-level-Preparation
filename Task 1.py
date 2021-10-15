#Prices
processorprice = 0
ramprice = 0
storageprice = 0
screenprice = 0
caseprice = 0
usbportsprice = 0

#conditions
x = 0
total = 0
y = True
percentage_vat_20 = 20 / 100

# program
while y:
    processor = input("Please select a processor: p3 / p5 / p7: ")
    if processor == "p3":
        processorprice += 100
        print(f'You chose the item {processor} and it\'s price is ${processorprice} ')
    elif processor == "p5":
        processorprice += 120
        print(f'You chose the item {processor} and it\'s price is ${processorprice} ')
    elif processor == "p7":
        processorprice += 200
        print(f'You chose the item {processor} and it\'s price is ${processorprice} ')
    else:
        x += 1
        print(f"Item missing or input invalid\nYour input was {processor}\nInput should be exactly: p3 / p5 / p7")

    ram = input("Please select a RAM: 16 GB / 32 GB: ")
    if ram == "16 GB":
        ramprice += 75
        print(f'You chose the item {ram} and it\'s price is ${ramprice} ')
    elif ram == "32 GB":
        ramprice += 150
        print(f'You chose the item {ram} and it\'s price is ${ramprice} ')
    else:
        x += 1
        print(f"Item missing or input invalid\nYour input was {ram}\nInput should be exactly: 16 GB / 32 GB")

    storage = input("Please select a Storage: 1 TB / 2 TB: ")
    if storage == "1 TB":
        storageprice += 50
        print(f'You chose the item {storage} and it\'s price is ${storageprice} ')
    elif storage == "2 TB":
        storageprice += 100
        print(f'You chose the item {storage} and it\'s price is ${storageprice} ')
    else:
        x += 1
        print(f"Item missing or input invalid\nYour input was {storage}\nInput should be exactly: 16 GB / 32 GB")

    screen = input("Please select a screen: 19\" / 23\" : ")
    if screen == "19\"":
        screenprice += 65
        print(f'You chose the item {screen} and it\'s price is ${screenprice} ')
    elif screen == "23\"":
        screenprice += 120
        print(f'You chose the item {screen} and it\'s price is ${screenprice} ')
    else:
        x += 1
        print(f"Item missing or input invalid\nYour input was {screen}\nInput should be exactly: 19\" / 23\" ")

    case = input("Please select a Case: Mini Tower / Midi Tower: ")
    if case == "Mini Tower":
        caseprice += 40
        print(f'You chose the item {case} and it\'s price is ${caseprice} ')
    elif case == "Midi Tower":
        caseprice += 70
        print(f'You chose the item {case} and it\'s price is ${caseprice} ')
    else:
        x += 1
        print(
            f"Item missing or input invalid\nYour input was {case}\nInput should be exactly: Mini Tower / Midi Tower ")

    usb = input("Please select amount of USB Ports: 2 ports / 4 ports: ")
    if usb == "2 ports":
        usbportsprice += 10
        print(f'You chose the item {usb} and it\'s price is ${usbportsprice} ')
    elif usb == "4 ports":
        usbportsprice += 20
        print(f'You chose the item {usb} and it\'s price is ${usbportsprice} ')
    else:
        x += 1
        print(f"Item missing or input invalid\nYour input was {usb}\nInput should be exactly: Mini Tower / Midi Tower ")

    # item missing condition code
    if x > 0:
        print(f"{x} Items are missing, can't take your order")
    elif x == 0:
        total = processorprice + ramprice + storageprice + screenprice + caseprice + usbportsprice + percentage_vat_20
        print(f'Your total price is: ${total} including 20% VAT')
    else:  # useless code, just used so that the program works fine
        print("")

    # to check if there is more orders up ahead
    question = input("Is there more orders?\nAns: ")
    if question == "No":  # if no, our program will not take another order
        y = False
    elif question == "Yes":  # if yes, then our program will take another order
        y = True
    else:
        print("Invalid input, please type in exactly: Yes / No")