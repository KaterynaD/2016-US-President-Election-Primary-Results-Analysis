
import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import BayesianRidge

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
#%matplotlib osx
#output folder
OutputFolder="LinearRegressionPredictionPrimary/"

def residual_plot(Y_train, pred_train, Y_test, pred_test, candidate, test_dataset_name, train_dataset_name,method):

    plt.close()
    # Scatter plot the training data
    train = plt.scatter(pred_train,(Y_train-pred_train),c="b",alpha=0.5)
    # Scatter plot the testing data
    test = plt.scatter(pred_test,(Y_test-pred_test),c="r",alpha=0.5)
    # Plot a horizontal axis line at 0
    plt.hlines(y=0,xmin=-0.5,xmax=1)

    #Labels
    plt.legend((train,test),("Train","Test"),loc="lower left")
    plt.title("Residual Plots for %s  using %s method " % (candidate, method) )

    plt.savefig(OutputFolder+method+"_"+"Residual_plot_"+candidate.replace(" ", "_")+".png")
    plt.close()

def prediction_ols (X_train, Y_train, X_test, Y_test,normalize):

    # Print shapes of the training and testing data sets
    #print ("Shapes of the training and testing data sets")
    #print(X_train.shape, X_test.shape, Y_train.shape, Y_test.shape)


    #Create our regression object
    lreg = LinearRegression(normalize=normalize)

    #do a linear regression, except only on the training
    lreg.fit(X_train,Y_train)

    #print("The estimated intercept coefficient is %.2f " %lreg.intercept_)
    #print("The number of coefficients used was %d " % len(lreg.coef_))



    # Set a DataFrame from the Facts
    coeff_df = DataFrame(X_train.columns)
    coeff_df.columns = ["Fact"]


    # Set a new column lining up the coefficients from the linear regression
    coeff_df["Coefficient"] = pd.Series(lreg.coef_)


    # Show
    #coeff_df

    #highest correlation between a fact and fraction votes
    #print ("Highest correlation fact: %s is %.9f" % (cf_dict.loc[coeff_df.iloc[coeff_df["Coefficient"].idxmax()]["Fact"],"description"], coeff_df.iloc[coeff_df["Coefficient"].idxmax()]["Coefficient"]) )
    #sns_plot = sns.jointplot(coeff_df.iloc[coeff_df["Coefficient"].idxmax()]["Fact"],"Fraction Votes",pd.merge(X_test,pd.DataFrame(Y_test), right_index=True, left_index=True),kind="scatter")


    #Predictions on training and testing sets
    pred_train = lreg.predict(X_train)
    pred_test = lreg.predict(X_test)

    # The mean square error
    #print("Fit a model X_train, and calculate MSE with Y_train: %.6f"  % np.mean((Y_train - pred_train) ** 2))
    #print("Fit a model X_train, and calculate MSE with Y_test: %.6f"  %np.mean((Y_test - pred_test) ** 2))
    #Explained variance score: 1 is perfect prediction
    #print("Variance score: %.2f" % lreg.score(X_test, Y_test))

    result={}
    result["method"]="LeastSquares "
    if normalize :
        result["normalize"]="Y"
    else:
        result["normalize"]="N"
    result["X_train_shape"]=X_train.shape
    result["Y_train_shape"]=Y_train.shape
    result["X_test_shape"]=X_test.shape
    result["Y_test_shape"]=Y_test.shape
    result["intercept"]=lreg.intercept_
    result["num_coef"]=len(lreg.coef_)
    result["max_fact"]=cf_dict.loc[coeff_df.iloc[coeff_df["Coefficient"].idxmax()]["Fact"],"description"]
    result["max_fact_value"]=coeff_df.iloc[coeff_df["Coefficient"].idxmax()]["Coefficient"]
    result["MSE_train"]=np.mean((Y_train - pred_train) ** 2)
    result["MSE_test"]=np.mean((Y_test - pred_test) ** 2)
    result["variance"]=lreg.score(X_test, Y_test)
    return pred_test,coeff_df,pred_train,result

def prediction_ridge (X_train, Y_train, X_test, Y_test,alpha,normalize):

    # Print shapes of the training and testing data sets
    #print ("Shapes of the training and testing data sets")
    #print(X_train.shape, X_test.shape, Y_train.shape, Y_test.shape)
    #Create our regression object

    lreg = Ridge (alpha = alpha,normalize=normalize)

    #do a linear regression, except only on the training
    lreg.fit(X_train,Y_train)

    #print("The estimated intercept coefficient is %.2f " %lreg.intercept_)
    #print("The number of coefficients used was %d " % len(lreg.coef_))



    # Set a DataFrame from the Facts
    coeff_df = DataFrame(X_train.columns)
    coeff_df.columns = ["Fact"]


    # Set a new column lining up the coefficients from the linear regression
    coeff_df["Coefficient"] = pd.Series(lreg.coef_)


    # Show
    #coeff_df

    #highest correlation between a fact and fraction votes
    #print ("Highest correlation fact: %s is %.9f" % (cf_dict.loc[coeff_df.iloc[coeff_df["Coefficient"].idxmax()]["Fact"],"description"], coeff_df.iloc[coeff_df["Coefficient"].idxmax()]["Coefficient"]) )

    #sns_plot = sns.jointplot(coeff_df.iloc[coeff_df["Coefficient"].idxmax()]["Fact"],"Fraction Votes",pd.merge(X_test,pd.DataFrame(Y_test), right_index=True, left_index=True),kind="scatter")


    #Predictions on training and testing sets
    pred_train = lreg.predict(X_train)
    pred_test = lreg.predict(X_test)

    # The mean square error
    #print("Fit a model X_train, and calculate MSE with Y_train: %.6f"  % np.mean((Y_train - pred_train) ** 2))
    #print("Fit a model X_train, and calculate MSE with X_test and Y_test: %.6f"  %np.mean((Y_test - pred_test) ** 2))

    #Explained variance score: 1 is perfect prediction
    #print("Variance score: %.2f" % lreg.score(X_test, Y_test))

    result={}
    result["method"]="Ridge %.3f  " %alpha
    if normalize :
        result["normalize"]="Y"
    else:
        result["normalize"]="N"
    result["X_train_shape"]=X_train.shape
    result["Y_train_shape"]=Y_train.shape
    result["X_test_shape"]=X_test.shape
    result["Y_test_shape"]=Y_test.shape
    result["intercept"]=lreg.intercept_
    result["num_coef"]=len(lreg.coef_)
    result["max_fact"]=cf_dict.loc[coeff_df.iloc[coeff_df["Coefficient"].idxmax()]["Fact"],"description"]
    result["max_fact_value"]=coeff_df.iloc[coeff_df["Coefficient"].idxmax()]["Coefficient"]
    result["MSE_train"]=np.mean((Y_train - pred_train) ** 2)
    result["MSE_test"]=np.mean((Y_test - pred_test) ** 2)
    result["variance"]=lreg.score(X_test, Y_test)
    return pred_test,coeff_df,pred_train,result

def prediction_lasso (X_train, Y_train, X_test, Y_test,alpha,normalize):

    # Print shapes of the training and testing data sets
    #print ("Shapes of the training and testing data sets")
    #print(X_train.shape, X_test.shape, Y_train.shape, Y_test.shape)
    #Create our regression object

    lreg = Lasso (alpha = alpha,normalize=normalize)

    #do a linear regression, except only on the training
    lreg.fit(X_train,Y_train)

    #print("The estimated intercept coefficient is %.2f " %lreg.intercept_)
    #print("The number of coefficients used was %d " % len(lreg.coef_))



    # Set a DataFrame from the Facts
    coeff_df = DataFrame(X_train.columns)
    coeff_df.columns = ["Fact"]


    # Set a new column lining up the coefficients from the linear regression
    coeff_df["Coefficient"] = pd.Series(lreg.coef_)


    # Show
    #coeff_df

    #highest correlation between a fact and fraction votes
    #print ("Highest correlation fact: %s is %.9f" % (cf_dict.loc[coeff_df.iloc[coeff_df["Coefficient"].idxmax()]["Fact"],"description"], coeff_df.iloc[coeff_df["Coefficient"].idxmax()]["Coefficient"]) )

    #sns_plot = sns.jointplot(coeff_df.iloc[coeff_df["Coefficient"].idxmax()]["Fact"],"Fraction Votes",pd.merge(X_test,pd.DataFrame(Y_test), right_index=True, left_index=True),kind="scatter")


    #Predictions on training and testing sets
    pred_train = lreg.predict(X_train)
    pred_test = lreg.predict(X_test)

    # The mean square error
    #print("Fit a model X_train, and calculate MSE with Y_train: %.6f"  % np.mean((Y_train - pred_train) ** 2))
    #print("Fit a model X_train, and calculate MSE with X_test and Y_test: %.6f"  %np.mean((Y_test - pred_test) ** 2))

    #Explained variance score: 1 is perfect prediction
    #print("Variance score: %.2f" % lreg.score(X_test, Y_test))

    result={}
    result["method"]="Lasso %.3f  " %alpha
    if normalize :
        result["normalize"]="Y"
    else:
        result["normalize"]="N"
    result["X_train_shape"]=X_train.shape
    result["Y_train_shape"]=Y_train.shape
    result["X_test_shape"]=X_test.shape
    result["Y_test_shape"]=Y_test.shape
    result["intercept"]=lreg.intercept_
    result["num_coef"]=len(lreg.coef_)
    result["max_fact"]=cf_dict.loc[coeff_df.iloc[coeff_df["Coefficient"].idxmax()]["Fact"],"description"]
    result["max_fact_value"]=coeff_df.iloc[coeff_df["Coefficient"].idxmax()]["Coefficient"]
    result["MSE_train"]=np.mean((Y_train - pred_train) ** 2)
    result["MSE_test"]=np.mean((Y_test - pred_test) ** 2)
    result["variance"]=lreg.score(X_test, Y_test)

    return pred_test,coeff_df,pred_train,result

def prediction_BayesianRidge (X_train, Y_train, X_test, Y_test,normalize):

    # Print shapes of the training and testing data sets
    #print ("Shapes of the training and testing data sets")
    #print(X_train.shape, X_test.shape, Y_train.shape, Y_test.shape)
    #Create our regression object

    lreg = BayesianRidge(normalize=normalize)

    #do a linear regression, except only on the training
    lreg.fit(X_train,Y_train)

    #print("The estimated intercept coefficient is %.2f " %lreg.intercept_)
    #print("The number of coefficients used was %d " % len(lreg.coef_))



    # Set a DataFrame from the Facts
    coeff_df = DataFrame(X_train.columns)
    coeff_df.columns = ["Fact"]


    # Set a new column lining up the coefficients from the linear regression
    coeff_df["Coefficient"] = pd.Series(lreg.coef_)


    # Show
    #coeff_df

    #highest correlation between a fact and fraction votes
    #print ("Highest correlation fact: %s is %.9f" % (cf_dict.loc[coeff_df.iloc[coeff_df["Coefficient"].idxmax()]["Fact"],"description"], coeff_df.iloc[coeff_df["Coefficient"].idxmax()]["Coefficient"]) )

    #sns_plot = sns.jointplot(coeff_df.iloc[coeff_df["Coefficient"].idxmax()]["Fact"],"Fraction Votes",pd.merge(X_test,pd.DataFrame(Y_test), right_index=True, left_index=True),kind="scatter")


    #Predictions on training and testing sets
    pred_train = lreg.predict(X_train)
    pred_test = lreg.predict(X_test)

    # The mean square error
    #print("MSE with X_train and Y_train: %.6f"  % np.mean((Y_train - pred_train) ** 2))
    #print("MSE with X_test and Y_test: %.6f"  %np.mean((Y_test - pred_test) ** 2))

    #Explained variance score: 1 is perfect prediction
    #print("Variance score: %.2f" % lreg.score(X_test, Y_test))

    result={}
    result["method"]="BayesianRidge"
    if normalize :
        result["normalize"]="Y"
    else:
        result["normalize"]="N"
    result["X_train_shape"]=X_train.shape
    result["Y_train_shape"]=Y_train.shape
    result["X_test_shape"]=X_test.shape
    result["Y_test_shape"]=Y_test.shape
    result["intercept"]=lreg.intercept_
    result["num_coef"]=len(lreg.coef_)
    result["max_fact"]=cf_dict.loc[coeff_df.iloc[coeff_df["Coefficient"].idxmax()]["Fact"],"description"]
    result["max_fact_value"]=coeff_df.iloc[coeff_df["Coefficient"].idxmax()]["Coefficient"]
    result["MSE_train"]=np.mean((Y_train - pred_train) ** 2)
    result["MSE_test"]=np.mean((Y_test - pred_test) ** 2)
    result["variance"]=lreg.score(X_test, Y_test)
    return pred_test,coeff_df,pred_train,result

#===============================================================================
def get_data(candidate):
    # source data
    # from Kaggle 2016 US Election project
    pr=pd.read_csv("SourceData/primary_results.csv")
    #pivoting and drop Null values for clean and easy analysis
    pr_piv= pr[["fips", "candidate","fraction_votes"]].pivot_table(index="fips", columns="candidate", values="fraction_votes")
    pr_piv.drop(" No Preference", axis=1, inplace=True)
    pr_piv.drop(" Uncommitted", axis=1, inplace=True)

    #merge fraction votes and facts to have a complete data set for all counties for each candidate
    pr_facts=pd.merge(pr_piv, facts, right_index=True, left_index=True)

    Candidate_data=pr_facts[[candidate,"PST045214", "PST040210", "PST120214", "POP010210", "AGE135214","AGE295214", "AGE775214", "SEX255214", "RHI125214", "RHI225214","RHI325214", "RHI425214", "RHI525214", "RHI625214", "RHI725214","RHI825214", "POP715213", "POP645213", "POP815213","VET605213", "LFE305213", "HSG010214", "HSG445213","HSG096213", "HSG495213", "HSD410213", "HSD310213", "INC910213","INC110213", "PVY020213", "BZA010213", "BZA110213", "BZA115213","NES010213", "SBO001207", "SBO315207", "SBO115207", "SBO215207","SBO515207", "SBO415207", "SBO015207", "MAN450207", "WTN220207","RTN130207", "RTN131207", "AFN120207", "BPS030214", "LND110210","POP060210"]]
    Candidate_data=Candidate_data.dropna()
    Candidate_data.columns=["Fraction Votes","PST045214", "PST040210", "PST120214", "POP010210", "AGE135214","AGE295214", "AGE775214", "SEX255214", "RHI125214", "RHI225214","RHI325214", "RHI425214", "RHI525214", "RHI625214", "RHI725214","RHI825214", "POP715213", "POP645213", "POP815213","VET605213", "LFE305213", "HSG010214", "HSG445213","HSG096213", "HSG495213", "HSD410213", "HSD310213", "INC910213","INC110213", "PVY020213", "BZA010213", "BZA110213", "BZA115213","NES010213", "SBO001207", "SBO315207", "SBO115207", "SBO215207","SBO515207", "SBO415207", "SBO015207", "MAN450207", "WTN220207","RTN130207", "RTN131207", "AFN120207", "BPS030214", "LND110210","POP060210"]
    Candidate_fractions=Candidate_data["Fraction Votes"]
    Candidate_facts=Candidate_data.drop("Fraction Votes", 1)

    return Candidate_facts,Candidate_fractions


def vis_results(Y_train, pred_train, Y_test, pred_test, candidate, test_dataset_name, train_dataset_name,result,method):

    #residual plot
    residual_plot(Y_train, pred_train, Y_test, pred_test, candidate, test_dataset_name, train_dataset_name,method)

    #prediction in csv
    CandidateFractionPrediction=pd.DataFrame(Y_test)
    CandidateFractionPrediction["Prediction"]=pred_test
    CandidateFractionPrediction=pd.merge(CandidateFractionPrediction,facts[["area_name","state_abbreviation"]], right_index=True, left_index=True)
    CandidateFractionPrediction=CandidateFractionPrediction.reset_index()
    CandidateFractionPrediction.columns=["fips", "Fraction Votes", "Prediction", "county", "state"]
    CandidateFractionPrediction[CandidateFractionPrediction["state"]=="CA"]
    CandidateFractionPrediction.to_csv(OutputFolder+method+"_"+"Prediction_data_"+candidate.replace(" ", "_")+".csv")

    #joinplot
    sns_plot = sns.jointplot("Fraction Votes","Prediction",CandidateFractionPrediction,kind="scatter")
    sns_plot.savefig(OutputFolder+method+"_"+"Jointplot_"+candidate.replace(" ", "_")+".png")

    #total table
    result["candidate"]=candidate
    results.append(result)
def run(candidate):

    print ("----------%s PRIMARY RESULTS PREDICTION------------" %candidate)

    test_dataset_name="Test part"
    train_dataset_name="Train part"

    #get source data
    Candidate_facts,Candidate_fractions=get_data(candidate)

    #separate to training and test data sets
    X_train, X_test, Y_train, Y_test = sklearn.cross_validation.train_test_split(Candidate_facts,Candidate_fractions)

    #Prediction
    #multi
    print ("----------------------Ordinary least square Normalize ------------")
    pred_test,coeff_df,pred_train,result=prediction_ols (X_train, Y_train, X_test, Y_test,True)
    vis_results(Y_train, pred_train, Y_test, pred_test, candidate, test_dataset_name, train_dataset_name,result,"ols_n")
    print ("----------------------Ordinary least square-----------------------")
    pred_test,coeff_df,pred_train,result=prediction_ols (X_train, Y_train, X_test, Y_test,False)
    vis_results(Y_train, pred_train, Y_test, pred_test, candidate, test_dataset_name, train_dataset_name,result,"ols")

    print ("------------------------------Ridge 0.01 Normalize ------------")
    pred_test,coeff_df,pred_train,result=prediction_ridge(X_train, Y_train, X_test, Y_test, 0.01,True)
    vis_results(Y_train, pred_train, Y_test, pred_test, candidate, test_dataset_name, train_dataset_name,result,"ridge_n")
    print ("------------------------------Ridge 0.01-----------------------")
    pred_test,coeff_df,pred_train,result=prediction_ridge(X_train, Y_train, X_test, Y_test, 0.01,False)
    vis_results(Y_train, pred_train, Y_test, pred_test, candidate, test_dataset_name, train_dataset_name,result,"ridge")

    print ("------------------------------Lasso 0.0001 Normalize ------------")
    pred_test,coeff_df,pred_train,result=prediction_lasso(X_train, Y_train, X_test, Y_test, 0.0001,True)
    vis_results(Y_train, pred_train, Y_test, pred_test, candidate, test_dataset_name, train_dataset_name,result,"lasso_n")
    print ("------------------------------Lasso 0.0001-----------------------")
    pred_test,coeff_df,pred_train,result=prediction_lasso(X_train, Y_train, X_test, Y_test, 0.0001,False)
    vis_results(Y_train, pred_train, Y_test, pred_test, candidate, test_dataset_name, train_dataset_name,result,"lasso")


    print ("---------------------------BayesianRidge Normalize ------------")
    pred_test,coeff_df,pred_train,result=prediction_BayesianRidge(X_train, Y_train, X_test, Y_test,True)
    vis_results(Y_train, pred_train, Y_test, pred_test, candidate, test_dataset_name, train_dataset_name,result,"br_n")

    print ("---------------------------BayesianRidge-----------------------")
    pred_test,coeff_df,pred_train,result=prediction_BayesianRidge(X_train, Y_train, X_test, Y_test,False)
    vis_results(Y_train, pred_train, Y_test, pred_test, candidate, test_dataset_name, train_dataset_name,result,"br")


#===============================================================================
#facts and  dictionary
cf_dict=pd.read_csv("SourceData/county_facts_dictionary.csv")
cf_dict=cf_dict.set_index("column_name")
facts=pd.read_csv("SourceData/county_facts.csv")
facts=facts.set_index("fips")
#===============================================================================
results=[]
#===============================================================================
run("Hillary Clinton")
run("Bernie Sanders")
run("Donald Trump")
run("Marco Rubio")
run("Ted Cruz")




with open(OutputFolder+"results.csv", "wb") as output:
    output.write("candidate,"+
    "method,"+
    "normalize,"
    "X_train_shape,"+
    "Y_train_shape,"+
    "X_test_shape,"+
    "Y_test_shape,"+
    "intercept,"+
    "num_coef,"+
    "max_fact,"+
    "max_fact_value,"+
    "MSE_train,"+
    "MSE_test,"+
    "Variance"+
    "\n")
    c=""
    for result in results:
        output.write("%s,\"%s\",%s,\"%s\",\"%s\",\"%s\",\"%s\",%s,%s,\"%s\",%s,%s,%s,%s\n"
        % (result["candidate"],
        result["method"],
        result["normalize"],
        result["X_train_shape"],
        result["Y_train_shape"],
        result["X_test_shape"],
        result["Y_test_shape"],
        result["intercept"],
        result["num_coef"],
        result["max_fact"],
        result["max_fact_value"],
        result["MSE_train"],
        result["MSE_test"],
        result["variance"])
        )
        if c!=result["candidate"]:
                print ("------------------------------------")
                print (result["candidate"])
                c=result["candidate"]
                print ("------------------------------------")
                print ("Method        N MSE   MSE   Varia Fact")
                print ("------------------------------------")
        print ( "%s %s %.3f %.3f %.3f %s" %(result["method"],result["normalize"],result["MSE_train"],result["MSE_test"],result["variance"],result["max_fact"]))
