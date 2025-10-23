import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

data=pd.read_csv('airlines_flights_data.csv')

print(data)

#1. drop index column
data=data.drop(columns='index',inplace=False) 

#2. info about data
print(data.info())

#3. statistical summary
print(data.describe())

#4.  maximum duraion flights
max_duration=data['duration'].max()
print("Maximum Duration of Flights:",max_duration)
max_duration_flights=data[data['duration']==max_duration]
print("Flights with Maximum Duration:\n",max_duration_flights)

#5.  minimum duration flights
min_duration=data['duration'].min()
print("Minimum Duration of Flights:",min_duration)
min_duration_flights=data[data['duration']==min_duration]
print("Flights with Minimum Duration:\n",min_duration_flights)

#6. null values or missing valuesand delete duplicates
print("Null Values in Each Column:\n",data.isnull().sum())
data=data.drop_duplicates()
print("Data after removing duplicates:\n",data)
print("Shape of Data after removing duplicates:",data.shape)


#7. airlines accompanied by frequency
plt.figure(figsize=(10,6))
sbn.countplot(data=data,x='airline',palette=['#1f77b4','#ff7f0e'])
plt.xticks(rotation=45) 
plt.title('Frequency of Airlines')
plt.show()

#8. Representing the arrival and departure time
plt.figure(figsize=(12,6))
sbn.countplot(data=data,x='airline',hue='arrival_time',palette='Set2')
plt.xticks(rotation=45)
plt.title('Flights by Arrival Time for Each Airline')
plt.show()
plt.figure(figsize=(12,6))
sbn.countplot(data=data,x='airline',hue='departure_time',palette='Set3')
plt.xticks(rotation=45)
plt.title('Flights by Departure Time for Each Airline')
plt.show()

#9. Representing the Source City & Destination City.
plt.figure(figsize=(10,6))
sbn.countplot(data=data,x='source_city',palette='viridis')              
plt.xticks(rotation=45)
plt.title('Frequency of Source Cities')     
plt.show()
plt.figure(figsize=(10,6))
sbn.countplot(data=data,x='destination_city',palette='magma')
plt.xticks(rotation=45)
plt.title('Frequency of Destination Cities')
plt.show()

#10. Does price varies with airlines
plt.figure(figsize=(12,6))
sbn.boxplot(data=data,x='airline',y='price',palette='Set1')
plt.xticks(rotation=45)     
plt.title('Price Variation with Airlines')
plt.show()


# 11. Does ticket price change based on the departure time and arrival time

plt.figure(figsize=(12,6))
sbn.boxplot(data=data,x='departure_time',y='price',palette='Set2')
plt.title('Price Variation with Departure Time')        
plt.show()
plt.figure(figsize=(12,6))
sbn.boxplot(data=data,x='arrival_time',y='price',palette='Set3')
plt.title('Price Variation with Arrival Time')  
plt.show()  

#12. How the price changes with change in Source and Destination?
plt.figure(figsize=(12,6))
sbn.boxplot(data=data,x='source_city',y='price',palette='coolwarm')
plt.xticks(rotation=45) 
plt.title('Price Variation with Source City')
plt.show()
plt.figure(figsize=(12,6))
sbn.boxplot(data=data,x='destination_city',y='price',palette='Spectral')
plt.xticks(rotation=45)
plt.title('Price Variation with Destination City')
plt.show()



# 13. How is the price affected when tickets are bought in just 1 or 2 days before departure?
plt.figure(figsize=(10,6))
sbn.boxplot(data=data,x='days_left',y='price',palette='Set1')
plt.title('Price Variation with Days Left to Departure')
plt.show()

# 14. How does the ticket price vary between Economy and Business class?
plt.figure(figsize=(10,6))
sbn.boxplot(data=data,x='class',y='price',palette='Set2')   
plt.title('Price Variation between Economy and Business Class')
plt.show()

#15. What will be the Average Price of Vistara airline for a flight from Delhi to Hyderabad in Business Class ?
vistara_flights=data[(data['airline']=='Vistara') & (data['source_city']=='Delhi') & (data['destination_city']=='Hyderabad') & (data['class']=='Business')]
if not vistara_flights.empty:
    average_price_vistara=vistara_flights['price'].mean()
    print("Average Price of Vistara airline from Delhi to Hyderabad in Business Class:",average_price_vistara)  
else:
    print("No Vistara flights found from Delhi to Hyderabad in Business Class.")


# 16. What is the Average Duration of Flights operated by Indigo from Bangalore to Mumbai?
indigo_ban_mum=data[(data['airline']=='Indigo') & (data['source_city']=='Bangalore') & (data['destination_city']=='Mumbai')]
average_duration_indigo=indigo_ban_mum['duration'].mean()   
print("Average Duration of Indigo from Bangalore to Mumbai:",average_duration_indigo)

# 17. Which airline has the highest number of flights departing in the Morning?
morning_flights=data[data['departure_time']=='Morning']
highest_morning_flights=morning_flights['airline'].value_counts().idxmax()
print("Airline with Highest Morning Departures:",highest_morning_flights)  


#  18. What is the most common source city for flights operated by Air India?

air_india_flights=data[data['airline']=='Air India']
if not air_india_flights.empty:
    most_common_source_city=air_india_flights['source_city'].value_counts().idxmax()
    print("Most Common Source City for Air India Flights:",most_common_source_city)
else:
    print("No Air India flights found in the dataset.")

#  19. How many flights are there from Chennai to Kolkata in Economy class?
chennai_kolkata_economy=data[(data['source_city']=='Chennai') & (data['destination_city']=='Kolkata') & (data['class']=='Economy')]
num_flights_chennai_kolkata=len(chennai_kolkata_economy)    
print("Number of Economy Flights from Chennai to Kolkata:",num_flights_chennai_kolkata)

#  20. What is the average price of flights departing in the Evening across all airlines?
evening_flights=data[data['departure_time']=='Evening'] 
average_price_evening=evening_flights['price'].mean()  
print("Average Price of Evening Departures:",average_price_evening)

#  21. Which destination city has the longest average flight duration?
average_duration_by_destination=data.groupby('destination_city')['duration'].mean() 
longest_avg_duration_city=average_duration_by_destination.idxmax()
print("Destination City with Longest Average Flight Duration:",longest_avg_duration_city)   

#  22. Which airline offers the lowest average ticket price for flights departing from Mumbai?
mumbai_flights=data[data['source_city']=='Mumbai']  
average_price_by_airline=mumbai_flights.groupby('airline')['price'].mean()
lowest_avg_price_airline=average_price_by_airline.idxmin()
print("Airline with Lowest Average Ticket Price from Mumbai:",lowest_avg_price_airline)

#  23. How many flights are there for each class (Economy and Business) across all airlines?
class_counts=data['class'].value_counts()   
print("Number of Flights for Each Class:\n",class_counts)
plt.figure(figsize=(8,6))
sbn.countplot(data=data,x='class',palette='Set3')
plt.title('Number of Flights for Each Class')
plt.show()

#  24. What is the average duration of flights departing in the Afternoon?
afternoon_flights=data[data['departure_time']=='Afternoon']
average_duration_afternoon=afternoon_flights['duration'].mean()
print("Average Duration of Afternoon Departures:",average_duration_afternoon)

#  25. Which source city has the highest average ticket price for Economy class flights?
economy_class_flights=data[data['class']=='Economy']    
average_price_by_source=economy_class_flights.groupby('source_city')['price'].mean()
highest_avg_price_source=average_price_by_source.idxmax()   
print("Source City with Highest Average Ticket Price for Economy Class:",highest_avg_price_source)

#  26. How does the flight duration vary with different airlines?
plt.figure(figsize=(12,6))  
sbn.boxplot(data=data,x='airline',y='duration',palette='Set1')
plt.xticks(rotation=45)
plt.title('Flight Duration Variation with Airlines')
plt.show()

#27 correlation heatmap, Compute the correlation only on numeric columns
numeric_data = data.select_dtypes(include=['number'])
correlation_matrix = numeric_data.corr()
plt.figure(figsize=(10,8))
sbn.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap of Numeric Features')
plt.show()