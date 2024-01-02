import streamlit as st 
import joblib
import pandas 
import numpy

model = joblib.load('laptop_price_model.pkl')
st.header("Laptop Price Prediction App")
col1,col2 = st.columns(2)

with col1:
    choice = ('Apple','Hp','Acer','Asus','Dell','Lenovo','Chuwi','MSI',
               'Microsoft','Toshiba','Huawei','Xioami','Vero','Razer',
               'Mediacom','Samsung','Google','Fujitsu','LG')
    option = list(range(len(choice)))
    p1 = st.selectbox("Laptop Type",option, format_func=lambda x: choice[x])
with col2:
    choice = ('Ultrabook','Notebook','Netbook','Gaming','2 in 1 convertible','Workstation')
    option = list(range(len(choice)))
    p2 = st.selectbox("Laptop type Name",option, format_func=lambda x: choice[x])
with col1:
    choice = ('macOS','No OS','Windows 10','Windows 7','Mac OS X','Linux','Android','Windows 10 S',
              'Chrome OS')
    option = list(range(len(choice)))
    p3 = st.selectbox("Operating System",option, format_func=lambda x: choice[x])
with col2:
    choice = ('Yes','No')
    option = list(range(len(choice)))
    p4 = st.selectbox("TouchScreen",option, format_func=lambda x: choice[x])
with col1:
    choice = ('2560','1440','1920','2880','1366','2304','3200','2256','3840','2160','1600','2736','2400')
    option = list(range(len(choice)))
    p5 = st.selectbox("Screen Width",option, format_func=lambda x: choice[x])
with col2:
    choice = ('1600','900','1080','1800','768','1440','1200','1504','2160','1824')
    option = list(range(len(choice)))
    p6 = st.selectbox("Screen Height",option, format_func=lambda x: choice[x])
with col1:
    choice = ('Intel','AMD','Samsung')
    option = list(range(len(choice)))
    p7 = st.selectbox("CPu Brand",option, format_func=lambda x: choice[x])
with col2:
    choice = ('128','256','512','500','1000','32','64','2000','16','180','240','8','508')
    option = list(range(len(choice)))
    p8 = st.selectbox("Memory in GB",option, format_func=lambda x: choice[x])
with col1:
    choice = ('SSD','HDD','Flash','Hybrid')
    option = list(range(len(choice)))
    p9 = st.selectbox("Memory Type",option, format_func=lambda x: choice[x])
with col2:
    choice = ('Intel', 'AMD', 'Nvidia', 'ARM')
    option = list(range(len(choice)))
    p10 = st.selectbox("GPU brand",option, format_func=lambda x: choice[x])
with col1:
    p11 = st.slider("Frequency Ghz",0.9,3.6)
with col2:
    p12 = st.slider("Ram in GB",2,64,step=2)
with col1:
    p13 = st.slider("Size in Inches",10.1,18.4)
with col2:
    p14 = st.slider("Weight in Kg",0.69,4.6)

if st.button("Predict Price"):
    result = model.predict([[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14]])
    st.success("The price of the laptop is {:.0f} dollars".format(result[0]))
