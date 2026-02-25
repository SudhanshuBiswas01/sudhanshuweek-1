import statistics

# Weather data for Gandhinagar (last 10 days)
temperature = [32, 33, 31, 34, 35, 36, 34, 33, 32, 31]
humidity = [45, 48, 50, 47, 46, 44, 43, 45, 49, 50]

print("Temperature Analysis:")
print("Average:", statistics.mean(temperature))
print("Median:", statistics.median(temperature))

print("\nHumidity Analysis:")
print("Average:", statistics.mean(humidity))
print("Median:", statistics.median(humidity))
