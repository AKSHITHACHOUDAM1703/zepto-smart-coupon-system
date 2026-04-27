import streamlit as st
import random
import string

st.set_page_config(page_title="Zepto Smart Coupon", page_icon="🛒")

st.title("🛒 Zepto Smart Coupon System")

# Session state
if "user_id" not in st.session_state:
    st.session_state.user_id = None

if st.session_state.user_id is None:
    user_id = st.number_input("Enter User ID", min_value=1)

    if st.button("Enter"):
        st.session_state.user_id = user_id
        st.rerun()

else:
    st.write(f"User ID: {st.session_state.user_id}")

    cart_value = st.number_input("Enter Cart Value (₹)", min_value=0)

    if st.button("Get Coupon"):
        coupon = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
        st.success("🎉 ₹150 OFF Coupon Generated!")
        st.code(coupon)

    if st.button("Change User"):
        st.session_state.user_id = None
        st.rerun()
