<b>Data Source</b>: <a href="https://www.kaggle.com/benhamner/2016-us-election">Kaggle 2016 US Presidential Election dataset</a>

<ol>
<li><b>primary_results_candidates_correlation.py</b> explores the correlations between candidates based on votes fractions they have in the same counties.
The results are saved in CandidateCorrelation folder
<ol>
<li> Most two anti-correlated Democrat party candidates are Hillary Clinton and Bernie Sanders. The script calculates Pearson correlation coeficient, PValue and StdErr
<img src="https://raw.githubusercontent.com/KaterynaD/2016USPresidentElectionPrimaryResultsAnalysis/master/CandidateCorrelation/dem_rvalue.png">
<p>Here is the <a href="https://raw.githubusercontent.com/KaterynaD/2016USPresidentElectionPrimaryResultsAnalysis/master/CandidateCorrelation/dem_pvalue.png">Pvalue</a>
 and <a href="https://raw.githubusercontent.com/KaterynaD/2016USPresidentElectionPrimaryResultsAnalysis/master/CandidateCorrelation/dem_stderr.png">StdErr</a>
<p>Here is the joinplot of these two candidates:
<p><img src="https://raw.githubusercontent.com/KaterynaD/2016USPresidentElectionPrimaryResultsAnalysis/master/CandidateCorrelation/HillaryClinton_BernieSanders_joinplot.png">

<li>The more interesting question is anti-correlated Repupublican candidates. According to my analysis they are:
<ul>
<li>Donald Trump and Marco Rubio
<li>Marco Rubio and Ted Cruz
</ul>
<p>Both pairs have -0.49 Rvalue. The next pair is Marco Rubio and Mike Huckabee with -0.42 Rvalue
The data has strong negative correlation, and it's significant as p-value is a lot lesser than 0.001

<p><img src="https://raw.githubusercontent.com/KaterynaD/2016USPresidentElectionPrimaryResultsAnalysis/master/CandidateCorrelation/rep_rvalue.png">

<p>Here is the <a href="https://raw.githubusercontent.com/KaterynaD/2016USPresidentElectionPrimaryResultsAnalysis/master/CandidateCorrelation/rep_pvalue.png">Pvalue</a>
 and <a href="https://raw.githubusercontent.com/KaterynaD/2016USPresidentElectionPrimaryResultsAnalysis/master/CandidateCorrelation/rep_stderr.png">StdErr</a>

<p>Here are the joinplots of two first pairs:
<ul>
<li><img src="https://raw.githubusercontent.com/KaterynaD/2016USPresidentElectionPrimaryResultsAnalysis/master/CandidateCorrelation/DonaldTrump_MarcoRubio_joinplot.png">
<li><img src="https://raw.githubusercontent.com/KaterynaD/2016USPresidentElectionPrimaryResultsAnalysis/master/CandidateCorrelation/MarcoRubio_TedCruz_joinplot.png">
</ul>
<li> Primary results assume a choice between Democrats candidates only or Republican candidates only
So comparing Democrats to Republicans based on these results does not have a lot of sense
However let's look on the picture as a whole

<p><img src="https://raw.githubusercontent.com/KaterynaD/2016USPresidentElectionPrimaryResultsAnalysis/master/CandidateCorrelation/rvalue.png">
<p>or in this <a href="https://raw.githubusercontent.com/KaterynaD/2016USPresidentElectionPrimaryResultsAnalysis/master/CandidateCorrelation/corrplot.png">view</a>


<p>Let's look now how high is the <a href="https://raw.githubusercontent.com/KaterynaD/2016USPresidentElectionPrimaryResultsAnalysis/master/CandidateCorrelation/pvalue.png">PValue</a> for correlations between democrat and republican candidates
We can not trust such results

<li> And at the end the pairplot for the data set:

<p><a href="https://raw.githubusercontent.com/KaterynaD/2016USPresidentElectionPrimaryResultsAnalysis/master/CandidateCorrelation/pairplot.png"><img height=50 width= 50 src="https://raw.githubusercontent.com/KaterynaD/2016USPresidentElectionPrimaryResultsAnalysis/master/CandidateCorrelation/pairplot.png"></a>
</ol>

<li> <b>county_facts_candidates_correlation.py</b> explores the correlations between candidates and county facts based on votes fractions they have in each county.
The results are saved in FactCandidateCorrelation folder
<ol>
<li> There is a strong correlation between percent of Asian and Bernie Sanders votes fraction. In the opposite, Hillary Clinton has anti-correlation with Asian percent and stong positive correlation with White percent.

<p><img src="https://raw.githubusercontent.com/KaterynaD/2016USPresidentElectionPrimaryResultsAnalysis/master/FactCandidateCorrelation/DemRvalue_max.png">

<p>The <a href="https://raw.githubusercontent.com/KaterynaD/2016USPresidentElectionPrimaryResultsAnalysis/master/FactCandidateCorrelation/DemPvalue_max.png">PValue</a> is small enough to trust the results

<li> Here is the similar analysis for republicans. the results are more sparse but what we can see the strong positive relationship
between percent of Housing units in multi-unit structures and votes fractions of John Kasich, <a href="https://raw.githubusercontent.com/KaterynaD/2016USPresidentElectionPrimaryResultsAnalysis/master/FactCandidateCorrelation/MarcoRubio_HSG096213_joinplot.png">Marco Rubio</a> and Rand Paul.

<p>There is also the strong correlation between percent of <a href="https://raw.githubusercontent.com/KaterynaD/2016USPresidentElectionPrimaryResultsAnalysis/master/FactCandidateCorrelation/MarcoRubio_EDU685213_joinplot.png">Bachelor's degree or higher and the same republican candidates</a>

<p>The <a href="https://raw.githubusercontent.com/KaterynaD/2016USPresidentElectionPrimaryResultsAnalysis/master/FactCandidateCorrelation/RepPvalue_max.png">PValue</a> is very low and we can trust the results.

<p>Interesting, <a href="https://raw.githubusercontent.com/KaterynaD/2016USPresidentElectionPrimaryResultsAnalysis/master/FactCandidateCorrelation/DonaldTrump_EDU685213_joinplot.png">Donald Trump</a> has the strong anti-correlated results with the percent of Bachelor's degree or higher Fact with a low PValue

<p>He has a moderate positive correlation with the percent of Persons 65 years and over. However the PValue is high in this case

<a href="https://raw.githubusercontent.com/KaterynaD/2016USPresidentElectionPrimaryResultsAnalysis/master/FactCandidateCorrelation/MarcoRubio_AGE775214_joinplot.png">Marco Rubio</a> fraction votes is strongly anti-correlated with the percent of Persons 65 years and over fact and PValue is very low.


<p><img src="https://raw.githubusercontent.com/KaterynaD/2016USPresidentElectionPrimaryResultsAnalysis/master/FactCandidateCorrelation/RepRvalue_max.png">

<li> Here is the full picture: <a href="https://raw.githubusercontent.com/KaterynaD/2016USPresidentElectionPrimaryResultsAnalysis/master/FactCandidateCorrelation/rvalue_facts.png">RValue</a> and <a href="https://raw.githubusercontent.com/KaterynaD/2016USPresidentElectionPrimaryResultsAnalysis/master/FactCandidateCorrelation/pvalue_facts.png">Pvalue</a>
The fact dictionary is <a href="https://github.com/KaterynaD/2016USPresidentElectionPrimaryResultsAnalysis/blob/master/SourceData/county_facts_dictionary.csv">here</a>.
</ol>
<li><b>The rest of scripts</b> were used to generate data for <a href="https://public.tableau.com/views/2016ElectionPrimaryResults/CandidateCorrelationHeatmap?:embed=y&:display_count=yes&:showTabs=y">Tableau</a>

</ol>


 
 
 <script type='text/javascript' src='https://public.tableau.com/javascripts/api/viz_v1.js'></script><div class='tableauPlaceholder' style='width: 982px; height: 745px;'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;20&#47;2016ElectionPrimaryResults&#47;CandidateCorrelationHeatmap&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz' width='982' height='745' style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='site_root' value='' /><param name='name' value='2016ElectionPrimaryResults&#47;CandidateCorrelationHeatmap' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;20&#47;2016ElectionPrimaryResults&#47;CandidateCorrelationHeatmap&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='showTabs' value='y' /></object></div>
