import numpy_financial as npf

n = int(input("Enter the number of years: "))
cash_flows = []
print("Enter cash flows:")

for i in range(n + 1):
    if i == 0:
        value = float(input("Enter initial investment: "))
    else:
        value = float(input(f"Enter cash flow for year {i}: "))

    cash_flows.append(value)

req_irr = float(input("Enter required IRR (%): "))
irr = npf.irr(cash_flows)

irr_per= irr * 100

print("\n--- Project Evaluation ---")
print(f"Cash Flows: {cash_flows}")
print(f"Project IRR: {irr_per:.2f}%")
print(f"Required IRR: {req_irr:.2f}%")

if irr_per >= req_irr:
    print("Decision: ACCEPT THE PRJECT")
    print(f"Reason: IRR {irr_per} is higher than required return which is {req_irr}.")
else:
    print("Decision: REJECT THE PROJECT")
    print(f"Reason: IRR {irr_per} is lower than required return which is {req_irr}.")
