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
                
                inc = prev_price - current_price
                pos_change = ((prev_price - current_price)/current_price)*100 
                Dec = current_price - prev_price
                neg_change = abs(((Dec)/prev_price)*100)
                
                print(neg_change)
                print(Dec)
                print(f"Increase: {inc:.2f}$")
                print(f"Positive change: {pos_change:.2f}")
                print(f"Previous price: {prev_price:.2f}")
                print(f"Current price: {current_price:.2f}")    
                print(f'Pos change: {pos_change}%')
                #change = ((current_price - prev_price) / prev_price) * 100
                comp = self.df.iloc[prev_index, 1]  # Assuming the company name is in the second column
                #print(f'Comp: {comp}, Price: {current_price}, {prev_price} Change: {change}')
                #print(f'Prev: {prev_price} Line: {self.line_number} Prev_index: {prev_index} Current: {current_price}') 
                #print(f"Change for company {comp} in line {self.line_number}: {change}")

# Example usage
if __name__ == "__main__":
    analyzer = StockInfoAnalyzer('stockinfo.csv')
    analyzer.analyze()


'''Skal have lavet et if statement der siger om den skal udregnes posetivt eller negativt.'''