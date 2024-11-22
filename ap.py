
import streamlit as st
import numpy as np
# Resonance function
def Resonance(R, L, C):
    FR = 1 / (2 * np.pi * np.sqrt(L * C))
    BW = R / (2 * np.pi * L)
    Q = FR / BW
    FL = FR - BW / 2
    FU = FR + BW / 2
    return FR, BW, Q, FL, FU

# Streamlit App
def main():
    st.title("2305A21L44-03")  # Replace with your actual roll number and problem statement number
    
    st.write("This app calculates the resonance frequency (FR), band width (BW), quality factor (Q), upper cutoff frequency (FU), and lower cutoff frequency (FL) of a series resonance circuit.")
    
    R = st.number_input("Enter Resistance (R) in Ohms:")
    L = st.number_input("Enter Inductance (L) in Henries:")
    C = st.number_input("Enter Capacitance (C) in Farads:")
    
    if st.button("Calculate"):
        FR, BW, Q, FL, FU = Resonance(R, L, C)
        st.write(f"Resonance Frequency (FR): {FR:.2f} Hz")
        st.write(f"Band Width (BW): {BW:.2f} Hz")
        st.write(f"Quality Factor (Q): {Q:.2f} Hz")
        st.write(f"Lower Cutoff Frequency (FL): {FL:.2f} Hz")
        st.write(f"Upper Cutoff Frequency (FU): {FU:.2f} Hz")

if __name__ == "__main__":
    main()
