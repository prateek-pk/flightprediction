import pickle
import streamlit as st

model = pickle.load(open('C:/Users/lenovo/Desktop/pk/atom/assorted/Flight-Fare-Prediction.pkl', 'rb'))


def main():
    st.title('Flight Price Prediction')

    Source = st.selectbox("Choose Source value as follows:'Chennai':1,	'Delhi':2, 'Kolkata':3, 'Mumbai':4, 'Banglore':5", [1,2,3,4,5] , key='1')

    Destination = st.selectbox("Choose Destination value as follows: 'Cochin':1, 'Delhi':2, 'Hyderabad':3, 'Kolkata':4, 'New Delhi':5, 'Banglore':6", [1,2,3,4,5,6], key='2')

    Airline = st.selectbox("Choose Airline values as follows: 'Air India':1,	'GoAir':2,	'IndiGo':3,	'Jet Airways':4,	'Jet Airways Business':5,	'Multiple carriers':6,	'Multiple carriers Premium economy':7,	'SpiceJet':8,	'Vistara':9,	'Vistara Premium economy':10, 'Trujet':11'", [1,2,3,4,5,6,7,8,9,10,11], key='3')


    Total_Stops = st.selectbox('Total Stops', ['0', '1', '2', '3', '4'], key='4')
    Journey_Day = st.selectbox('Journey Day', ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'], key='5')
    Journey_Month = st.selectbox('Journey Month', ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], key='6')
    Dep_hour = st.selectbox('Departure Hour', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'], key='7')
    Dep_Minute = st.selectbox('Departure Minute', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59'],  key='8')
    Arrival_hour = st.selectbox('Arrival Hour', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'], key='9')
    Arrival_Minute = st.selectbox('Arrival Minute', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59'], key='10')
    Duration_Hour = st.selectbox('Duration Hour', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'], key='11')
    Duration_Minute = st.selectbox('Duration Minute', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59'], key='12')




    #Prediction
    if st.button('Predict'):
        makeprediction = model.predict([[Total_Stops,	Journey_Day,	Journey_Month,	Dep_hour,	Dep_Minute,	Arrival_hour,	Arrival_Minute, Duration_Hour,	Duration_Minute,    Airline,	Source, Destination]])
        st.success('As of our prediction the price of your flight might be {}.'.format(makeprediction))

main()
