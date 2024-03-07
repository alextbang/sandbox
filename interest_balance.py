
# # calculate total interest paid over the remainder of mortgage payoff period
#
# print("Mortgage interest balance")
# #
# # number of months remaining to pay off mortgage
# months = 78
# #
# # amount of intest paid each month, decreases monthly

# interest = 639

# total = interest
 
# while months > 0:
#     diff = interest - 8
#     interest = diff
#     months-=1
#     # total = interest + diff
#     print("interest balance:", interest)
#     total += interest
#     #print(f"interest total: {total}")
 
# print("Total intrest paid:", total)

######################################
 
print("Mortgage interest balance")
months = 30
interest = 639
total = interest
 
while months > 0:
    diff = interest - 8
    interest = diff
    months-=1
    # total = interest + diff
    print("interest balance:", interest)
    total += interest
    #print(f"interest total: {total}")
 
print("Total intrest paid:", total)
######################################