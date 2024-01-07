import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('india.csv')


list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Overall India')

st.sidebar.title("India Demographic visualization")

selected_state = st.sidebar.selectbox("Select a state",list_of_states)

Primary = st.sidebar.selectbox("Select Primary Parameter",sorted(df.columns[5:]))
Secondary = st.sidebar.selectbox("Select Secondary Parameter",sorted(df.columns[5:]))

plot = st.sidebar.button("Plot Graph")

if plot:
    
    if selected_state == "Overall India":
        #plot for india
        
        fig = px.scatter_mapbox(df,lat="Latitude",lon="Longitude", size=Primary, color=Secondary  ,zoom=4
                            , size_max=35, color_continuous_scale=px.colors.sequential.Viridis, mapbox_style="carto-positron", width=1200, height=700, hover_name="District")
        
        st.plotly_chart(fig,use_container_width=True)
        
        
    else:
        state_df=  df[df["State"]== selected_state]
        
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size=Primary, color=Secondary, zoom=4
                                , size_max=35, color_continuous_scale=px.colors.sequential.Viridis, mapbox_style="carto-positron",width=1200,height=700,hover_name='District')

        st.plotly_chart(fig,use_container_width=True)