import streamlit as st
import pickle
from prediction_models import *
from logger import get_log

logger = get_log('app')

def main():
    try:
        html_temp = """
        <div style="padding:10px">
        <h1 style="color:white;text-align:center">AI4I Prediction</h1>
        </div> 
        """

        st.markdown(html_temp,unsafe_allow_html=True)

        nav = st.sidebar.selectbox("Select a model",['','Linear Regression','Lasso Regression','Ridge Regression','ElasticNet Regression'])

        home_temp = """
        <div style="padding:10px">
            <h3 style="color:#E9EFF4; text-align:center">Welcome to AI4I Prediction</h3>
            <h4 style="color:#E9EFF4; text-align:center">here, we can use the following models to predict the Air Temperature <br>
                Using inputs Process Temperature, TWF, HDF, PWF, OSF, RNF 
            </h4>
            <br>
            <h4 style="color:#E9EFF4; text-align:center">Below are the list of Models available for prediction</h4>
            <br>
                <div style="color:#E9EFF4; text-align:center">
                    <li>Linear Regression model</li>
                    <li>Lasso Regression model</li>
                    <li>Ridge Regression model</li>
                    <li>ElasticNet Regression model</li>
                </div>
            <br>
            <h5 style="color:#E9EFF4; text-align:center">Note: Please use sidebar for navigating to desired model</h5>
        </div> 
        """

        if nav == "":
            st.markdown(home_temp,unsafe_allow_html=True)
            # st.balloons()

        if nav == "Linear Regression":

            logger.info("Linear Regression Selected")

            pro_temp = st.number_input("Process Temperature")
            type_en = st.text_input("Type",max_chars=1)
            st.text('value should be between 1 to 3, 1 = L, M = 2, H = 3')
            twf = st.text_input("TWF",max_chars=1)
            hdf = st.text_input("HDF",max_chars=1)
            st.text('value should be 0 or 1 ')
            pwf = st.text_input("PWF",max_chars=1)
            st.text('value should be 0 or 1 ')
            osf = st.text_input("OSF",max_chars=1)
            st.text('value should be 0 or 1 ')
            rnf = st.text_input("RNF",max_chars=1)
            st.text('value should be 0 or 1 ')

            if st.button("Predict"):
                linear_Prediction = linear_model(int(pro_temp),int(type_en),int(twf),int(hdf),int(pwf),int(osf),int(rnf))
                st.write("The Air Temperature for the given Input is ",linear_Prediction)

        if nav == "Lasso Regression":

            logger.info("Lasso Regression Selected")

            pro_temp = st.number_input("Process Temperature")
            type_en = st.text_input("Type",max_chars=1)
            st.text('value should be between 1 to 3, 1 = L, M = 2, H = 3')
            twf = st.text_input("TWF",max_chars=1)
            st.text('value should be 0 or 1 ')
            hdf = st.text_input("HDF",max_chars=1)
            st.text('value should be 0 or 1 ')
            pwf = st.text_input("PWF",max_chars=1)
            st.text('value should be 0 or 1 ')
            osf = st.text_input("OSF",max_chars=1)
            st.text('value should be 0 or 1 ')
            rnf = st.text_input("RNF",max_chars=1)
            st.text('value should be 0 or 1 ')

            if st.button("Predict"):
                lasso_Prediction = lasso_model(int(pro_temp),int(type_en),int(twf),int(hdf),int(pwf),int(osf),int(rnf))
                st.write("The Air Temperature for the given Input is ",lasso_Prediction)

        if nav == "Ridge Regression":

            logger.info("Linear Regression Selected")

            pro_temp = st.number_input("Process Temperature")
            type_en = st.text_input("Type",max_chars=1)
            st.text('value should be between 1 to 3, 1 = L, M = 2, H = 3')
            twf = st.text_input("TWF",max_chars=1)
            st.text('value should be 0 or 1 ')
            hdf = st.text_input("HDF",max_chars=1)
            st.text('value should be 0 or 1 ')
            pwf = st.text_input("PWF",max_chars=1)
            st.text('value should be 0 or 1 ')
            osf = st.text_input("OSF",max_chars=1)
            st.text('value should be 0 or 1 ')
            rnf = st.text_input("RNF",max_chars=1)
            st.text('value should be 0 or 1 ')

            if st.button("Predict"):
                ridge_Prediction = ridge_model(int(pro_temp),int(type_en),int(twf),int(hdf),int(pwf),int(osf),int(rnf))
                st.write("The Air Temperature for the given Input is ",ridge_Prediction)

        if nav == "ElasticNet Regression":

            logger.info("Linear Regression Selected")

            pro_temp = st.number_input("Process Temperature")
            type_en = st.text_input("Type",max_chars=1)
            st.text('value should be between 1 to 3, 1 = L, M = 2, H = 3')
            twf = st.text_input("TWF",max_chars=1)
            st.text('value should be 0 or 1 ')
            hdf = st.text_input("HDF",max_chars=1)
            st.text('value should be 0 or 1 ')
            pwf = st.text_input("PWF",max_chars=1)
            st.text('value should be 0 or 1 ')
            osf = st.text_input("OSF",max_chars=1)
            st.text('value should be 0 or 1 ')
            rnf = st.text_input("RNF",max_chars=1)
            st.text('value should be 0 or 1 ')

            if st.button("Predict"):
                elastic_Prediction = elasticnet_model(int(pro_temp),int(type_en),int(twf),int(hdf),int(pwf),int(osf),int(rnf))
                st.write("The Air Temperature for the given Input is ",elastic_Prediction)
    except Exception as e:
        logger.error(e)
        st.error("Something went wrong")

if __name__ == '__main__':
    main()