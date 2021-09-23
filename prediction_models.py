import streamlit as st
import pickle
from logger import get_log

logger = get_log('prediction_models')

def linear_model(pro_temp,type_en,twf,hdf,pwf,osf,rnf):
    try:
        standard_data = pickle.load(open('standardscalar.sav','rb'))
        logger.info("Data Tranformed into Standard Scalar")
        transformed_data = standard_data.transform([[pro_temp,type_en,twf,hdf,pwf,osf,rnf]])
        print(transformed_data)

        linear = pickle.load(open('linearregression.pickle','rb'))
        logger.info("Linear Model Loaded")
        lr = linear.predict(transformed_data)
        return lr
    except Exception as e:
        logger.error("The error is : ",e)
        st.error("Something went Wrong",e)


def lasso_model(pro_temp,type_en,twf,hdf,pwf,osf,rnf):
    try:
        standard_data = pickle.load(open('standardscalar.sav','rb'))
        logger.info("Data Tranformed into Standard Scalar")
        transformed_data = standard_data.transform([[pro_temp,type_en,twf,hdf,pwf,osf,rnf]]) 

        lasso = pickle.load(open('lassoregression.pickle','rb'))
        logger.info("Lasso Model Loaded")
        ls = lasso.predict(transformed_data)
        return ls
    except Exception as e:
        logger.error("The error is : ",e)
        st.error("Something went Wrong",e)    

def ridge_model(pro_temp,type_en,twf,hdf,pwf,osf,rnf):
    try:
        standard_data = pickle.load(open('standardscalar.sav','rb'))
        logger.info("Data Tranformed into Standard Scalar")
        transformed_data = standard_data.transform([[pro_temp,type_en,twf,hdf,pwf,osf,rnf]]) 

        ridge = pickle.load(open('ridgeregression.pickle','rb'))
        logger.info("Ridge Model Loaded")
        rd = ridge.predict(transformed_data)
        return rd
    except Exception as e:
        logger.error("The error is : ",e)
        st.error("Something went Wrong",e)

def elasticnet_model(pro_temp,type_en,twf,hdf,pwf,osf,rnf):
    try:
        standard_data = pickle.load(open('standardscalar.sav','rb'))
        logger.info("Data Tranformed into Standard Scalar")
        transformed_data = standard_data.transform([[pro_temp,type_en,twf,hdf,pwf,osf,rnf]]) 

        elastic = pickle.load(open('elasticregression.pickle','rb'))
        logger.info("ElasticNet Model Loaded")
        en = elastic.predict(transformed_data)
        return en
    except Exception as e:
        logger.error("The error is : ",e)
        st.error("Something went Wrong",e)