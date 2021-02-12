price = input("Вартісьть товару: ")
price = int(price)

taken = input('Отримано від покуця: ')
taken = int(taken)
здача = taken - price


if price > taken:
    print('дайте ще')
else:
    print('всьо ок')
    print('дякуюємо за покупки.Прихотьте ще.')
    print(f"Здача: {здача}")

while здача > 0:
    if здача >= 100:
        print("100 ")
        здача = здача - 100
    else:
        здача > 0
        print("1")
        здача = здача - 1
