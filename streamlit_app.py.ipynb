{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "bc5bec3d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import plost\n",
    "from PIL import Image\n",
    "\n",
    "# Page setting\n",
    "st.set_page_config(layout=\"wide\")\n",
    "\n",
    "with open('style.css') as f:\n",
    "    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)\n",
    "\n",
    "# Data\n",
    "seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])\n",
    "stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')\n",
    "\n",
    "# Row A\n",
    "a1, a2, a3 = st.columns(3)\n",
    "a1.image(Image.open('streamlit-logo-secondary-colormark-darktext.png'))\n",
    "a2.metric(\"Wind\", \"9 mph\", \"-8%\")\n",
    "a3.metric(\"Humidity\", \"86%\", \"4%\")\n",
    "\n",
    "# Row B\n",
    "b1, b2, b3, b4 = st.columns(4)\n",
    "b1.metric(\"Temperature\", \"70 °F\", \"1.2 °F\")\n",
    "b2.metric(\"Wind\", \"9 mph\", \"-8%\")\n",
    "b3.metric(\"Humidity\", \"86%\", \"4%\")\n",
    "b4.metric(\"Humidity\", \"86%\", \"4%\")\n",
    "\n",
    "# Row C\n",
    "c1, c2 = st.columns((7,3))\n",
    "with c1:\n",
    "    st.markdown('### Heatmap')\n",
    "    plost.time_hist(\n",
    "    data=seattle_weather,\n",
    "    date='date',\n",
    "    x_unit='week',\n",
    "    y_unit='day',\n",
    "    color='temp_max',\n",
    "    aggregate='median',\n",
    "    legend=None)\n",
    "with c2:\n",
    "    st.markdown('### Bar chart')\n",
    "    plost.donut_chart(\n",
    "        data=stocks,\n",
    "        theta='q2',\n",
    "        color='company')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "17c87d01",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
