#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 15:08:00 2024

@author: Mauricio

Pendiente generar el bum_chart_data
"""

import json
import pandas as pd
from streamlit_elements import elements, dashboard, mui, nivo
import streamlit as st

st.set_page_config(layout="wide")
# As for Streamlit Elements, we will need all these objects.
# All available objects and there usage are listed there:
# https://github.com/okld/streamlit-elements#getting-started

with open("pie_dict.json", "r") as file:
    pie_data = json.load(file)
        
with open("bar_dict.json", "r") as file:
    bar_data = json.load(file)

with open("bum_dict.json", "r") as file:
    bump_chart_data = json.load(file)

# Define a default dashboard layout.
layout = [
    # and takes 6/12 columns and has a height of 3.
    dashboard.Item("bar_chart", 0, 1, 6, 3),
    # Chart item is positioned in coordinates x=6 and y=0,
    # and takes 6/12 columns and has a height of 3.
    dashboard.Item("pie", 6, 1, 6, 3),
    # Media item is positioned in coordinates
    # x=0 and y=3, and takes 6/12 columns and has a height of 4.
    dashboard.Item("area_bump", 0, 2, 12, 4),
]

custom_theme = {
    "axis": {
        "ticks": {
            "text": {"fill": "#d3d3d3"}  # Axis labels color
        },
        "legend": {
            "text": {"fill": "#4682b4"}  # Legend text color
        }
    },
    "tooltip": {
        "container": {
            "background": "#333",  # Tooltip background color
            "color": "#fff",        # Tooltip text color
            "fontSize": "14px",     # Tooltip font size
            "borderRadius": "5px",  # Tooltip border rounding
            "boxShadow": "0px 3px 6px rgba(0,0,0,0.2)",  # Tooltip shadow
        }
    }
}
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

        with mui.Card(key="pie", sx={"display": "flex", "flexDirection": "column"}):

            # To make this header draggable, we just need to set its classname to 'draggable',
            # as defined above in dashboard.Grid's draggableHandle.

            mui.CardHeader(title="Department Gross Margin", className="draggable")

            # Like above, we want to make our content grow and shrink as the user resizes the card,
            # by setting flex to 1 and minHeight to 0.

            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # This is where we will draw our Bump chart.
                #
                # For this exercise, we can just adapt Nivo's example and make
                # it work with Streamlit Elements.
                # Nivo's example is available in the 'code' tab there:
                # https://nivo.rocks/bump/
                #
                # Data takes a dictionary as parameter, so we need to convert
                # our JSON data from a string to
                # a Python dictionary first, with `json.loads()`.
                #
                # For more information regarding other available Nivo charts:
                # https://nivo.rocks/

                nivo.Pie(
                    data=pie_data,
                    margin={"top": 40, "right": 80, "bottom": 80, "left": 80},
                    valueFormat=" >+$,~r",
                    innerRadius=0.5,
                    padAngle=0.7,
                    cornerRadius=3,
                    activeOuterRadiusOffset=8,
                    borderWidth=1,
                    borderColor={"from": "color", "modifiers": [["darker", 0.2]]},
                    arcLinkLabelsSkipAngle=10,
                    arcLinkLabelsTextColor="#d3d3d3",
                    arcLinkLabelsThickness=2,
                    arcLinkLabelsColor={"from": "color"},
                    arcLabelsSkipAngle=10,
                    arcLabelsTextColor="#d3d3d3",

                    defs=[
                        {
                            "id": "dots",
                            "type": "patternDots",
                            "background": "inherit",
                            "color": "rgba(255, 255, 255, 0.3)",
                            "size": 4,
                            "padding": 1,
                            "stagger": True,
                        },
                        {
                            "id": "lines",
                            "type": "patternLines",
                            "background": "inherit",
                            "color": "rgba(255, 255, 255, 0.3)",
                            "rotation": -45,
                            "lineWidth": 6,
                            "spacing": 10,
                        },
                    ],
                    fill=[
                        {"match": {"id": "ruby"}, "id": "dots"},
                        {"match": {"id": "c"}, "id": "dots"},
                        {"match": {"id": "go"}, "id": "dots"},
                        {"match": {"id": "python"}, "id": "dots"},
                        {"match": {"id": "scala"}, "id": "lines"},
                        {"match": {"id": "lisp"}, "id": "lines"},
                        {"match": {"id": "elixir"}, "id": "lines"},
                        {"match": {"id": "javascript"}, "id": "lines"},
                    ],
                    legends=[
                        {
                            "anchor": "bottom",
                            "direction": "row",
                            "justify": False,
                            "translateX": 0,
                            "translateY": 56,
                            "itemsSpacing": 0,
                            "itemWidth": 100,
                            "itemHeight": 18,
                            "itemTextColor": "#999",
                            "itemDirection": "left-to-right",
                            "itemOpacity": 1,
                            "symbolSize": 18,
                            "symbolShape": "circle",
                            "effects": [
                                {"on": "hover", "style": {"itemTextColor": "#000"}}
                            ],
                        }
                    ],
                )
        with mui.Card(key="bar_chart", sx={"display": "flex", "flexDirection": "column"}):

            # To make this header draggable, we just need to set its classname to 'draggable',
            # as defined above in dashboard.Grid's draggableHandle.

            mui.CardHeader(title="Gross Margin", className="draggable")

            # Like above, we want to make our content grow and shrink as the user resizes the card,
            # by setting flex to 1 and minHeight to 0.

            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # For more information regarding other available Nivo charts:
                # https://nivo.rocks/

                nivo.Bar(
                    data=bar_data,
                    keys=["2023", "2024"],
                    indexBy="month",
                    margin={"top": 50, "right": 130, "bottom": 50, "left": 60},
                    padding=0.3,
                    groupMode="grouped",
                    valueScale={"type": "linear"},
                    indexScale={"type": "band", "round": True},
                    valueFormat=" >+$,~r",
                    theme=custom_theme,
                    colors={"scheme": "paired"},
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
                        "tickRotation": 0,
                        "legend": "",
                        "legendPosition": "middle",
                        "legendOffset": 32,
                        "truncateTickAt": 0,
                    },
                    axisLeft={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "Gross Margin",
                        "legendPosition": "middle",
                        "legendOffset": -52,
                        "truncateTickAt": 0,
                    },
                    enableLabel=False,
                    labelSkipWidth=12,
                    labelSkipHeight=12,
                    labelTextColor="#ffffff",
                    legends=[
                        {
                            "dataFrom": "keys",
                            "anchor": "bottom-right",
                            "direction": "column",
                            "justify": False,
                            "translateX": 120,
                            "translateY": 0,
                            "itemsSpacing": 2,
                            "itemWidth": 100,
                            "itemHeight": 20,
                            "itemTextColor": "#999",
                            "itemDirection": "left-to-right",
                            "itemOpacity": 0.85,
                            "symbolSize": 20,
                            "effects": [{"on": "hover", "style": {"itemOpacity": 1}}],
                        }
                    ],
                    role="application",
                    ariaLabel="Nivo bar chart demo",
                    barAriaLabel=lambda e: f"{e['id']}: {e['formattedValue']} in country: {e['indexValue']}",
                )
        with mui.Card(key="area_bump", sx={"display": "flex", "flexDirection": "column"}):

            mui.CardHeader(
                title="Sales Executive ranking evolution", className="draggable"
            )

            with mui.CardContent(sx={"flex": 1, "minHeight": 600}):
                with mui.Box(sx={"height": 500}):
                    nivo.AreaBump(
                        data=bump_chart_data,
                        margin={"top": 40, "right": 100, "bottom": 40, "left": 100},
                        spacing=8,
                        colors={"scheme": "nivo"},
                        blendMode="multiply",
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
                            {"match": {"id": "CoffeeScript"}, "id": "dots"},
                            {"match": {"id": "TypeScript"}, "id": "lines"},
                        ],
                        startLabel="id",
                        endLabel="id",
                        axisTop={
                            "tickSize": 5,
                            "tickPadding": 5,
                            "tickRotation": 0,
                            "legend": "",
                            "legendPosition": "middle",
                            "legendOffset": -36,
                            "truncateTickAt": 0,
                        },
                        axisBottom={
                            "tickSize": 5,
                            "tickPadding": 5,
                            "tickRotation": 0,
                            "legend": "",
                            "legendPosition": "middle",
                            "legendOffset": 32,
                            "truncateTickAt": 0,
                        },
                    )
