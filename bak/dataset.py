# dataset
import os

dirlist = os.listdir(r"d:\dj")
for el in dirlist:
  if os.path.isfile(el):
    print el
    print '>'
exit(0);

fp = open('a.txt')
print fp.readline()
fp.close()
exit(0);

fp = open('a.txt')
print fp.read()
fp.close()

exit(0);


fp = open('a.txt', 'a')
fp.write("chen jian ping\n")
fp.close()

exit(0);
imginfo = {
  "extname": ['jpg', 'png', 'gif', 'shift'],
  "color": (256, 1234, 345)
}

imginfo['extname'].append('qwe')
imginfo['chen'] = ('chen', 'jian', 'ping')
for v in imginfo['extname']:
  print v
  
  
for k, v in imginfo.items():
  print k, v