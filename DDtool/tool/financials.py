from yahoo_fin.stock_info import *

# financials.py
# Retrieves valuable fundamental date from various financial documents
# Returns these values in the form of a dictionary
# Note: Some values need to be converted from scientific notation for readability
#       Current values are only annual, not quarterly 


# incomeStatment
# Parameters -> Will become the ticker that wants to be searched
# Returns ->a dictionary containing imporant values from the companies income statement

def incomeStatement():
    annualValues = {}

    annualSheet = get_income_statement("xspa")


    annualValues["totalRevenue"] = annualSheet.loc[['totalRevenue']].to_numpy().flatten() 
    annualValues["COGS"] = annualSheet.loc[['costOfRevenue']].to_numpy().flatten() 
    annualValues["grossProfit"] = annualSheet.loc[['grossProfit']].to_numpy().flatten()
    annualValues["totalExpenses"] = annualSheet.loc[['totalOperatingExpenses']].to_numpy().flatten()
    annualValues["operatingIncome"] = annualSheet.loc[['operatingIncome']].to_numpy().flatten()
    annualValues["netIncome"] = annualSheet.loc[['netIncome']].to_numpy().flatten()

    return annualValues


# balanceSheet()
# Parameters -> Will become the ticker that wants to be searched
# Returns ->a dictionary containing imporant values from the companies balance sheet statement
def balanceSheet():
    
    quartAndAnnual = [] #last four quarters if want?

    annualValues = {} #last four years standing
    annualSheet = get_balance_sheet("xspa")


    annualValues["times"] = list(annualSheet) #get X axis titles AKA timeframes
    annualValues["cash"] = annualSheet.loc[['cash']].to_numpy().flatten() #flatten just turns our silly 2D array to 1D
    annualValues["totalAssets"] = annualSheet.loc[['totalAssets']].to_numpy().flatten() 
    annualValues["currentAssets"] = annualSheet.loc[['totalCurrentAssets']].to_numpy().flatten()
    #put non current assets here
    annualValues["inventory"] = annualSheet.loc[['inventory']].to_numpy().flatten()
    annualValues["totalLiabilities"] = annualSheet.loc[['totalLiab']].to_numpy().flatten()
    annualValues["currentLiabilities"] = annualSheet.loc[['totalCurrentLiabilities']].to_numpy().flatten()
    
    #put noncurrent liabilities here
    
    return annualValues
    

# cashFlow()
# Parameters -> Will become the ticker that wants to be searched
# Returns ->a dictionary containing imporant values from the companies cash flow statement
def cashFlow():

    annualCashFlows = {}
    annualCashFlowSheet = get_cash_flow("GOOG")

    annualCashFlows["OperatingCashFlow"] = annualCashFlowSheet.loc[['totalCashFromOperatingActivities']].to_numpy().flatten() 
    annualCashFlows["investingCashFlow"] = annualCashFlowSheet.loc[['totalCashflowsFromInvestingActivities']].to_numpy().flatten() 
    annualCashFlows["financingCashFlow"] = annualCashFlowSheet.loc[['totalCashFromFinancingActivities']].to_numpy().flatten()
    try:
        annualCashFlows["issuanceOfStock"] = annualCashFlowSheet.loc[['issuanceOfStock']].to_numpy().flatten() 
    except Exception as e:
         annualCashFlows["issuanceOfStock"] = 0

    annualCashFlows["stockPurchasing"] = annualCashFlowSheet.loc[['repurchaseOfStock']].to_numpy().flatten()    
    annualCashFlows["capitalExpenditure"] = annualCashFlowSheet.loc[['capitalExpenditures']].to_numpy().flatten()
    return annualCashFlows    