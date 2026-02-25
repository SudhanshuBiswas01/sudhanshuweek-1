import statistics

# Weather data for Gandhinagar (last 10 days)
temperature = [32, 33, 31, 34, 35, 36, 34, 33, 32, 31]
humidity = [45, 48, 50, 47, 46, 44, 43, 45, 49, 50]
aqi = [110, 115, 120, 118, 122, 125, 130, 128, 124, 119]

results = []

results.append("Temperature Analysis:")
results.append(f"Average: {statistics.mean(temperature)}")
results.append(f"Median: {statistics.median(temperature)}\n")

results.append("Humidity Analysis:")
results.append(f"Average: {statistics.mean(humidity)}")
results.append(f"Median: {statistics.median(humidity)}\n")

results.append("AQI Analysis:")
results.append(f"Average: {statistics.mean(aqi)}")
results.append(f"Median: {statistics.median(aqi)}")

# Write results to file
with open("results.txt", "w") as file:
    for line in results:
        file.write(line + "\n")

print("Analysis complete. Results stored in results.txt")
