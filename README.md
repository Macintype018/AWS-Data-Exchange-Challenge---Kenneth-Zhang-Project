# AWS Data Exchange Challenge - Kenneth Zhang Project
Kenneth Zhang's AWS Data Exchange Project

## General Overview of Mobility Data/Reports
Due to the COVID-19 Pandemic, Mobility data and it's trends continue to shift and alter.
Using this data, we can identify change-points in mobility data in order to identify different time periods or instances
where mobility was increased in the population, in specific industries, or other areas.
Mobility data is often collected as a series of points with latitude and longitude collected at intervals by devices such as smartphones, 
shared micromobility vehicles, on-board vehicle computers, or app-based navigation systems.
Mobility data often has a temporal element, assigning time as well as location to each point. Depending on the device used to capture the data,
other characteristics, such as the speed of travel, or who is making the trip, can be connected to each individual latitude/longitude point.
Throughout this document, mobility data is often referred to as “geospatial trip data”, “trip data”, “geospatial mobility data”, “geospatial data”,and “bread-crumb”.

• GPS Trace/ Breadcrumb Trail - The product of recording information about a trip by using
a series of points with latitude and longitude collected at regular intervals by devices such as
smartphones, bicycles, scooters, navigation systems, and vehicles. When mapped, a breadcrumb
trail can show the path of travel of an individual and/or vehicle. GPS trace data may or may not
have temporal data associated with each point.

• Individual Trip Records - For shared micromobility, ride-hail trips, and trips recorded in appbased
navigation systems, a GPS trace record is created for each unique trip. This record typically
includes start/end locations and times, route, and may include information tying that trip to a
specific user account. Individual trip records are sometimes referred to colloquially as “raw” or
“unprocessed” data. “Anonymized” trip data is that which has individual identifiers removed.

• Location Telemetry data - Any data that records the movements and sensor readings from a
vehicle including location, direction, speed, brake/throttle position, etc. Fleet operators may
use vehicle telemetry data to determine instances of dangerous driving such as harsh-braking
or excessive speeding. Some shared micromobility providers report that they can use scooter
telemetry data to determine if a scooter has been left in an upright vs tipped over position.

• Data Protection - Mechanisms for guarding against unauthorized access, including practices for
preventing unauthorized entities from accessing data. This also includes the methods used for diminishing the
usefulness of stolen data should a system be breached.

• Verifiable Data Audit - Tools or practices that automatically and routinely capture, log, and
report activity in a data set in order to ensure those accessing sensitive datasets are acting in an
approved manner.


## Using the FBProphet for Change-point Detection in Google Mobility Data/Reports of Different Countries
In this project, I will used mobility data provided by Google Inc.
I specifically chose the United Arab Emirates (UAE) for change-point detection and analysis as it was a country that had one of the least amounts of missing values in 
each of the recorded data columns. Although the FBProphet is robust against missing datapoints and positions, it is beneficial to have as many actual recorded data points.
Since the Prophet forecasts for time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily, seasonality, with the addition of
holiday effects, it would be useful for us to use more data points.

Simply put, the FBProphet uses time as a regressor and fits several similar linear and non-linear functions of time as components.
The first function fits the trend and models non-periodic changes. The second function fits seasonality with periodic changes present. The third fits ties in effects
of holidays on potentially irregular schedules for greater than or equal to one day. The last function covers idiosyncratic changes not accommodated by the model. Prophet is essentially “framing the forecasting problem as a curve-fitting exercise” rather than looking explicitly at the time based dependence of each observation.

I observed the change-points of the data depending on the yearly, monthly, and daily seasonality. Since daily and yearly seasonality are able to give us a general overview 
and forecast of what mobility data for specific countries may look like, we can use it to do a general forecast. In order to get a more detailed and consistent change-point analysis, data such as COVID-19 Mobility Data which is taken in weekly and monthly intervals, should be analyzed weekly or monthly. Monthly and weekly seasonalities were also added manually using the `.add_seasonality` function in python. 

```python
pro_change = Prophet(changepoint_range = 0.9)
pro_change.add_seasonality(period = 30.5, name = 'monthly', fourier_order = 5)
forecast = pro_change.fit(train_dataset).predict(future)
fig = pro_change.plot(forecast);
a = add_changepoints_to_plot(fig.gca(), pro_change, forecast)
```
The Python code above uses the `.add_seasonality` function to add the monthly seasonality to the model. 
I analyzed two columns of data, one for 'retail_and_recreation_percent_change_from_baseline' and the other for 'grocery_and_pharmacy_percent_change_from_baseline'.
The Jupyter Notebooks for the according columns were uploaded separately.

## Building a Multi-Layer Perceptron Artificial Neural Network Predicting Future Mobility Data
The core features of the model will include an input layer with shape (1480, 1) which is the shape of the input data, a Dense layer with 64 filters and a 'relu' 
activation function with a 'normal' kernel initializer, another Dense layer with 64 filters and relu activation, and an output layer.
The loss function is 'mse', and I also used the 'RMSprop' as optimizer, and accuracy as the metric. 
Before importing the x-values though, I had to adjust the dates like this:

```
from sklearn.model_selection import train_test_split
x = uaeMobilityData['date']
y = uaeMobilityData['retail_and_recreation_percent_change_from_baseline']
x = pd.to_numeric(uaeMobilityData['date'],errors='coerce')
x = pd.factorize(uaeMobilityData['date'])[0].reshape(-1, 1)
```

This is so that the dates are recognized as numeric values, so that the regression can actually work. 
Also, I needed to reshape the data, as it was only 1-dimensional at the time.

Using the `sklearn.preprocessing.scale` function, I normalized the dates of the data. `preprocessing.StandardScaler().fit` function returns a scalar with the normalized mean and standard deviation of the training data, which I applied to the test data using `scalar.transform` function. 

The code shown below is how I preprocessed and normalized the `x_train` data. 

```
x_train_scaled = preprocessing.scale(x_train) 
scaler = preprocessing.StandardScaler().fit(x_train) 
x_test_scaled = scaler.transform(x_test)
```

I then built the model using the components and layers introduced in the previous paragraph in this section.
The code below, in Python 3, shows how I did it.

```
model = Sequential() 
model.add(Dense(64, kernel_initializer = 'normal', activation = 'relu',input_shape = (1480, 1))) 
model.add(Dense(64, activation = 'relu')) 
model.add(Dense(1))
```

I then compiled the model using the loss function, optimizer, and metrics I before:

```
model.compile(
   loss = 'mse', 
   optimizer = RMSprop(), 
   metrics = ['mean_absolute_error']
)
```
, and the then fitted the model and analyzed and printed the overall test loss and accuracy:

```
history = model.fit(
   x_train_scaled, y_train,    
   batch_size=128, 
   epochs = 500, 
   verbose = 1, 
   validation_split = 0.3,
   callbacks = [EarlyStopping(monitor = 'val_loss', patience = 20)]
)

score = model.evaluate(x_test_scaled, y_test, verbose = 0) 
print('Test loss:', score[0]) 
print('Test accuracy:', score[1])
```

Easily, I could make predictions:

```
prediction = model.predict(x_test_scaled) 
print(prediction.flatten()) 
print(y_test)
```

## Conclusion

In conclusion, we can clearly visualize how mobility data trends altered during the COVID-19 Pandemic. We can see through the change-point detection program whether policies implemented by the United Arab Emirates did slow activity down in the country. Using the Mobility Data, we can see which countries would survive during times and whether they deemed to be essential or not. Of course, these programs are versatile and can implemented for any country.
In addition, using the Regression Predicting using a Multi-Layer Perceptron Artificial Neural Network, we can predict the future values of the mobility data for the UAE. 
These visualizations can help countries whether policies that were implemented slowed the spread and activity of the citizens within the country, as well as if the activity was correlated to an increase in cases or deaths. 

### Hopefully you enjoyed my project!


