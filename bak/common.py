#coding=utf-8

class Pclass:

  varw = 'varw'
  _sex = 'man'
  
  def __init__(self, name = 'Li'):
    self.name = name
    self.addr = 'bei jin'
    # self._sex = 'man'
    self.__cai = 'caipiao'
    self.dic = {}
  
  def funa(self):
    print self.varw
    
  def funb(self):
    print self._sex
    
class Man(Pclass):
  """
    this is good class.
  """
  userinfo = {
    "name": "chen",
    "sex": "man",
    "age": 32,
    "addr": "北京朝阳区望京"
  }
  
  def __init__(self):
    # Pclass.__init__(self)
    self.addr = 'hg'
    
  def __getitem__(self, key):
    return self.data[key]
    
  def getaddr(self):
    print self.userinfo
    
  def getdic(self):
    print self.dic
    
def funb():
  print 'bbb'