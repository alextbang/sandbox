
# calculate total interest paid over the remainder of mortgage payoff period

print("Mortgage interest balance")
#
# number of months remaining to pay off mortgage
months = 78
#
# initial interest paid starting month, decreases monthly
interest = 639

# total interest paid over time
total = interest
 
while months > 0:
    interest-=8
    months-=1
    print("interest balance:", interest)
    total += interest
    #print(f"interest total: {total}")
 
print("Total interest paid:", total)

######################################
 
# print("Mortgage interest balance")
# months = 30
# interest = 639
# total = interest
 
# while months > 0:
#     interest-=8
#     months-=1
#     print("interest balance:", interest)
#     total += interest
#     #print(f"interest total: {total}")
 
# print("Total intrest paid:", total)

######################################