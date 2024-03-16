nric = input('Enter an NRIC number: ')
# Type your code below
list_S_T = ['J','Z','I','H','G','F','E','D','C','B','A']
list_F_G = ['X','W','U','T','R','Q','P','N','M','L','K']


nric = nric.upper()
if len(nric) != 9:
    print('NRIC is invalid.')

elif nric[0] not in ['S', 'T', 'F', 'G']:
    print('NRIC is invalid.')

elif  not nric[1:8].isdigit():
    print ('NRIC is invalid.')
   
else:
    nric_sum = int(nric[1])*2+int(nric[2])*7+int(nric[3])*6+int(nric[4])*5+int(nric[5])*4+int(nric[6])*3+int(nric[7])*2
    if nric[0] in ['T','G']:
        nric_sum = nric_sum+4
    nric_re = nric_sum % 11
    if nric[8] == list_S_T[nric_re] or nric[8] == list_F_G[nric_re]:
        print('NRIC is valid.')
    else:
        print('NRIC is invalid.')


    