import pandas as pd

#from flask import Flask

#app = Flask(__name__)

# Preperation
final_report = pd.read_csv(r"final_10k_report.csv")
summary_report = pd.read_csv(r"summary_final10k_report.csv")

# Inspect the columns to check for correct column names
print("Columns in final_report:", final_report.columns)
print("Columns in summary_report:", summary_report.columns)

# Basic chatbot development
#@app.route('/chatbot', methods=['POST'])
def simple_chatbot():
    print("Enter Your Query")
    user_query = input()

    # final report

    if user_query == "What is the total revenue?":
        total_revenue = \
        final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)][
            "Total Revenue"
        ].values[0]
        return f"The total revenue for {company_input} for fiscal year {fiscal_year} is ${total_revenue}."

    elif user_query == "How has net income changed over the last year?":
        net_income = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)][
            "Net Income"].values[0]
        return f"The net income for {company_input} for fiscal year {fiscal_year} has changed by ${net_income} over the last year."

    elif user_query == "What are the current liabilities?":
        total_liabilities = \
        final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)][
            "Total Liabilities"
        ].values[0]
        return f"The current liabilities for {company_input} for fiscal year {fiscal_year} are ${total_liabilities}."

    elif user_query == "What is the sum total assets?":
        total_assets = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)][
            "Total Assets"].values[0]
        return f"The Total Liabilities for {company_input} for fiscal year {fiscal_year} is {total_assets}%."

    elif user_query == "What is the operating cash flow?":
        cash_flow_operation = \
        final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)][
            "Cash Flow from Operating Activities"
        ].values[0]
        return f"The operating cash flow for {company_input} for fiscal year {fiscal_year} is ${cash_flow_operation}."

    # final report growth

    elif user_query == "What is the net income growth(%) ?":
        net_growth = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)][
            "Net Income Growth (%)"
        ].values[0]
        return f"The Net Income Growth(%) for {company_input} for fiscal year {fiscal_year} is {net_growth}(%)"

    elif user_query == "What is the assets growth(%) ?":
        assets_growth = \
        final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)][
            "Assets Growth (%)"
        ].values[0]
        return f"The Assets Growth(%) for {company_input} for fiscal year {fiscal_year} is {assets_growth}(%)"

    elif user_query == "What is the liabilities growth(%) ?":
        liabilities_growth = \
        final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)][
            "Liabilities Growth (%)"
        ].values[0]
        return f"The Liabilities Growth(%) for {company_input} for fiscal year {fiscal_year} is {liabilities_growth}(%)"

    elif user_query == "What is the cash flow from operations growth(%) ?":
        cash_flow_growth = \
        final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)][
            "Cash flow from Operations Growth (%)"
        ].values[0]
        return f"The Cash Flow from Operations Growth(%) for {company_input} for fiscal year {fiscal_year} is {cash_flow_growth}(%)"

    # summary report

    elif user_query == "What is the year by year average revenue growth rate(%)?":
        year_avg_revenue_growth = (
            summary_report[(summary_report["Company"] == company_input)]["Revenue Growth (%)"]
            .values[0]
            .round(4)
        )
        return f"The Year By Year Average Revenue Growth Rate(%) from 2021 to 2023 for {company_input} is {year_avg_revenue_growth}(%)"

    elif user_query == "What is the year by year average net income growth rate(%)?":
        year_avg_netincome_growth = (
            summary_report[(summary_report["Company"] == company_input)][
                "Net Income Growth (%)"
            ]
            .values[0]
            .round(4)
        )
        return f"The Year By Year Net Income Revenue Growth Rate(%) from 2021 to 2023 for {company_input} is {year_avg_netincome_growth}(%)"

    elif user_query == "What is the year by year average assets growth rate(%)?":
        year_avg_assets_growth = (
            summary_report[(summary_report["Company"] == company_input)]["Assets Growth (%)"]
            .values[0]
            .round(4)
        )
        return f"The Year By Year Average Assets Growth Rate(%) from 2021 to 2023 for {company_input} is {year_avg_assets_growth}(%)"

    elif user_query == "What is the year by year average liabilities growth rate(%)?":
        year_avg_liabilities_growth = (
            summary_report[(company_input)]["Liabilities Growth (%)"].values[0].round(4)
        )
        return f"The Year By Year Average Liabilities Growth Rate(%) from 2021 to 2023 for {company_input} is {year_avg_liabilities_growth}(%)"
        
    elif user_query == "What is the year by year average cash flow from operations growth rate(%)?":
        year_avg_cashflowops_growth = (
            summary_report[(summary_report["Company"] == company_input)][
                "Cash flow from Operations Growth (%)"
            ]
            .values[0]
            .round(4)
        )
        return f"The Year By Year Average Cash Flow from Operations Growth Rate(%) from 2021 to 2023 for {company_input} is {year_avg_cashflowops_growth}(%)"
        
    # Add more conditions for other predefined queries
    
    else:
        return "Sorry, I can only provide information on predefined queries."


# Test the chatbot
while True:
    print("--------------------------------------------------------------")
    user_input = input("Enter to start the chatbot session; (type 'exit' to quit):")
    if user_input.lower() == "exit":
        break
    elif user_input.lower() == "hi":
        print("\nHi! Welcome to AI Chatbot Financial!!!")
        print("\nI can help you with financial queries")
        print("Select to find company name from below: -")
        print("\n1. Microsoft \n2. Tesla \n3. Apple")
        company_input = input("Enter company name: ").capitalize()
        if company_input not in ["Apple", "Microsoft", "Tesla"]:
            print(f"Invalid company name doesnt exit. Please try again")
            break
        else:
            print("\nThe data for fiscal year 2023, 2022, 2021 is currently available")
            fiscal_year = int(input("Enter fiscal year: "))
            if fiscal_year not in [2023, 2022, 2021]:
                print(f"Invalid fiscal year doesnt exit. Please input again")
                break
    else:
        print(f"Enter 'Hi' by starting the chatbot session again")
        break

responce = simple_chatbot()
print(responce)

#if __name__ == '__main__':
#    app.run(debug=True)
