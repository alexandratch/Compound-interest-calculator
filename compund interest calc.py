principle=0
rate=0
time=0
while True:
    principle=float(input("Enter a principle number:  "))
    if principle <0:
        print("Principle can't be less than 0")
    else:
        break

while True:
    rate= float(input("Enter the interest rate:  "))
    if rate<0:
        print("Interest rate can't be less than 0")
    else:
        break

while True:
    time=int(input("Enter the time in years:  "))
    if time < 0:
        print("Time can't be less than 0 years")
    else:
        break

total= principle * pow((1+ rate / 100), time)
print(f"Balance after {time} year/s is: ${total:.2f}")
