#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 13:09:35 2024

@author: sakurajima
"""
import json
import pandas as pd
from streamlit_elements import elements, dashboard, mui, nivo
import streamlit as st

st.set_page_config(layout="wide")


with open("horizonta_bar_dict.json", "r") as file:
    dictionary = json.load(file)


# Initialize the result dictionary with all months

# Define a default dashboard layout.
# Dashboard grid has 12 columns by default.
#
# For more information on available parameters:
# https://github.com/react-grid-layout/react-grid-layout#grid-item-props

layout = [
    # Editor item is positioned in coordinates x=0 and y=0,
    # and takes 6/12 columns and has a height of 3.
    dashboard.Item("editor", 0, 1, 6, 3),
    # Chart item is positioned in coordinates x=6 and y=0,
    # and takes 6/12 columns and has a height of 3.
    dashboard.Item("chart", 6, 1, 6, 3),
    # Media item is positioned in coordinates
    # x=0 and y=3, and takes 6/12 columns and has a height of 4.
    dashboard.Item("media", 0, 2, 12, 4),
]
# Create a frame to display elements.

with elements("demo"):

    # Create a new dashboard with the layout specified above.
    #
    # draggableHandle is a CSS query selector to define the draggable part of each dashboard item.
    # Here, elements with a 'draggable' class name will be draggable.
    #
    # For more information on available parameters for dashboard grid:
    # https://github.com/react-grid-layout/react-grid-layout#grid-layout-props
    # https://github.com/react-grid-layout/react-grid-layout#responsive-grid-layout-props

    with dashboard.Grid(layout, draggableHandle=".draggable"):

        # First card, the code editor.
        #
        # We use the 'key' parameter to identify the correct dashboard item.
        #
        # To make card's content automatically fill the height available, we will use CSS flexbox.
        # sx is a parameter available with every Material UI widget to define CSS attributes.
        #
        # For more information regarding Card, flexbox and sx:
        # https://mui.com/components/cards/
        # https://mui.com/system/flexbox/
        # https://mui.com/system/the-sx-prop/
        # We will use the same flexbox configuration as the first card to
        # auto adjust the content height.
        


        with mui.Card(key="editor", sx={"display": "flex", "flexDirection": "column"}):

            # To make this header draggable, we just need to set its classname to 'draggable',
            # as defined above in dashboard.Grid's draggableHandle.

            mui.CardHeader(title="Customer Net Margin", className="draggable")

            # Like above, we want to make our content grow and shrink as the user resizes the card,
            # by setting flex to 1 and minHeight to 0.

            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # For more information regarding other available Nivo charts:
                # https://nivo.rocks/

                nivo.Bar(
                    data=dictionary,
                    keys=["Gross Margin"],
                    indexBy="Customer",
                    margin={"top": 10, "right": 50, "bottom": 50, "left": 190}, #CUANDO NO CABE EL NOMBRE DEL EJE, AMPLIA EL MARGEN
                    padding=0.3,
                    layout="horizontal",
                    groupMode="grouped",
                    valueScale={"type": "linear"},
                    indexScale={"type": "band", "round": True},
                    valueFormat=" >+$,~r",
                    colors={"scheme": "nivo"},
                    colorBy="indexValue",
                    defs=[
                        {
                            "id": "dots",
                            "type": "patternDots",
                            "background": "inherit",
                            "color": "#38bcb2",
                            "size": 4,
                            "padding": 1,
                            "stagger": True,
                        },
                        {
                            "id": "lines",
                            "type": "patternLines",
                            "background": "inherit",
                            "color": "#eed312",
                            "rotation": -45,
                            "lineWidth": 6,
                            "spacing": 10,
                        },
                    ],
                    fill=[
                        {"match": {"id": "fries"}, "id": "dots"},
                        {"match": {"id": "sandwich"}, "id": "lines"},
                    ],
                    borderColor={"from": "color", "modifiers": [["darker", 1.6]]},
                    axisTop=None,
                    axisRight=None,
                    axisBottom={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 51,
                        "legend": "",
                        "legendPosition": "middle",
                        "legendOffset": 32,
                        "truncateTickAt": 0,
                    },
                    axisLeft={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "",
                        "legendPosition": "middle",
                        "legendOffset": -170, #POSISION DE LA LEGENDA
                        "truncateTickAt": 0,
                    },
                    enableLabel=False,
                    labelSkipWidth=12,
                    labelSkipHeight=12,
                    labelTextColor="#ffffff",
                    legends=[
],
                    role="application",
                    ariaLabel="Nivo bar chart demo",
                    barAriaLabel=lambda e: f"{e['id']}: {e['formattedValue']} in country: {e['indexValue']}",
                )
