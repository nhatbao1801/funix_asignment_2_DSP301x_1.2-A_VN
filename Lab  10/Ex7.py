import re

str="""Some of the prices were as following TSLA:749.50, ORCL: 50.50, GE: 10.90, MSFT: 170.50, BIDU: 121.40. As the macroeconomic developments continue we will update the prices. """

#Type your answer here.

regex='[a-zA-Z0-9+._-]+:'
data=re.findall(regex, str)


print(data)

