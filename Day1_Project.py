Verification = 'Request Initiated, kindly verify yourself.'
print(Verification)

#MK = True
name = input(f'Enter your name ' )
verify = ('Verification Confirmed.')
if name == "MK":
    print(verify)
    ask = input('How may I help you Sir?')
    if ask == '' :
        print("Aborted")
    else: print('Process Initiated')

else: print("User not Authorized")
