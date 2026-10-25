def cnvt_inr(usd):
    inr = usd * 82.74
    return inr

usd = float(input("Enter amount in USD: "))
inr = cnvt_inr(usd)
print("Amount in INR: ", inr)  