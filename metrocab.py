import streamlit as st
name=st.text_input("Name")
mobile=st.text_input("Mobile No")
stations=["Select",
          "JNTUH",
          "MYP",
          "KPHB",
          "MGBS"]
from_station=st.selectbox("From Station",stations)
to_station=st.selectbox("To Station",stations)
tickets=st.number_input("Tickets",min_value=1,value=1)
cab_required=st.radio(
 "Do you need a Cab?",
    ["Yes","No"],index=None
)
if cab_required=="Yes":
    destination=st.text_input("Final Destination")
if st.button("Book"):
    if from_station==to_station:
        st.error("Please select correct stations")
    else:
        bill=tickets*20
        st.success(f"Booking confirmed! Total bill: ₹{bill}")
        st.subheader("Metro Ticket Details")
        st.write("Name:",name)
        st.write("Mobile :",mobile)
        st.write("From Station:",from_station)
        st.write("To Station:",to_station)
        st.write("Tickets:",tickets)
        if cab_required=="Yes":
            st.subheader("Cab Deatils")
            st.write("PickUp:",to_station)
            st.write("Drop:",destination)
        else:
            st.write("Cab not requires")