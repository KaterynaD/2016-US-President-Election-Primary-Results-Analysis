import pandas as pd
from pandas import Series,DataFrame
import numpy as np

# source data
pr=pd.read_csv('primary_results.csv')
#pivoting
pr_piv= pr[['fips', 'candidate','fraction_votes']].pivot(index='fips', columns='candidate', values='fraction_votes')
pr_piv.drop(' No Preference', axis=1, inplace=True)
pr_piv.drop(' Uncommitted', axis=1, inplace=True)
pr_piv=pr_piv.dropna()
l=len(pr_piv.index)
pr_unpiv = DataFrame('',index=range(l*14),columns=['fips','fraction_votes','candidate'])

j=0
while j<len(pr_unpiv):
  for i in range(0,l-1):
    for c in pr_piv.columns:
      pr_unpiv.set_value(j, 'fips', pr_piv.index[i])
      pr_unpiv.set_value(j, 'fraction_votes', pr_piv.get_value(pr_piv.index[i],c))
      pr_unpiv.set_value(j, 'candidate', c)
      j+=1
pr_unpiv.to_csv('DataForTableau/primary_results_dropna.csv')
