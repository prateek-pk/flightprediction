import pickle
import streamlit as st

model = pickle.load(open('C:/Users/lenovo/Desktop/pk/atom/assorted/Flight-Fare-Prediction.pkl', 'rb'))

def main():
    st.title('Flight Price Prediction')

    #input variables
    Source = st.text_input('Source', key='1')
    Destination = st.text_input('Destination', key='2')
    Total_Stops = st.text_input('Total Stops', key='3')
    Journey_Day = st.text_input('Journey Day', key='4')
    Journey_Month = st.text_input('Journey Month', key='5')
    Dep_hour = st.text_input('Departure Hour', key='6')
    Dep_Minute = st.text_input('Departure Minute', key='7')
    Arrival_hour = st.text_input('Arrival Hour', key='8')
    Arrival_Minute = st.text_input('Arrival Minute', key='9')
    Duration_Hour = st.text_input('Duration Hour', key='10')
    Duration_Minute = st.text_input('Duration Minute', key='11')


    #Prediction
    if st.button('Predict'):
        makeprediction = model.predict([[Source, Destination, Total_Stops,	Journey_Day, Journey_Month,	Dep_hour,	Dep_Minute,	Arrival_hour,	Arrival_Minute,	Duration_Hour,	Duration_Minute]])
        st.success('As of our prediction the price of your flight might be {}.'.format(makeprediction))

main()
