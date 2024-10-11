# Program #3: Tax Rate
""" Pseudocode

DEFINE get_Tax with inputs county_sales as a float and state_sales as a float, outputing a tuple of floats
    SET county_tax to county_sales times 2.5%
    SET state_tax to state_sales times 5%
    RETURN county_tax and state_tax and state_tax + county_tax

IF program is run directly
    SET county_sales to GET "County sales: "
    SET state_sales to GET "State sales: "
    SET taxes to RUN get_Tax with county_sales and state_sales

    PRINT index 0 of taxes
    PRINT index 1 of taxes
    PRINT index 2 of taxes


"""

# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program

def get_Tax(county_sales : float, state_sales : float) -> tuple[float]:
    county_tax : float = county_sales * 0.025
    state_tax : float = state_sales * 0.05

    return (round(county_tax, 2), round(state_tax, 2), round(state_tax + county_tax, 2))

def float_input(text : str) -> float:
    while True:
        try:
            out : float = float(input(text))
            return out
        except ValueError:
            print("Please enter a float.")

if __name__ == "__main__":
    county_sales : float = float_input("County sales: ")
    state_sales : float = float_input("State sales: ")

    taxes : tuple[float] = get_Tax(county_sales, state_sales)

    print(f"County tax: {taxes[0]}")
    print(f"State tax: {taxes[1]}")
    print(f"Total tax: {taxes[2]}")