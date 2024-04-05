import pandas as pd

class StockInfoAnalyzer:
    def __init__(self, filename):
        self.df = pd.read_csv(filename)
        self.line_number = 0

    def analyze(self):
        for index, row in self.df.iterrows():
            self.line_number += 1
            if self.line_number % 6 == 0:
                prev_index = self.line_number - 6
                prev_price = self.df.iloc[prev_index, 2]  # Assuming the price is in the third column
                current_price = self.df.iloc[self.line_number, 2]  # Assuming the price is in the third column
                change = ((current_price - prev_price) / prev_price) * 100
                comp = self.df.iloc[prev_index, 1]  # Assuming the company name is in the second column
                print(f'Comp: {comp}, Price: {current_price}, {prev_price} Change: {change}')
                #print(f'Prev: {prev_price} Line: {self.line_number} Prev_index: {prev_index} Current: {current_price}') 
                #print(f"Change for company {comp} in line {self.line_number}: {change}")

# Example usage
if __name__ == "__main__":
    analyzer = StockInfoAnalyzer('stockinfo.csv')
    analyzer.analyze()


'''Problemet er at de tager den forkerte linje i programmet og udregner change, Tror problemet ligger på linje 
6. Der udover tror jeg at den tager prisen fra den samme linje heletiden og derfor er der ikke nogen change.'''