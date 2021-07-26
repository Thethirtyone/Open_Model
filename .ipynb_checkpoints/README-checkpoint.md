# Open Co Company Model [DRAFT]

## Model Architecture

The idea is to build a company model by using blocks. The model starts with a loan, then consolidates into clients, channels and finally, the company view. 

. Loan = smallest modeled unit. 

. Clients = group of loans (LTV of client calculated)

. Channels = group of clients (CAC, UW + Fee Revenues calculations)

. Company = group of channels (Cost of Capital and Securitization calculations + Operational expenses)

## Loan 

Jupyter Notebook: `unit_loan.ipynb`

### Description

The unit loan pricing starts with a standard `price` table and adjusts cash flows to different events. On each month the loan can either:

1. Perform (p)

    a. PMTs paid as expected

    b. Loan balance is paid early 

2. Not Perform (1 - p)

    a. Refinanced / Rescheduled
    
    b. Defaults (and loan is sold off)
    
A probability tree is built with each of these scenarios.

 
    
    
    
    
-------------------------
## Notes - WORK IN PROGRESS:
 
. Should Cash Flows be discounted by the company's cost of equity? Or just by the CDI curve? Or not discounted?

- Probably not discounted on the loan to channel models. On the company model, the calculations should be included. 

. For now, there's an assumption that 3% of defaults are recovered. Kind of an instant sale of non-performing loans. But maybe a better model would include actual refinancing estimates. Something like 10% of non-performers, refinance the balance at same initial terms (i.e. n months starting from today - spreading it out). But given the lower amounts on these scenarios, this is an ok assumption for now. 