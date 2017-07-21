
def compute_payment(hrs, rate):
    if hrs > 40:
        payment = rate * hrs * 2
    elif hrs < 40:
        payment = rate * hrs
    else:
        print('Please enter valid hours or rate')

    print("Need to Pay: ", payment)

try:
    inp = input("Enter hours: ")
    hrs = float(inp)
    inp2 = input("Enter rate: ")
    rate = float(inp2)
    compute_payment(hrs, rate)
except:
    print("Not valid entries.")
    quit()






