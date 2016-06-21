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
<li><b>LinearRegression.py</b> predicts primary results fraction votes based on demographic county facts.
Hillary Clinton and Bernie Sanders fraction votes are most correlated to the county facts.
The variance is above 0.6 for these 2 candidates. The quality of the predicted values for the rest of the candidates
is low with 0.4 and less varience values.

<p>Ordinary least squares method works perfectly fine fo the data. The rest of the method can give a slightly better results but not very significant
<p>Hillary Clinton fraction votes prediction residual plot for ordinary least squares method, not normalize data

<p><img src="https://raw.githubusercontent.com/KaterynaD/2016-US-President-Election-Primary-Results-Analysis/master/LinearRegressionPredictionPrimary/ols_Residual_plot_Hillary_Clinton.png">

<p>Hillary Clinton prediction joint plot for ordinary least squares method, not normalize data

<p><img src="https://raw.githubusercontent.com/KaterynaD/2016-US-President-Election-Primary-Results-Analysis/master/LinearRegressionPredictionPrimary/ols_Jointplot_Hillary_Clinton.png">

<p>The files with the predicted data and plots for each candidates can be found in LinearRegressionPredictionPrimary folder
<p><b>Other candidates prediction data models fit for different methods and parameters.</b>
More data can be found <a href="https://github.com/KaterynaD/2016-US-President-Election-Primary-Results-Analysis/blob/master/LinearRegressionPredictionPrimary/results.csv">here</a>
<br>  <table border=1>
  <thead><tr><th title="Field #1">candidate</th>
  <th title="Field #2">method</th>
  <th title="Field #3">normalize</th>
  <th title="Field #4">MSE Train set</th>
  <th title="Field #5">MSE Test set</th>
  <th title="Field #6">Variance</th>
  </tr></thead>
  <tbody><tr><td>Hillary Clinton</td>
  <td>LeastSquares </td>
  <td>Y</td>
  <td align="right">0.011</td>
  <td align="right">0.011</td>
  <td align="right">0.614</td>
  </tr>
  <tr><td>Hillary Clinton</td>
  <td>LeastSquares </td>
  <td>N</td>
  <td align="right">0.011</td>
  <td align="right">0.011</td>
  <td align="right">0.614</td>
  </tr>
  <tr><td>Hillary Clinton</td>
  <td>Ridge 0.010  </td>
  <td>Y</td>
  <td align="right">0.011</td>
  <td align="right">0.011</td>
  <td align="right">0.616</td>
  </tr>
  <tr><td>Hillary Clinton</td>
  <td>Ridge 0.010  </td>
  <td>N</td>
  <td align="right">0.011</td>
  <td align="right">0.011</td>
  <td align="right">0.614</td>
  </tr>
  <tr><td>Hillary Clinton</td>
  <td>Lasso 0.000  </td>
  <td>Y</td>
  <td align="right">0.012</td>
  <td align="right">0.011</td>
  <td align="right">0.627</td>
  </tr>
  <tr><td>Hillary Clinton</td>
  <td>Lasso 0.000  </td>
  <td>N</td>
  <td align="right">0.011</td>
  <td align="right">0.011</td>
  <td align="right">0.618</td>
  </tr>
  <tr><td>Hillary Clinton</td>
  <td>BayesianRidge</td>
  <td>Y</td>
  <td align="right">0.011</td>
  <td align="right">0.011</td>
  <td align="right">0.620</td>
  </tr>
  <tr><td>Hillary Clinton</td>
  <td>BayesianRidge</td>
  <td>N</td>
  <td align="right">0.011</td>
  <td align="right">0.011</td>
  <td align="right">0.610</td>
  </tr>
  <tr><td>Bernie Sanders</td>
  <td>LeastSquares </td>
  <td>Y</td>
  <td align="right">0.010</td>
  <td align="right">0.010</td>
  <td align="right">0.642</td>
  </tr>
  <tr><td>Bernie Sanders</td>
  <td>LeastSquares </td>
  <td>N</td>
  <td align="right">0.010</td>
  <td align="right">0.010</td>
  <td align="right">0.642</td>
  </tr>
  <tr><td>Bernie Sanders</td>
  <td>Ridge 0.010  </td>
  <td>Y</td>
  <td align="right">0.010</td>
  <td align="right">0.010</td>
  <td align="right">0.643</td>
  </tr>
  <tr><td>Bernie Sanders</td>
  <td>Ridge 0.010  </td>
  <td>N</td>
  <td align="right">0.010</td>
  <td align="right">0.010</td>
  <td align="right">0.642</td>
  </tr>
  <tr><td>Bernie Sanders</td>
  <td>Lasso 0.000  </td>
  <td>Y</td>
  <td align="right">0.011</td>
  <td align="right">0.010</td>
  <td align="right">0.649</td>
  </tr>
  <tr><td>Bernie Sanders</td>
  <td>Lasso 0.000  </td>
  <td>N</td>
  <td align="right">0.010</td>
  <td align="right">0.010</td>
  <td align="right">0.646</td>
  </tr>
  <tr><td>Bernie Sanders</td>
  <td>BayesianRidge</td>
  <td>Y</td>
  <td align="right">0.010</td>
  <td align="right">0.010</td>
  <td align="right">0.643</td>
  </tr>
  <tr><td>Bernie Sanders</td>
  <td>BayesianRidge</td>
  <td>N</td>
  <td align="right">0.010</td>
  <td align="right">0.010</td>
  <td align="right">0.640</td>
  </tr>
  <tr><td>Donald Trump</td>
  <td>LeastSquares </td>
  <td>Y</td>
  <td align="right">0.005</td>
  <td align="right">0.006</td>
  <td align="right">0.401</td>
  </tr>
  <tr><td>Donald Trump</td>
  <td>LeastSquares </td>
  <td>N</td>
  <td align="right">0.005</td>
  <td align="right">0.006</td>
  <td align="right">0.401</td>
  </tr>
  <tr><td>Donald Trump</td>
  <td>Ridge 0.010  </td>
  <td>Y</td>
  <td align="right">0.005</td>
  <td align="right">0.006</td>
  <td align="right">0.426</td>
  </tr>
  <tr><td>Donald Trump</td>
  <td>Ridge 0.010  </td>
  <td>N</td>
  <td align="right">0.005</td>
  <td align="right">0.006</td>
  <td align="right">0.402</td>
  </tr>
  <tr><td>Donald Trump</td>
  <td>Lasso 0.000  </td>
  <td>Y</td>
  <td align="right">0.005</td>
  <td align="right">0.006</td>
  <td align="right">0.417</td>
  </tr>
  <tr><td>Donald Trump</td>
  <td>Lasso 0.000  </td>
  <td>N</td>
  <td align="right">0.005</td>
  <td align="right">0.006</td>
  <td align="right">0.407</td>
  </tr>
  <tr><td>Donald Trump</td>
  <td>BayesianRidge</td>
  <td>Y</td>
  <td align="right">0.005</td>
  <td align="right">0.006</td>
  <td align="right">0.428</td>
  </tr>
  <tr><td>Donald Trump</td>
  <td>BayesianRidge</td>
  <td>N</td>
  <td align="right">0.005</td>
  <td align="right">0.006</td>
  <td align="right">0.411</td>
  </tr>
  <tr><td>Marco Rubio</td>
  <td>LeastSquares </td>
  <td>Y</td>
  <td align="right">0.004</td>
  <td align="right">0.004</td>
  <td align="right">0.228</td>
  </tr>
  <tr><td>Marco Rubio</td>
  <td>LeastSquares </td>
  <td>N</td>
  <td align="right">0.004</td>
  <td align="right">0.004</td>
  <td align="right">0.228</td>
  </tr>
  <tr><td>Marco Rubio</td>
  <td>Ridge 0.010  </td>
  <td>Y</td>
  <td align="right">0.004</td>
  <td align="right">0.004</td>
  <td align="right">0.242</td>
  </tr>
  <tr><td>Marco Rubio</td>
  <td>Ridge 0.010  </td>
  <td>N</td>
  <td align="right">0.004</td>
  <td align="right">0.004</td>
  <td align="right">0.228</td>
  </tr>
  <tr><td>Marco Rubio</td>
  <td>Lasso 0.000  </td>
  <td>Y</td>
  <td align="right">0.004</td>
  <td align="right">0.005</td>
  <td align="right">0.226</td>
  </tr>
  <tr><td>Marco Rubio</td>
  <td>Lasso 0.000  </td>
  <td>N</td>
  <td align="right">0.004</td>
  <td align="right">0.004</td>
  <td align="right">0.242</td>
  </tr>
  <tr><td>Marco Rubio</td>
  <td>BayesianRidge</td>
  <td>Y</td>
  <td align="right">0.004</td>
  <td align="right">0.004</td>
  <td align="right">0.253</td>
  </tr>
  <tr><td>Marco Rubio</td>
  <td>BayesianRidge</td>
  <td>N</td>
  <td align="right">0.004</td>
  <td align="right">0.004</td>
  <td align="right">0.243</td>
  </tr>
  <tr><td>Ted Cruz</td>
  <td>LeastSquares </td>
  <td>Y</td>
  <td align="right">0.009</td>
  <td align="right">0.008</td>
  <td align="right">0.326</td>
  </tr>
  <tr><td>Ted Cruz</td>
  <td>LeastSquares </td>
  <td>N</td>
  <td align="right">0.009</td>
  <td align="right">0.008</td>
  <td align="right">0.326</td>
  </tr>
  <tr><td>Ted Cruz</td>
  <td>Ridge 0.010  </td>
  <td>Y</td>
  <td align="right">0.009</td>
  <td align="right">0.008</td>
  <td align="right">0.348</td>
  </tr>
  <tr><td>Ted Cruz</td>
  <td>Ridge 0.010  </td>
  <td>N</td>
  <td align="right">0.009</td>
  <td align="right">0.008</td>
  <td align="right">0.326</td>
  </tr>
  <tr><td>Ted Cruz</td>
  <td>Lasso 0.000  </td>
  <td>Y</td>
  <td align="right">0.009</td>
  <td align="right">0.008</td>
  <td align="right">0.374</td>
  </tr>
  <tr><td>Ted Cruz</td>
  <td>Lasso 0.000  </td>
  <td>N</td>
  <td align="right">0.009</td>
  <td align="right">0.008</td>
  <td align="right">0.322</td>
  </tr>
  <tr><td>Ted Cruz</td>
  <td>BayesianRidge</td>
  <td>Y</td>
  <td align="right">0.009</td>
  <td align="right">0.008</td>
  <td align="right">0.362</td>
  </tr>
  <tr><td>Ted Cruz</td>
  <td>BayesianRidge</td>
  <td>N</td>
  <td align="right">0.009</td>
  <td align="right">0.008</td>
  <td align="right">0.318</td>
  </tr>
  </tbody></table>
<li><b>The rest of scripts</b> were used to generate data for <a href="https://public.tableau.com/views/2016ElectionPrimaryResults/CandidateCorrelationHeatmap?:embed=y&:display_count=yes&:showTabs=y">Tableau</a>

</ol>
