import pandas as pd

    def analyze(filename):
        df = pd.read_csv(filename)
        line_number = 0

        for index, row in df.iterrows():
            line_number += 1
            if line_number % 6 == 0:
                prev_index = line_number - 6
                prev_price = df.iloc[prev_index, 2]  # Assuming the price is in the third column
                current_price = df.iloc[line_number, 2]  # Assuming the price is in the third column
                comp = df.iloc[prev_index, 1]  # Assuming the company name is in the second column

                inc = prev_price - current_price
                Dec = current_price - prev_price

                print(prev_index)
                if inc > 0:
                    pos_change = ((inc)/current_price)*100 
                    print(f"Increase: {inc:.2f}$")
                    print(f"Positive change: {pos_change:.2f}, Company: {comp}")
                else:
                    neg_change = abs(((Dec)/prev_price)*100)
                    print(f"Decrease: {-inc:.2f}$")
                    print(f"Negative change: {neg_change:.2f}%, Company: {comp}")




    # Example usage
    if __name__ == "__main__":
        analyze('stockinfo.csv')
