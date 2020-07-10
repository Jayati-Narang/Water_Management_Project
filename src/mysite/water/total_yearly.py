import plotly.graph_objects as go
import plotly.express as px
import chart_studio
import chart_studio.plotly as py
import plotly.io as pio
from models import Final
x = ['old_qtr','ananda_nivas', 'budha_nivas', 'palash', 'kadamb', 'parijaat', 'bakul', 'sahana_aithi_house', 'nilgiri', 'vindhya', 'admin_block', 'krb', 'bodh']
y, z = Final.get_avg_by_block(Final)

# Use textposition='auto' for direct text
fig = go.Figure(data=[go.Bar(
            x=x, y=y,
            text=y,
            textposition='auto',
        )])

fig.show()
