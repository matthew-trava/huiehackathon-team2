import matplotlib.pyplot as plt
import numpy as np

def transform_dataframes(df20, df21):
	df20.rename(columns={
	    'revenue affect': 'revenue_affect',

	}, inplace=True)
	df21.rename(columns={
	    'Are your funding/revenue levels for this past 12 months different from the year previous? (Please show us on the scale below)': 'revenue_affect',
	    'What type of organisation do you represent? (Please choose from the list below)': 'orgtype',
	    'Approximately how many paid staff and/or contractors work with/for your organisation?': 'paid staff',
	    'Approximately how many volunteers work with your organisation each month?': 'volunteers',
	    'What was the approximate annual income / operations budget for your organisation for the last financial year?': 'income',
	    'Of the following options, which best describes the focus of your organisation\'s activities or services?': 'service type',
	}, inplace=True)

	df20['revenue_affect'] = df20.revenue_affect.map({
	    'We have had, or expect to have, a very large reduction in revenue (decline of 50% or more)': -50,
	    'We have had, or expect to have, a large reduction in revenue (decline of 20% to 49%)': -35,
	    'We have had, or expect to have, a moderate reduction in revenue (10-19% decline)': -15,
	    'We have had, or expect to have, a small reduction in revenue (0-9% decline)': -5,
	    'We have had, or expect to have, no change in revenue': 0,
	    'We have had, or expect to have, a small increase in revenue (0-9% increase)': 5,
	    'We have had, or expect to have, a moderate increase in revenue (10-19% increase)': 15,
	    'We have had, or expect to have, a large increase in revenue (increase of 20% to 49%)': 35,
	    'We have had, or expect to have, a very large increase in revenue (increase of 50% or more)': 50,
	    "I'm not sure": np.nan
	})
	df21['revenue_affect'] = df21.revenue_affect.map({
	    '100% or more decline': -100,
	    '75% decline': -75,
	    '50% decline': -50,
	    '25% or less decline': -25,
	    'No change in funding/revenue': 0,
	    '25% increase': 25,
	    '50% increase': 50,
	    '75% increase': 75,
	    '100% or more increase': 100,
	    "Response": np.nan
	})

	df20['revenue_sign'] = np.sign(df20.revenue_affect).fillna(0)
	df21['revenue_sign'] = np.sign(df21.revenue_affect).fillna(0)

	service_delivery_affect_order = ['Substantial cuts', 'Moderate cuts', 'Small cuts', 'Same level of services', 'Small increases', 'Moderate increases', 'Substantial increases']
	df20['service delivery affect'] = df20['service delivery affect'].map({
	    'We have had to substantially cut back on our services because of COVID-19': 'Substantial cuts',
	    'We have had to make moderate cuts to our services because of COVID-19': 'Moderate cuts',
	    'We have had to make small cuts to our services because of COVID-19': 'Small cuts',
	    'We have maintained services at the same level': 'Same level of services',
	    'We have had to make some small increases in our service delivery to respond to COVID-19': 'Small increases',
	    'We have had to make moderate increases to our services because of COVID-19': 'Moderate increases',
	    'We have had to substantially expand our services to respond to COVID-19': 'Substantial increases',
	    "I'm not sure": 'Response'
	})
	df20['service delivery affect index'] = df20['service delivery affect'].map({c:i for i,c in enumerate(service_delivery_affect_order)})
	df21 = df21 \
	    .rename(columns={'To what level has your service delivery changed since pre-COVID-19 (March 2020)? (In terms of cuts or increases)': 'service delivery affect'})
	df21['service delivery affect index'] = df21['service delivery affect'].map({c:i for i,c in enumerate(service_delivery_affect_order)})

	funding_reserve_order = ['More than one year', 'Six to twelve months', 'Four to five months', 'Two to three months', 'Up to one month', 'None of the above', 'I\'m not sure']
	df20['funding reserve'] = df20['funding reserve'].map({
	    'We have sufficient funds to maintain staff and activity for more than one year': 'More than one year',
	    'We have sufficient funds to maintain staff and activity for six to 12 months': 'Six to twelve months',
	    'We have sufficient funds to maintain staff and activity for four to five months': 'Four to five months',
	    'We have sufficient funds to maintain staff and activity for two to three months': 'Two to three months',
	    'We have sufficient funds to maintain staff and activity for up to one month': 'Up to one month',
	})
	df20['funding reserve index'] = df20['funding reserve'].map({c:i for i,c in enumerate(funding_reserve_order)})
	df21 = df21 \
	    .rename(columns={'Based on your organisation\'s present financial reserves, approximately how long can you maintain your current levels of staff and/or service delivery?': 'funding reserve'})
	df21['funding reserve index'] = df21['funding reserve'].map({c:i for i,c in enumerate(funding_reserve_order)})
	return df20, df21
