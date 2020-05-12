# Read from the str 'X-DSPAM-Confidence: 0.8475' and extract the number.

sent = 'X-DSPAM-Confidence: 0.8475'
pos = sent.find(':')
num = float(sent[pos+1:])
print(num)
