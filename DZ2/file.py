import requests

num = int(input("Input count requests:"))
mas1=['web-6745ffd5c8-hmc7m', 'web-6745ffd5c8-sqljw', 'web-6745ffd5c8-wdvh']

ns1=0

for t in range(num):
  req = 'http://10.73.1.115' 
  resp = requests.get(req)
  resp = resp.text
  print (resp)
  for i in mas1:
    if resp.find(i) != -1:
      ns1 = ns1+1

ns2=num-ns1    

print ("Sum request:",num, "Request on current ingress:",ns1,"Canary:", ns2, sep='')
