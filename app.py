import streamlit as st
from fpdf import FPDF

st.header('PDF generator - test')
button1 = st.button('PDF')

if button1:
    name = st.text_input('Name', value='')
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font(family='Times', size=16)
    pdf.cell(40, 50, txt=name)

    st.download_button('Download PDF',
                       data=pdf,
                       file_name='pdf_test.pdf'
                       )
