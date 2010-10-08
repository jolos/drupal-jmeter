from xml.sax import saxutils

class FindSample(saxutils.handler.ContentHandler):
  def __init__(self,label):
    self.label = label
    self.results =[]
    
  def startElement(self,name,attrs):
  
    if name != 'httpSample': return
    
    label = attrs.get('lb',"")
    if label == self.label:
      row={}
      row['ts']=int(attrs.get('ts',""))
      row['elapsed']=int(attrs.get('t',""))
      row['latency']=int(attrs.get('lt',""))
      self.results.append(row)
      
  
  def getresults(self):
    return self.results