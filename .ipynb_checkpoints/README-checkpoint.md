# Open Co Company Model [DRAFT]

## Model Architecture

The idea is to build a company model by using blocks. The model starts with a loan, then consolidates into clients, channels and finally, the company view. 

. [Loan Model](#Loan): smallest modeled unit. 

. Client Model: group of loans (LTV of client calculated)

. Channel Model: group of clients (CAC, UW + Fee Revenues calculations)

. Company Model: group of channels (Cost of Capital and Securitization calculations + Operational expenses)

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


### Setting up a new loan instance

The example below sets up a new loan. For the probability of default (pd) table, a full curve can be provided as well as an interpolation method between points.

#### Adding new default curve points

Points should be included in the format `(month, probability)` as in the example below. 


```python
# Create empty instance with defaults
loan = unit_loan()
loan.product_name = 'Unsecured Personal Loan'
loan.rate = 0.0409
loan.term = 27
loan.ticket_size = 11600
loan.fpd30 = 0.085
loan.ever30 = 0.45
loan.prepay_start = 0.005
loan.prepay_end = 0.01
loan.refi_start = 0.04
loan.refi_quality_loss = 0.60
loan.refi_end = 0.005
# Assume we know that on the 17th month, the prob of default = 43% 
loan.pd_table.append((17, 0.43))
# Assume we know that on the 6th month, the prob of default = 30%
loan.pd_table.append((6, 0.30))
# Now with FPD, EVER and the point above we can interpolate
loan.pd_method = {'method': 'pchip', 'order': 3}
```

A list of interpolation methods can be found [here](https://tinyurl.com/6mkuyz6n)


### Loan Functions

The following functions can be performed on the loan instance. 

| Syntax      | Description |
| ----------- | ----------- |
| `loan.pmt()`   | Returns the loan monthly pmt |
| `loan.save()`  | Saves the loan to disk to be later loaded into other models |
| `loan.loan_cycle()` | Creates a dataframe with the price pmt table as well as all probabilities |
| `loan.stats()` | Displays summary results for the loan including IRR, MOIC, Breakeven and other metrics | 
| `loan.pd_chart()` | Displays the probability of default chart |
| `loan.cf_chart()` | Displays the cash flow chart |
| `loan.unit_econ(chart = False)` | Displays the loan unit economics. If chart = True, displays a chart |

    
-------------------------
## Notes - WORK IN PROGRESS:
 
. Should Cash Flows be discounted by the company's cost of equity? Or just by the CDI curve? Or not discounted?

- Probably not discounted on the loan to channel models. On the company model, the calculations should be included. 

. For now, there's an assumption that 3% of defaults are recovered. Kind of an instant sale of non-performing loans. But maybe a better model would include actual refinancing estimates. Something like 10% of non-performers, refinance the balance at same initial terms (i.e. n months starting from today - spreading it out). But given the lower amounts on these scenarios, this is an ok assumption for now. 