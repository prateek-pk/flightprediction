import pickle
import streamlit as st

model = pickle.load(open('C:/Users/lenovo/Desktop/pk/atom/assorted/Flight-Fare-Prediction.pkl', 'rb'))

#Initializing variables
#Source_Chennai,    Source_Delhi,	Source_Kolkata,   Source_Mumbai
if 'Source_Chennai' not in st.session_state:
	st.session_state.Source_Chennai = 0
if 'Source_Delhi' not in st.session_state:
	st.session_state.Source_Delhi = 0
if 'Source_Kolkata' not in st.session_state:
	st.session_state.Source_Kolkata = 0
if 'Source_Mumbai' not in st.session_state:
	st.session_state.Source_Mumbai = 0
#Destination_Cochin,  Destination_Delhi,  Destination_Hyderabad,	Destination_Kolkata,	Destination_New_Delhi
if 'Destination_Cochin' not in st.session_state:
	st.session_state.Destination_Cochin = 0
if 'Destination_Delhi' not in st.session_state:
	st.session_state.Destination_Delhi = 0
if 'Destination_Hyderabad' not in st.session_state:
	st.session_state.Destination_Hyderabad = 0
if 'Destination_Kolkata' not in st.session_state:
	st.session_state.Destination_Kolkata = 0
if 'Destination_New_Delhi' not in st.session_state:
    st.session_state.Destination_New_Delhi = 0
#AirIndia,	GoAir,	IndiGo,	JetAirways,	JetAirwaysP,	MultipleCarriers,	MultipleCarriersP,	SpiceJet,	Vistara,	VistaraP
if 'AirIndia' not in st.session_state:
	st.session_state.AirIndia = 0
if 'GoAir' not in st.session_state:
	st.session_state.GoAir = 0
if 'IndiGo' not in st.session_state:
	st.session_state.IndiGo = 0
if 'JetAirways' not in st.session_state:
	st.session_state.JetAirways = 0
if 'JetAirwaysP' not in st.session_state:
    st.session_state.JetAirwaysP = 0
if 'MultipleCarriers' not in st.session_state:
	st.session_state.MultipleCarriers = 0
if 'MultipleCarriersP' not in st.session_state:
	st.session_state.MultipleCarriersP = 0
if 'SpiceJet' not in st.session_state:
	st.session_state.SpiceJet = 0
if 'Vistara' not in st.session_state:
	st.session_state.Vistara = 0
if 'VistaraP' not in st.session_state:
    st.session_state.VistaraP = 0
#duration hour and minutes
if 'Duration_Hour' not in st.session_state:
    st.session_state.Duration_Hour = 0
if 'Duration_Minute' not in st.session_state:
    st.session_state.Duration_Minute = 0


def main():
    st.title('Flight Price Prediction')

    Source = st.selectbox('Source', ['Chennai',	'Delhi', 'Kolkata', 'Mumbai'] , key='1')
    if Source == 'Chennai':
        Source_Chennai = 1
    elif Source == 'Delhi':
        Source_Delhi = 1
    elif Source == 'Kolkata':
        Source_Kolkata = 1
    elif Source == 'Mumbai':
        Source_Mumbai = 1

    Destination = st.selectbox('Destination', ['Cochin', 'Delhi', 'Hyderabad', 'Kolkata', 'New Delhi'], key='2')
    if Destination == 'Cochin':
        Destination_Cochin = 1
    elif Destination == 'Delhi':
        Destination_Delhi = 1
    elif Destination == 'Hyderabad':
        Destination_Hyderabad = 1
    elif Destination == 'Kolkata':
        Destination_Kolkata = 1
    elif Destination == 'New Delhi':
        Destination_New_Delhi = 1

    Airline = st.selectbox('Airline', ['Air India',	'GoAir',	'IndiGo',	'Jet Airways',	'Jet Airways Business',	'Multiple carriers',	'Multiple carriers Premium economy',	'SpiceJet',	'Vistara',	'Vistara Premium economy'], key='3')
    if Airline == 'Air India':
        AirIndia = 1
    elif Airline == 'GoAir':
        GoAir = 1
    elif Airline == 'IndiGo':
        IndiGo = 1
    elif Airline == 'Jet Airways':
        JetAirways = 1
    elif Airline == 'Jet Airways Business':
        JetAirwaysP = 1
    if Airline == 'Multiple carriers':
        MultipleCarriers = 1
    elif Airline == 'Multiple carriers Premium economy':
        MultipleCarriersP = 1
    elif Airline == 'SpiceJet':
        SpiceJet = 1
    elif Airline == 'Vistara':
        Vistara = 1
    elif Airline == 'Vistara Premium economy':
        VistaraP = 1


    Total_Stops = st.selectbox('Total Stops', ['0', '1', '2', '3', '4'], key='4')
    Journey_Day = st.selectbox('Journey Day', ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'], key='5')
    Journey_Month = st.selectbox('Journey Month', ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], key='6')
    Dep_hour = st.selectbox('Departure Hour', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'], key='7')
    Dep_Minute = st.selectbox('Departure Minute', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59'],  key='8')
    Arrival_hour = st.selectbox('Arrival Hour', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'], key='9')
    Arrival_Minute = st.selectbox('Arrival Minute', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59'], key='10')

    if int(Arrival_hour) > int(Dep_hour):
        st.session_state.Duration_Hour = int(Arrival_hour) - int(Dep_hour)
    else:
        st.session_state.Duration_Hour = 23 - (int(Dep_hour) - int(Arrival_hour))

    if int(Arrival_Minute) > int(Dep_Minute):
        st.session_state.Duration_Minute = int(Arrival_Minute) - int(Dep_Minute)
    else:
        st.session_state.Duration_Minute = 60 - (int(Dep_hour) - int(Arrival_hour))



    #Prediction
    if st.button('Predict'):
        makeprediction = model.predict([[Total_Stops,	Journey_Day,	Journey_Month,	Dep_hour,	Dep_Minute,	Arrival_hour,	Arrival_Minute,   Duration_Hour,	Duration_Minute,	AirIndia,	GoAir,	IndiGo,	JetAirways,	JetAirwaysP,	MultipleCarriers,	MultipleCarriersP,	SpiceJet,	Vistara,	VistaraP,	Source_Chennai,    Source_Delhi,	Source_Kolkata,   Source_Mumbai,	Destination_Cochin,  Destination_Delhi,  Destination_Hyderabad,	Destination_Kolkata,	Destination_New_Delhi]])
        st.success('As of our prediction the price of your flight might be {}.'.format(makeprediction))

main()
