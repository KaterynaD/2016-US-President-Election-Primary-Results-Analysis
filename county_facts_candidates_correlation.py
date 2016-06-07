
import pandas as pd
from pandas import Series,DataFrame
import numpy as np
from scipy.stats import linregress

# For Visualization
import matplotlib.pyplot as plt
import seaborn as sns
#for ipython
#%matplotlib osx

#output folder
OutputFolder='FactCandidateCorrelation/'
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

#multiindex  to make data more readable
c=pr[['party','candidate']].drop_duplicates().sort_values(by=['party','candidate'])
c = c.loc[c['candidate'] != ' No Preference']
c = c.loc[c['candidate'] != ' Uncommitted']
t=c[['party', 'candidate']].apply(tuple, axis=1).tolist()
index = pd.MultiIndex.from_tuples(t, names=['Democrat', 'Republican'])

#heatmap visualization
def heatmap(data,file_name):
  fig, ax = plt.subplots(figsize=(10, 10))
  heatmap = sns.heatmap(data, cmap=plt.cm.Blues,annot=True, annot_kws={"size": 8})
  ax.xaxis.tick_top()
  # rotate
  plt.xticks(rotation=90)
  plt.yticks(rotation=0)
  plt.tight_layout()
  fig.savefig(OutputFolder+file_name)

#if pythonw
#plt.show()

#skipy linregress
#Pearson Correlation
rvalue = DataFrame(np.nan,index=cf_dict.index,columns=index)
rvalue.columns.names=['Party','Candidate']
rvalue.columns.lexsort_depth
rvalue.index.names=['Fact']
#PValue
pvalue = DataFrame(np.nan,index=cf_dict.index,columns=index)
pvalue.columns.names=['Party','Candidate']
pvalue.columns.lexsort_depth
pvalue.index.names=['Fact']
#StdErr
stderr = DataFrame(np.nan,index=cf_dict.index,columns=index)
stderr.columns.names=['Party','Candidate']
stderr.columns.lexsort_depth
stderr.index.names=['Fact']


#
for c_X in pr_piv.columns:
  for c_Y in cf_dict.index:
    R=linregress(pr_facts[[c_X,c_Y]])
    p_X=index.get_loc_level(c_X,1)[1][0]
    rvalue.set_value(c_Y,(p_X,c_X), R.rvalue)
    pvalue.set_value(c_Y,(p_X,c_X), R.pvalue)
    stderr.set_value(c_Y,(p_X,c_X), R.stderr)

#It's a huge image and it's hard to review
heatmap(rvalue,'rvalue_facts.png')
heatmap(pvalue,'pvalue_facts.png')
heatmap(stderr,'stderr_facts.png')

#Let's find out the most correlated facts to Democrat candidates choice
#democrats only

DemRvalue=rvalue['Democrat']
DemPvalue=pvalue['Democrat']
DemStdErr=stderr['Democrat']

DemRvalue_idxmax=DemRvalue.idxmax(axis=0)

DemRvalue_max = DataFrame(np.nan,index=DemRvalue_idxmax.tolist(),columns=DemRvalue_idxmax.index)
DemRvalue_max['description']=''

DemPvalue_max = DataFrame(np.nan,index=DemRvalue_idxmax.tolist(),columns=DemRvalue_idxmax.index)
DemPvalue_max['description']=''

DemStdErr_max = DataFrame(np.nan,index=DemRvalue_idxmax.tolist(),columns=DemRvalue_idxmax.index)
DemStdErr_max['description']=''


for c_X in DemRvalue_idxmax.index:
    for c_Y in DemRvalue_idxmax.tolist():
        DemRvalue_max.set_value(c_Y,c_X, DemRvalue[c_X][c_Y])
        DemRvalue_max.set_value(c_Y,'description', cf_dict['description'][c_Y])

        DemPvalue_max.set_value(c_Y,c_X, DemPvalue[c_X][c_Y])
        DemPvalue_max.set_value(c_Y,'description', cf_dict['description'][c_Y])

        DemStdErr_max.set_value(c_Y,c_X, DemStdErr[c_X][c_Y])
        DemStdErr_max.set_value(c_Y,'description', cf_dict['description'][c_Y])


DemRvalue_max=DemRvalue_max.set_index('description')
heatmap(DemRvalue_max,'DemRvalue_max.png')

DemPvalue_max=DemPvalue_max.set_index('description')
heatmap(DemPvalue_max,'DemPvalue_max.png')

DemStdErr_max=DemStdErr_max.set_index('description')
heatmap(DemStdErr_max,'DemStdErr_max.png')


#Most anticorrelated facts to Democrat candidates choice

DemRvalue_idxmin=DemRvalue.idxmin(axis=0)

DemRvalue_min = DataFrame(np.nan,index=DemRvalue_idxmin.tolist(),columns=DemRvalue_idxmin.index)
DemRvalue_min['description']=''

DemPvalue_min = DataFrame(np.nan,index=DemRvalue_idxmin.tolist(),columns=DemRvalue_idxmin.index)
DemPvalue_min['description']=''

DemStdErr_min = DataFrame(np.nan,index=DemRvalue_idxmin.tolist(),columns=DemRvalue_idxmin.index)
DemStdErr_min['description']=''


for c_X in DemRvalue_idxmin.index:
    for c_Y in DemRvalue_idxmin.tolist():
        DemRvalue_min.set_value(c_Y,c_X, DemRvalue[c_X][c_Y])
        DemRvalue_min.set_value(c_Y,'description', cf_dict['description'][c_Y])

        DemPvalue_min.set_value(c_Y,c_X, DemPvalue[c_X][c_Y])
        DemPvalue_min.set_value(c_Y,'description', cf_dict['description'][c_Y])

        DemStdErr_min.set_value(c_Y,c_X, DemStdErr[c_X][c_Y])
        DemStdErr_min.set_value(c_Y,'description', cf_dict['description'][c_Y])


DemRvalue_min=DemRvalue_min.set_index('description')
heatmap(DemRvalue_min,'DemRvalue_min.png')

DemPvalue_min=DemPvalue_min.set_index('description')
heatmap(DemPvalue_min,'DemPvalue_min.png')

DemStdErr_min=DemStdErr_min.set_index('description')
heatmap(DemStdErr_min,'DemStdErr_min.png')



#republicans only
#most correlated facts to Republican candidates choice

RepRvalue=rvalue['Republican']
RepPvalue=pvalue['Republican']
RepStdErr=stderr['Republican']

RepRvalue_idxmax=RepRvalue.idxmax(axis=0)

RepRvalue_max = DataFrame(np.nan,index=list(set(RepRvalue_idxmax.tolist())),columns=RepRvalue_idxmax.index)
RepRvalue_max['description']=''

RepPvalue_max = DataFrame(np.nan,index=list(set(RepRvalue_idxmax.tolist())),columns=RepRvalue_idxmax.index)
#RepPvalue_max['description']=''

RepStdErr_max = DataFrame(np.nan,index=list(set(RepRvalue_idxmax.tolist())),columns=RepRvalue_idxmax.index)
#RepStdErr_max['description']=''


for c_X in RepRvalue_idxmax.index:
    for c_Y in RepRvalue_idxmax.tolist():
        RepRvalue_max.set_value(c_Y,c_X, RepRvalue[c_X][c_Y])
        RepRvalue_max.set_value(c_Y,'description', cf_dict['description'][c_Y])

        RepPvalue_max.set_value(c_Y,c_X, RepPvalue[c_X][c_Y])
        #RepPvalue_max.set_value(c_Y,'description', cf_dict['description'][c_Y])

        RepStdErr_max.set_value(c_Y,c_X, RepStdErr[c_X][c_Y])
        #RepStdErr_max.set_value(c_Y,'description', cf_dict['description'][c_Y])


RepRvalue_max=RepRvalue_max.set_index('description')
heatmap(RepRvalue_max,'RepRvalue_max.png')

#RepPvalue_max=RepPvalue_max.set_index('description')
heatmap(RepPvalue_max,'RepPvalue_max.png')

#RepStdErr_max=RepStdErr_max.set_index('description')
heatmap(RepStdErr_max,'RepStdErr_max.png')




#most anticorrelated facts to Republican candidates choice
RepRvalue=rvalue['Republican']
RepPvalue=pvalue['Republican']
RepStdErr=stderr['Republican']

RepRvalue_idxmin=RepRvalue.idxmin(axis=0)

RepRvalue_min = DataFrame(np.nan,index=list(set(RepRvalue_idxmin.tolist())),columns=RepRvalue_idxmin.index)
RepRvalue_min['description']=''

RepPvalue_min = DataFrame(np.nan,index=list(set(RepRvalue_idxmin.tolist())),columns=RepRvalue_idxmin.index)
#RepPvalue_min['description']=''

RepStdErr_min = DataFrame(np.nan,index=list(set(RepRvalue_idxmin.tolist())),columns=RepRvalue_idxmin.index)
#RepStdErr_min['description']=''


for c_X in RepRvalue_idxmin.index:
    for c_Y in RepRvalue_idxmin.tolist():
        RepRvalue_min.set_value(c_Y,c_X, RepRvalue[c_X][c_Y])
        RepRvalue_min.set_value(c_Y,'description', cf_dict['description'][c_Y])

        RepPvalue_min.set_value(c_Y,c_X, RepPvalue[c_X][c_Y])
        #RepPvalue_min.set_value(c_Y,'description', cf_dict['description'][c_Y])

        RepStdErr_min.set_value(c_Y,c_X, RepStdErr[c_X][c_Y])
        #RepStdErr_min.set_value(c_Y,'description', cf_dict['description'][c_Y])


RepRvalue_min=RepRvalue_min.set_index('description')
heatmap(RepRvalue_min,'RepRvalue_min.png')

#RepPvalue_min=RepPvalue_min.set_index('description')
heatmap(RepPvalue_min,'RepPvalue_min.png')

#RepStdErr_min=RepStdErr_min.set_index('description')
heatmap(RepStdErr_min,'RepStdErr_min.png')

#More details for most anticorrelated Republican candidates

#Bachelor's degree or higher, percent of persons age 25+, 2009-2013
sns_plot = sns.jointplot('Marco Rubio','EDU685213',pr_facts,kind='scatter')
sns_plot.savefig(OutputFolder+'MarcoRubio_EDU685213_joinplot.png')

sns_plot = sns.jointplot('Donald Trump','EDU685213',pr_facts,kind='scatter')
sns_plot.savefig(OutputFolder+'DonaldTrump_EDU685213_joinplot.png')

#Housing units in multi-unit structures
sns_plot = sns.jointplot('Marco Rubio','HSG096213',pr_facts,kind='scatter')
sns_plot.savefig(OutputFolder+'MarcoRubio_HSG096213_joinplot.png')


sns_plot = sns.jointplot('Donald Trump','HSG096213',pr_facts,kind='scatter')
sns_plot.savefig(OutputFolder+'DonaldTrump_HSG096213_joinplot.png')

#Persons 65 years and over, percent, 2014
sns_plot = sns.jointplot('Marco Rubio','AGE775214',pr_facts,kind='scatter')
sns_plot.savefig(OutputFolder+'MarcoRubio_AGE775214_joinplot.png')


sns_plot = sns.jointplot('Donald Trump','AGE775214',pr_facts,kind='scatter')
sns_plot.savefig(OutputFolder+'DonaldTrump_AGE775214_joinplot.png')
