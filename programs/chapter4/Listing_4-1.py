from scipy import exp

# Wavelength of light
wl = float(input('Enter the wavelength (nm): '))

# Adaptation state
adpSt = input(
    'Adaptation State: Please enter the state of adaptation (p for photopic and s for scotopic): ')

# Radiometric to Photometric or Photometric to Radiometric?
tmpStr = str(
    'Conversion Direction: Please enter 1 to go from Radiometry to Photometry and 2 for Photometry to Radiometry: ')
iType = int(input(tmpStr))

# Enter the value of the input quantity
iVal = float(input('Value of the input quantity: '))
oVal = 0.0

if adpSt in 'sS':
    VStarLambda = exp(-321.9 * ((wl - 507) / 1000)**2)
elif adpSt in 'pP':
    VLambda = exp(-285.4 * ((wl - 555) / 1000)**2)

if iType == 1:
    # From Radiometry to Photometry
    if adpSt in 'sS':  # Scotopic
        oVal = iVal * 1704.0 * VStarLambda
    elif adpSt in 'pP':  # Photopic
        oVal = iVal * 683.0 * VLambda
    else:
        print('You entered an impossible value for Adaptation State.')
        print('Quitting')
elif iType == 2:
    # From Photometry to Radiometry
    if adpSt in 'sS':  # Scotopic
        oVal = iVal / (1704.0 * VStarLambda)
    elif adpSt in 'sS':  # Photopic
        oVal = iVal / (683.0 * VLambda)
    else:
        print('You entered an impossible value for Adaptation State.')
        print('Quitting')
else:
    print('You did not enter the correct values for the Conversion Direction.')
    print('Quitting.')


print('Input = %f, Output = %f' % (iVal, oVal))
