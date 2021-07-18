# Open Co Company Model

## Model Architecture

The model starts by pricing the unit loan. Similar to building blocks, the idea is that:

. Loan = smallest priced unit. Products are loans with specific characteristics.
. Clients = group of loans (LTV of client calculated here)
. Channels = group of clients (CAC calculations done here)
. Company = group of channels

    
    
    
    
    
-------------------------
 Notes:
. Should Cash Flows be discounted by the company's cost of equity? Or just by the CDI curve? Or not discounted?
. For now, there's an assumption that 3% of defaults are recovered. Kind of an instant sale of non-performing loans. But maybe a better model would include actual refinancing estimates. Something like 10% of non-performers, refinance the balance at same initial terms (i.e. n months starting from today - spreading it out)