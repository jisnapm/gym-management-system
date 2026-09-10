import streamlit as st
from gymViews import GymMemberManager

member_instance = GymMemberManager()
t1, t2 = st.tabs(["Add", "View"])

with t1:
    st.title("Add New Member")
    name = st.text_input("Enter Name: ")
    place = st.text_input("Enter Place: ")
    mobile = st.text_input("Enter Mobile: ")
    plan = st.text_input("Enter Plan: ")
    fee = st.text_input("Enter Fee: ")
    date = st.text_input("Enter Joined Date: ")
    if st.button("Add New Donor"):
        member_instance.post(name= name, place= place, mobile= mobile, plan= plan, fee= fee, joined_date=date)

with t2:
    st.title("View Members")