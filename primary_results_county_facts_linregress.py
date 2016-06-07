
import pandas as pd
from pandas import Series,DataFrame
import numpy as np
from scipy.stats import linregress


# source data
pr=pd.read_csv('SourceData/primary_results.csv')
facts=pd.read_csv('SourceData/county_facts.csv')
facts=facts.set_index('fips')
cf_dict=pd.read_csv('SourceData/county_facts_dictionary.csv')
cf_dict=cf_dict.set_index('column_name')
#pivoting and drop Null values for clean and easy analysis
pr_piv= pr[['fips', 'candidate','fraction_votes']].pivot(index='fips', columns='candidate', values='fraction_votes')
pr_piv.drop(' No Preference', axis=1, inplace=True)
pr_piv.drop(' Uncommitted', axis=1, inplace=True)
pr_facts=pd.merge(pr_piv, facts, right_index=True, left_index=True)
pr_facts=pr_facts.dropna()
c=pr[['candidate','party']].drop_duplicates().sort_values(by=['candidate','party'])
t=c[['candidate','party']].apply(tuple, axis=1).tolist()
d=dict(t)

#skipy linregress
l=len(pr_facts.columns)
linregress_unpiv = DataFrame('',index=range(l),columns=['party','candidate','fact','Rvalue','Pvalue','StdError','Slope','Intercept'])
i=0
for c_X in pr_piv.columns:
  for c_Y in cf_dict.index:
    R=linregress(pr_facts[[c_X,c_Y]])
    #
    linregress_unpiv.set_value(i,'party',d[c_X])
    linregress_unpiv.set_value(i,'candidate',c_X)
    linregress_unpiv.set_value(i,'fact',c_Y)
    linregress_unpiv.set_value(i,'Rvalue',R.rvalue)
    linregress_unpiv.set_value(i,'Pvalue',R.pvalue)
    linregress_unpiv.set_value(i,'StdError',R.stderr)
    linregress_unpiv.set_value(i,'Slope',R.slope)
    linregress_unpiv.set_value(i,'Intercept',R.intercept)
    i+=1
linregress_unpiv.to_csv('DataForTableau/primary_results_county_facts_linregress.csv')
