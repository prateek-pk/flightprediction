
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings(action='ignore')


flight = pd.read_csv('C:/Users/lenovo/Desktop/pk/atom/assorted/Data_Train.csv')

flight.dropna(inplace=True)
flight.isnull().sum()

flight['Journey_Day'] = pd.to_datetime(flight.Date_of_Journey , format = '%d/%m/%Y').dt.day
flight['Journey_Month'] = pd.to_datetime(flight.Date_of_Journey , format = '%d/%m/%Y').dt.month
flight['Dep_hour'] = pd.to_datetime(flight.Dep_Time ).dt.hour
flight['Dep_Minute'] = pd.to_datetime(flight.Dep_Time ).dt.minute
flight['Arrival_hour'] = pd.to_datetime(flight.Arrival_Time ).dt.hour
flight['Arrival_Minute'] = pd.to_datetime(flight.Arrival_Time ).dt.minute

flight.drop(columns=['Dep_Time' , 'Date_of_Journey' , 'Arrival_Time'],inplace=True)

duration = list(flight.Duration)

for i in range(len(duration)):
    if len(duration[i].split()) != 2:
        if 'h' in duration[i]:
            duration[i] = duration[i] + ' 0m'
        else:
            duration[i] = '0h ' + duration[i]

duration
duration_hour=[]
duration_minute=[]

for i in range(len(duration)):
    duration_hour.append(int(duration[i].split(sep='h')[0] ))
    duration_minute.append(int( duration[i].split('m')[0].split()[-1] ))

flight['Duration_Hour'] = duration_hour
flight['Duration_Minute'] = duration_minute

flight.drop(columns='Duration',inplace=True)

Airline = flight['Airline']
Airline = pd.get_dummies(Airline , drop_first=True)

Source = flight[['Source']]
Source = pd.get_dummies(Source , drop_first=True)

Destination = flight[['Destination']]
Destination = pd.get_dummies(Destination , drop_first=True)

flight.drop(columns=['Route','Additional_Info'],axis=1 , inplace=True)

flight.replace( { 'non-stop':0 , '1 stop':1 , '2 stops':2 , '3 stops':3 ,'4 stops':4 } ,inplace=True)

flight = pd.concat( [flight , Airline ,Source , Destination] , axis=1)

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

flight.drop(columns = [ 'Airline' , 'Source' , 'Destination' ] , inplace=True)

flight_test = pd.read_excel('C:/Users/lenovo/Desktop/pk/atom/assorted/Test_set.xlsx')

flight_test.dropna(inplace=True)

flight_test['Journey_Day'] = pd.to_datetime(flight_test.Date_of_Journey , format = '%d/%m/%Y').dt.day
flight_test['Journey_Month'] = pd.to_datetime(flight_test.Date_of_Journey , format = '%d/%m/%Y').dt.month

flight_test['Dep_hour'] = pd.to_datetime(flight_test.Dep_Time ).dt.hour
flight_test['Dep_Minute'] = pd.to_datetime(flight_test.Dep_Time ).dt.minute

flight_test.drop(columns=['Dep_Time' , 'Date_of_Journey'],inplace=True)

flight_test['Arrival_hour'] = pd.to_datetime(flight_test.Arrival_Time ).dt.hour
flight_test['Arrival_Minute'] = pd.to_datetime(flight_test.Arrival_Time ).dt.minute

flight_test.drop(columns='Arrival_Time',inplace=True)

duration = list(flight_test.Duration)

for i in range(len(duration)):
    if len(duration[i].split()) != 2:
        if 'h' in duration[i]:
            duration[i] = duration[i] + ' 0m'
        else:
            duration[i] = '0h ' + duration[i]

duration
duration_hour=[]
duration_minute=[]

for i in range(len(duration)):
    duration_hour.append(int(duration[i].split(sep='h')[0] ))
    duration_minute.append(int( duration[i].split('m')[0].split()[-1] ))

flight_test['Duration_Hour'] = duration_hour
flight_test['Duration_Minute'] = duration_minute
flight_test.drop(columns='Duration',inplace=True)

Airline = flight_test['Airline']
Airline = pd.get_dummies(Airline , drop_first=True)

Source = flight_test[['Source']]
Source = pd.get_dummies(Source , drop_first=True)

Destination = flight_test[['Destination']]
Destination = pd.get_dummies(Destination , drop_first=True)

flight_test.drop(columns=['Route','Additional_Info'],axis=1 , inplace=True)

flight_test.replace( { 'non-stop':0 , '1 stop':1 , '2 stops':2 , '3 stops':3 ,'4 stops':4 } ,inplace=True)

flight_test = pd.concat( [flight_test , Airline ,Source , Destination] , axis=1)

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

flight_test.drop(columns = [ 'Airline' , 'Source' , 'Destination' ] , inplace=True)

X = flight.drop(columns='Price',axis=1)
y = flight['Price']

from sklearn.ensemble import ExtraTreesRegressor
etr = ExtraTreesRegressor()
etr.fit(X,y)

from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.2 , random_state=51)

from sklearn.ensemble import RandomForestRegressor
rfr = RandomForestRegressor()
rfr.fit(X_train , y_train)

pred = rfr.predict(X_test)

rfr.score(X_train , y_train)

rfr.score(X_test , y_test)

from sklearn import metrics
print('MAE:', metrics.mean_absolute_error(y_test, pred))
print('MSE:', metrics.mean_squared_error(y_test, pred))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, pred)))

metrics.r2_score(y_test,pred)

from sklearn.model_selection import RandomizedSearchCV

n_estimators = [int(x) for x in np.linspace(100,2000,10)]
max_depth = [int(x) for x in np.linspace(100,2000,10)]
min_samples_split=[2,4,6,8,10,12,14]
min_samples_leaf=[1,3,5,7,8,10]
max_features=['sqrt','log2','auto',None]

random_search = {
    'n_estimators' : n_estimators,
    'max_depth' : max_depth,
    'min_samples_split' : min_samples_split,
    'min_samples_leaf' : min_samples_leaf,
    'max_features' : max_features,

}


rfr_random = RandomizedSearchCV(estimator=rfr , param_distributions=random_search , n_iter=10 , cv=5 , verbose=2 , random_state=51 , n_jobs=1)

rfr_random.fit(X_train , y_train)
rfr_random.best_params_

prediction = rfr_random.predict(X_test)

print('MAE:', metrics.mean_absolute_error(y_test, prediction))
print('MSE:', metrics.mean_squared_error(y_test, prediction))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, prediction)))

metrics.r2_score(y_test,prediction)

import pickle
file = open('Flight-Fare-Prediction.pkl','wb')
pickle.dump(rfr_random,file)

model = open('Flight-Fare-Prediction.pkl','rb')
mod = pickle.load(model)
