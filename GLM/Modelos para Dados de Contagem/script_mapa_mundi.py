import pandas as pd
import plotly.express as px
import webbrowser

# Fisman, R.; Miguel, E. Corruption, Norms, and Legal Enforcement: Evidence
#from Diplomatic Parking Tickets.
# Journal of Political Economy, v. 15, n. 6, p. 1020-1048, 2007.
# https://www.journals.uchicago.edu/doi/abs/10.1086/527495

df_corruption = pd.read_csv('data/corruption.csv', delimiter=',')

# Mapa-múndi
fig = px.choropleth(df_corruption, 
                    locations='code',  # Código ISO dos países
                    color='corruption',
                    hover_name='country',  # Informações que aparecerão ao passar o mouse
                    color_continuous_scale=px.colors.sequential.RdBu_r,  # Escala de cores
                    projection="natural earth",  # Projeção do mapa
                    title="Mapa de Corrupção por País")

fig.write_html("mapa_corrupcao.html")

webbrowser.open("mapa_corrupcao.html")