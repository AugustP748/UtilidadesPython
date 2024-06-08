import plotly.express as px
import pandas as pd

# Datos de muestra
df = pd.DataFrame(dict(
    valor = [8, 12, 7, 14, 10],
    variable = ['V1', 'V2', 'V3', 'V4', 'V5']))
           
fig = px.line_polar(df, r = 'valor', theta = 'variable', line_close = True,
                    text = 'valor')
fig.update_traces(fill = 'toself', textposition = 'top center')

fig.show() 
 
