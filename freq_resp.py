import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Function to read data from a text file and create a DataFrame
def read_data(file_path):
    # Read the text file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Extract input frequencies and output voltages
    input_frequencies = []
    output_voltages = []

    for i in range(0, len(lines), 2):
        input_frequencies.append(float(lines[i].strip()))
        output_voltages.append(float(lines[i + 1].strip()))

    # Calculate voltage gain and gain in dB
    voltage_gains = [output / 1.0 for output in output_voltages]  # Input voltage is 1V
    gain_db = [20 * np.log10(gain) for gain in voltage_gains]

    # Create a DataFrame
    df = pd.DataFrame({
        'Input Frequency (Hz)': input_frequencies,
        'Output Voltage (V)': output_voltages,
        'Voltage Gain': voltage_gains,
        'Gain (dB)': gain_db
    })
    return df

# Function to plot frequency response on a semilog graph
def plot_frequency_response(df):
    plt.figure(figsize=(8, 6))
    plt.semilogx(df['Input Frequency (Hz)'], df['Gain (dB)'], marker='o', linestyle='-')
    plt.title('Frequency Response (Semilog Plot)')
    plt.xlabel('Input Frequency (Hz) [Log Scale]')
    plt.ylabel('Gain (dB)')
    plt.grid(which='both', linestyle='--', linewidth=0.5)
    plt.show()

# Main function
def main():
    # Path to the text file
    file_path = 'data6.txt'

    # Read the data
    df = read_data(file_path)

    # Display the tabular column
    print("Tabular Data:")
    print(df)

    # Plot the frequency response graph
    plot_frequency_response(df)

if __name__ == "__main__":
    main()
