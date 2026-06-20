str = 'X-DSPAM-Confidence: 0.8475'

atpos = str.find(":")
number = str[atpos+1:]
print(float(number))