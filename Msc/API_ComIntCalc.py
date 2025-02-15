from flask import Flask, request, jsonify
import pandas as pd
from datetime import datetime
import os

# Initialize the Flask app
app = Flask(__name__)

# Path to CSV file
csv_file = '/Users/rohit.jishtu/Documents/ListOfStocks.csv'

# If the CSV file does not exist, create an empty DataFrame


# Function to calculate compound interest rate
def compound_interest_rate(start_price, end_price, time, times_compounded):
    rate = times_compounded * ((end_price / start_price) ** (1 / (time * times_compounded)) - 1)
    return rate * 100  # Convert to percentage

# Function to calculate compound interest rate
def compound_interest_Value(start_price, rate, time, times_compounded):
    end_price=0
    end_price = start_price * (1 + rate / times_compounded) ** (times_compounded * time)
    return end_price

# Function to make a recommendation based on gain and rate
def recommendation(gain, rate, dividend_per_share, time):
    # Thresholds for decision-making
    dividend_threshold = 3  # Minimum acceptable annual dividend yield (in %)
    gain_threshold = 5      # Minimum acceptable gain (in %)
    rate_threshold = 10     # Minimum acceptable rate of return (in %)

    # Calculate dividend yield
    annual_dividend_yield = (dividend_per_share / (gain + dividend_per_share)) * 100

    # Decision-making logic
    if gain > gain_threshold and rate > rate_threshold and annual_dividend_yield > dividend_threshold:
        return "Buy More"
    elif gain > 0 or (rate > 5 and annual_dividend_yield > 2):
        return "Hold"
    else:
        return "Sell"

# Function to insert data into the DataFrame
def INSERT_Data(data, Input):
    ExistingStocks = set(data['StockName'])
    if Input['StockName'] not in ExistingStocks:
        new_row = pd.DataFrame([{
            'StockName': Input['StockName'],
            'StocksQty': Input['StocksQty'],
            'StartPrice': Input['StartPrice'],
            'EndPrice': Input['EndPrice'],
            'Divident_All': Input['Divident_All'],
            'DPS': Input['DPS'],
            'Time_Years': Input['Time'],
            'Gain': Input['Gain'],
            'Rate': Input['Rate'],
            'Times_Compounded': Input['timesCompounded'],
            'Recommendation': Input['Recommendation'],
            'InsertDate': Input["InsertDate"]
        }])
        data = pd.concat([data, new_row], ignore_index=True)
    else:
        print('Data Already Exists for this stock now ')
    
    return data

# API Endpoint to process stock data and return recommendation
@app.route('/stock_recommendation', methods=['POST'])
def stock_recommendation():
    input_data = request.get_json()  # Get input data as JSON
    
    # Check if required fields are present
    required_fields = ["StockName", "StocksQty", "StartPrice", "EndPrice", "Time", "timesCompounded", "Divident_All"]
    for field in required_fields:
        if field not in input_data:
            return jsonify({"error": f"Missing {field} in input data"}), 400
    
    # Perform calculations
    input_data["Rate"] = compound_interest_rate(
        input_data["StartPrice"],
        input_data["EndPrice"],
        input_data["Time"],
        input_data["timesCompounded"]
    )
    input_data["Gain"] = (input_data["EndPrice"] * input_data["StocksQty"]) - (input_data["StartPrice"] * input_data["StocksQty"])
    input_data["DPS"] = round(input_data["Divident_All"] / input_data['StocksQty'])
    input_data["Recommendation"] = recommendation(input_data["Gain"], input_data["Rate"], input_data["DPS"], input_data["Time"])

    # Insert data into the DataFrame
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    input_data["InsertDate"] = current_time
    data = pd.read_csv(csv_file)
    data = INSERT_Data(data, input_data)

    # Save the updated data to CSV
    data.to_csv(csv_file, index=False)

    # Return the recommendation and other details as JSON response
    return jsonify({
        "StockName": input_data["StockName"],
        "Recommendation": input_data["Recommendation"],
        "Rate": input_data["Rate"],
        "Gain": input_data["Gain"],
        "DPS": input_data["DPS"],
        "InsertDate": input_data["InsertDate"]
    })

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
