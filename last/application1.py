import pandas as pd
import streamlit as st
import pickle as pk

# Load your data
df = pd.read_pickle('C:/Users/bavan/Downloads/last/top_mobile_phones.pkl')

# Mobile data
mobile_data = pd.DataFrame({
    'Product Name': ['SAMSUNG Galaxy S23 FE', 'Motorola Edge 50 Pro 5G with 125W Charger', 'realme 12 Pro+ 5G', 'Apple iPhone 12', 'OnePlus Nord 3 5G'],
    'Price': [29999, 29999, 26999, 39900, 22399],
    'brand': ['Samsung', 'Motorola', 'Realme', 'Apple', 'OnePlus'],
    'urls': [
        'https://www.flipkart.com/samsung-galaxy-s23-fe-graphite-128-gb/p/itme751066521899?pid=MOBGVTA2836DQWTT&lid=LSTMOBGVTA2836DQWTTISGIME&marketplace=FLIPKART&q=20000+to+40000+mobile&store=tyy%2F4io&srno=s_1_11&otracker=AS_Query_OnlineSuffix_1_17_na_na_na&otracker1=AS_Query_OnlineSuffix_1_17_na_na_na&fm=organic&iid=ec5ee332-7942-414f-a948-0ca137688ad2.MOBGVTA2836DQWTT.SEARCH&ppt=clp&ppn=mobile-phones-store&ssid=j84nckqg5s0000001728217254232&qH=e28ec92a51ccd8a6',
        'https://www.flipkart.com/motorola-edge-50-pro-5g-125w-charger-moonlight-pearl-256-gb/p/itm58844545548bd?pid=MOBGXFXYK3GVSARU&lid=LSTMOBGXFXYK3GVSARULH9LJF&marketplace=FLIPKART&q=20000+to+40000+mobile&store=tyy%2F4io&srno=s_2_37&otracker=AS_Query_OnlineSuffix_1_17_na_na_na&otracker1=AS_Query_OnlineSuffix_1_17_na_na_na&fm=search-autosuggest&iid=528b9b1c-4b01-423d-91f0-2bbca373ea0d.MOBGXFXYK3GVSARU.SEARCH&ppt=sp&ppn=sp&qH=e28ec92a51ccd8a6',
        'https://www.flipkart.com/realme-12-pro-5g-explorer-red-256-gb/p/itm7f042fb6aebdb?pid=MOBGWH8SB4QUY3H7&lid=LSTMOBGWH8SB4QUY3H7UBIQFM&marketplace=FLIPKART&q=20000+to+40000+mobile&store=tyy%2F4io&srno=s_2_39&otracker=AS_Query_OnlineSuffix_1_17_na_na_na&otracker1=AS_Query_OnlineSuffix_1_17_na_na_na&fm=search-autosuggest&iid=528b9b1c-4b01-423d-91f0-2bbca373ea0d.MOBGWH8SB4QUY3H7.SEARCH&ppt=sp&ppn=sp&qH=e28ec92a51ccd8a6',
        'https://www.flipkart.com/apple-iphone-12-blue-128-gb/p/itm02853ae92e90a?pid=MOBFWBYZKPTZF9VG&lid=LSTMOBFWBYZKPTZF9VGHUA0UC&marketplace=FLIPKART&q=20000+to+40000+mobile&store=tyy%2F4io&srno=s_1_2&otracker=AS_Query_OnlineSuffix_1_17_na_na_na&otracker1=AS_Query_OnlineSuffix_1_17_na_na_na&fm=search-autosuggest&iid=0228e3cd-b3ac-4e34-95b5-a66ec521c4c0.MOBFWBYZKPTZF9VG.SEARCH&ppt=sp&ppn=sp&qH=e28ec92a51ccd8a6',
        'https://www.flipkart.com/oneplus-nord-3-5g-tempest-gray-128-gb/p/itm5fc87afce35dc?pid=MOBGRK2VXCKBADB5&lid=LSTMOBGRK2VXCKBADB5XYKXX3&marketplace=FLIPKART&q=20000+to+40000+mobile&store=tyy%2F4io&srno=s_1_3&otracker=AS_Query_OnlineSuffix_1_17_na_na_na&otracker1=AS_Query_OnlineSuffix_1_17_na_na_na&fm=search-autosuggest&iid=2e7f1777-2272-4777-9239-362acaed3b0c.MOBGRK2VXCKBADB5.SEARCH&ppt=sp&ppn=sp&qH=e28ec92a51ccd8a6'
    ]
})

df['Product Name'] = df['Product Name'].str.extract(r'([A-Za-z0-9\s\+]+)')[0].str.strip()

# Merge the dataframes
ds = pd.merge(df, mobile_data, on='Product Name', how='left')

# Streamlit app starts here
st.title('Flipkart Mobile Phone Recommendation')
st.write('Based on Sentiment analysis')

# Sidebar for brand selection
brand_options = ds['brand'].unique()
selected_brand = st.sidebar.selectbox("Select Brand:", brand_options)

# Sidebar for price range filtering
price_filter = st.sidebar.slider("Select Price Range (in INR):", min_value=20000, max_value=40000, value=(30000, 40000))

# Filter the DataFrame based on selected options
filtered_phones = ds[
    (ds['brand'] == selected_brand) 
]

# Display the results
if not filtered_phones.empty:
    for _, row in filtered_phones.iterrows():
        prompt = f"""
        Based on sentiment analysis, we recommend the following mobile phone:

        **Model**: {row['Product Name']}\n 
        Positive review Count: {row['average_sentiment']}\n
        Price: ₹{row['Price']}\n
        URLs: {row['urls']}\n
        """
        st.write(prompt)
else:
    st.write("No mobile phones available in this brand.")
