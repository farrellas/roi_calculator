class Property():
    def __init__(self):
        self.income = {
            "rental": 0,
            "laundry": 0,
            "storage": 0,
            "misc.": 0,
        }
        self.monthly_income = 0
        self.expenses = {
            "tax": 0,
            "insurance": 0,
            "electric": 0,
            "water": 0,
            "sewer": 0,
            "trash": 0,
            "gas": 0,
            "misc. utilties": 0,
            "hoa fees": 0,
            "lawn/snow": 0,
            "vacancy": 0,
            "repairs": 0,
            "capex": 0,
            "property mgmt": 0,
            "mortgage": 0,
        }
        self.monthly_expenses = 0
        self.monthly_cash_flow = 0
        self.investment_cost = {
            "down payment": 0,
            "closing costs": 0,
            "rehab budget": 0,
            "misc": 0,
        }
        self.total_investment = 0
        self.return_on_investment = 0

    def calc_income(self, income):
        monthly_income = 0
        for value in income.values():
            monthly_income += value
        self.monthly_income = monthly_income
        return monthly_income

    def calc_expenses(self, expenses):
        monthly_expenses = 0
        for value in expenses.values():
            monthly_expenses += value
        self.monthly_expenses = monthly_expenses
        return monthly_expenses

    def calc_cash_flow(self, monthly_income, monthly_expenses):
        monthly_cash_flow = monthly_income - monthly_expenses
        self.monthly_cash_flow = monthly_cash_flow
        return monthly_cash_flow

    def calc_investment(self, investment_cost):
        total_investment = 0
        for value in investment_cost.values():
            total_investment += value
        self.total_investment = total_investment
        return total_investment

    def calc_roi(self, monthly_cash_flow, total_investment):
        return_on_investment = ((monthly_cash_flow * 12) / total_investment) * 100
        self.return_on_investment = return_on_investment
        return return_on_investment

    def change_income(self):
        for key in self.income.keys():
            while True:
                amount = input(f"What is the {key} income per month?: $")
                try:
                    if int(amount) >= 0:
                        self.income[key] = int(amount)
                        break
                    else:
                        print("Please enter a positive number or zero.")
                except:
                    print("Please enter a valid number.")

    def change_expenses(self):
        for key in self.expenses.keys():
            while True:
                amount = input(f"What is the {key} expense per month?: $")
                try:
                    if int(amount) >= 0:
                        self.expenses[key] = int(amount)
                        break
                    else:
                        print("Please enter a positive number or zero.")
                except:
                    print("Please enter a valid number.")

    def change_investment(self):
        for key in self.investment_cost.keys():
            while True:
                amount = input(f"How much will be invested for {key}?: $")
                try:
                    if int(amount) >= 0:
                        self.investment_cost[key] = int(amount)
                        break
                    else:
                        print("Please enter a positive number or zero.")
                except:
                    print("Please enter a valid number.")

    def set_up(self):
        self.change_income()
        self.change_expenses()
        self.change_investment()
        print(f"Monthly income amount is: ${self.calc_income(self.income)}")
        print(f"Monthly expense amount is: ${self.calc_expenses(self.expenses)}")
        print(f"Total investment amount is: ${self.calc_investment(self.investment_cost)}")
        print(f"Monthly Cash Flow: ${self.calc_cash_flow(self.monthly_income, self.monthly_expenses)}")
        print(f"ROI for this property is: %{self.calc_roi(self.monthly_cash_flow, self.total_investment)}")


    def make_changes(self):
        flag = True
        while flag:
            answer = input("What would you like to change?\nIncome ('I')\nExpenses ('E')\nInvestments('V')\nEnter 'Q' to reach the main menu\n")
            if answer.lower() == 'q':
                flag = False

            elif answer.lower() == 'i':
                self.change_income()
                print(f"The new total monthly income amount is: ${self.calc_income(self.income)}")

            elif answer.lower() == 'e':
                self.change_expenses()
                print(f"The new total monthly expense amount is: ${self.calc_expenses(self.expenses)}")
                    
            elif answer.lower() == 'v':
                self.change_investment()
                print(f"The new total investment amount is: ${self.calc_investment(self.investment_cost)}")

            else:
                print("Invalid input, please enter one of the options.")

    def run(self):
        if self.income["rental"] == 0:
            print("It looks like this is a new property, let's get it set up!")
            self.set_up()

        while True:
            answer = input("What would you like to do?\nSet up property (This will overwrite all previously saved data) ('S')\nMake Changes ('C')\nView Income ('I')\nView Expenses ('E')\nView Cash Flow ('F')\nView ROI ('R')\nQuit ('Q')\n")
            if answer.lower() == 'q':
                break

            elif answer.lower() == 's':
                self.set_up()

            elif answer.lower() == 'c':
                self.make_changes()

            elif answer.lower() == 'i':
                print("Monthly income: ")
                for key, value in self.income.items():
                    if value:
                        print(f"{key.title()}: ${value}")
                print(f"Total monthly income: ${self.calc_income(self.income)}")

            elif answer.lower() == 'e':
                print("Monthly expenses: ")
                for key, value in self.expenses.items():
                    if value:
                        print(f"{key.title()}: ${value}")
                print(f"Total monthly expenses: ${self.calc_expenses(self.expenses)}")

            elif answer.lower() == 'f':
                self.calc_income(self.income)
                self.calc_expenses(self.expenses)
                print(f"Monthly Cash Flow: ${self.calc_cash_flow(self.monthly_income, self.monthly_expenses)}")

            elif answer.lower() == 'v':
                self.calc_investment(self.investment_cost)

            elif answer.lower() == 'r':
                self.calc_income(self.income)
                self.calc_expenses(self.expenses)
                self.calc_cash_flow(self.monthly_income, self.monthly_expenses)
                self.calc_investment(self.investment_cost)
                print(f"ROI for this property is: %{self.calc_roi(self.monthly_cash_flow, self.total_investment)}")
                
            else:
                print("Invalid input, please enter one of the options.")


main_st = Property()
main_st.run()
