
import pandas as pd
from pandas import Series,DataFrame
import numpy as np
from scipy.stats import linregress


# source data
pr=pd.read_csv('primary_results.csv')
#pivoting
pr_piv= pr[['fips', 'candidate','fraction_votes']].pivot(index='fips', columns='candidate', values='fraction_votes')
pr_piv.drop(' No Preference', axis=1, inplace=True)
pr_piv.drop(' Uncommitted', axis=1, inplace=True)
pr_piv=pr_piv.dropna()
c=pr[['candidate','party']].drop_duplicates().sort_values(by=['candidate','party'])
t=c[['candidate','party']].apply(tuple, axis=1).tolist()
d=dict(t)

#skipy linregress
l=len(pr_piv.columns)
linregress_unpiv = DataFrame('',index=range(l),columns=['party1','candidate1','party2','candidate2','Rvalue','Pvalue','StdError','Slope','Intercept'])
i=0
for c_X in pr_piv.columns:
  for c_Y in pr_piv.columns:
    R=linregress(pr_piv[[c_X,c_Y]])
    #
    linregress_unpiv.set_value(i,'party1',d[c_X])
    linregress_unpiv.set_value(i,'candidate1',c_X)
    linregress_unpiv.set_value(i,'party2',d[c_Y])
    linregress_unpiv.set_value(i,'candidate2',c_Y)
    linregress_unpiv.set_value(i,'Rvalue',R.rvalue)
    linregress_unpiv.set_value(i,'Pvalue',R.pvalue)
    linregress_unpiv.set_value(i,'StdError',R.stderr)
    linregress_unpiv.set_value(i,'Slope',R.slope)
    linregress_unpiv.set_value(i,'Intercept',R.intercept)
    i+=1
linregress_unpiv.to_csv('DataForTableau/primary_results_linregress.csv')
