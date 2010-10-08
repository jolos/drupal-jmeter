# very simple python script that parses the results of the tests
# and plots a scatter plot
# usage: change the query settings in query.py

import numpy as np
import matplotlib.pyplot as plt
import jmeter
from xml.sax import make_parser
from xml.sax.handler import feature_namespaces
import query

queries= query.queries

# Create a parser
parser = make_parser()


for query in queries:
  # Tell the parser we are not interested in XML namespaces
  parser.setFeature(feature_namespaces, 0)

  # Create the handler
  dh = jmeter.FindSample(query['label'])

  # Tell the parser to use our handler
  parser.setContentHandler(dh)

  # Parse the input
  parser.parse(query['file'])
  res = dh.getresults()
  y=[]
  x=[]
  start=res[0]['ts']
  for row in res:    
    x.append(row['ts']-start)
    if query['measure'] == 'elapsed':
      y.append(row['elapsed'])
    elif query['measure'] == 'latency':
      y.append(row['latency'])
  
  ynp=np.array(y)
  xnp=np.array(x)
  
  plt.scatter(xnp,ynp,c=query['color'],marker=query['marker'])

plt.show()
  