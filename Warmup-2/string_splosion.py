#Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
  new = ""
  for i in range(0, len(str)):
      new =  new + str[:i+1] 
      print(new)

string_splosion('Code') # 'CCoCodCode'
string_splosion('abc') # 'aababc'
string_splosion('ab') # 'aab'
string_splosion('fade')