from math import ceil, log
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--payment", type=int)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)

args_d = parser.parse_args()
args = {}
for i in ("type", "payment", "principal", "periods", "interest"):
    if vars(args_d)[i] is not None:
        args[i] = vars(args_d)[i]


if "interest" in args and len(args) == 4:
    summary = 0
    i = (float(args["interest"]) / 100) / 12
    if args["type"] == "diff":
        if "periods" in args:
            p = int(args["principal"])
            n = int(args["periods"])
            if n > 0:
                for m in range(1, n + 1):
                    diff_pay = ceil(p / n + i * (p - (p*(m-1)) / n))
                    summary += diff_pay
                    print(f"Month {m}: payment is {diff_pay}")
                print(f"Overpayment = {summary - p}")
            else:
                print("Incorrect parameters")
    elif args["type"] == "annuity":
        if "periods" in args and "principal" in args:
            p = int(args["principal"])
            n = int(args["periods"])
            m_payment = ceil(p * (i * (1 + i) ** n) / ((1 + i) ** n - 1))
            print(f"Your annuity payment = {m_payment}!")
            print(f"Overpayment = {ceil(m_payment * n - p)}")
        elif "payment" in args and "periods" in args:
            payment = int(args["payment"])
            n = int(args["periods"])
            p = payment / ((i * (1 + i) ** n) / ((1+i) ** n - 1))
            print(f"Your loan principal = {p}!")
            print(f"Overpayment = {payment * n - p}")
        elif "payment" in args and "principal" in args:
            p = int(args["principal"])
            payment = int(args["payment"])
            n = ceil(log((payment / (payment - i * p)), 1 + i))
            years, months = divmod(n, 12)
            if years and months:
                print(f"It will take {years} years and {months} months to repay this loan!")
            elif months:
                print(f"It will take {months} months to repay this loan!")
            else:
                print(f"It will take {years} years to repay this loan!")
            print(f"Overpayment = {payment * n - p}")
    else:
        print("Incorrect parameters")

else:
    print("Incorrect parameters")