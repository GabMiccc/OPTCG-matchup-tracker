import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# Imposta la larghezza della pagina a "wide"
st.set_page_config(layout="wide")

leader_list = [ 'zoroOP01',
                'lawOP01',
                'doffyOP01',
                'whitebeardOP02',
                'smokerOP02',
                'namiOP03',
                'belobettyOP05',
                'luffyOP05',
                'enelOP05',
                'yamatoOP06',
                'peronaOP06',
                'reijuOP06',
                'moriaOP06',
                'bonneyOP07',
                'lucciOP07',
                'boaOP07',
                'marcoOP08',
                'puddingOP08',
                'kalgaraOP08',
                'luffyST10',
                'kidST10',
                'utaST11',
                'luffyST13',
                'luffyST14',
                'shanksOP09',
                'limOP09',
                'buggyOP09',
                'blackbeardOP09',
                'sanjiPRB01',
                'kidOP10',
                'usoppOP10',
                'smokerOP10'
                ]


leaders_png = [ 'https://onepiecetopdecks.com/wp-content/gallery/op01/OP01-001.jpg', 
                'https://onepiecetopdecks.com/wp-content/gallery/op01/op01-002a.jpg',
                'https://onepiecetopdecks.com/wp-content/gallery/op01/OP01-060A.jpg',
                'https://onepiecetopdecks.com/wp-content/gallery/op02/OP02-001a.jpg',
                'https://onepiecetopdecks.com/wp-content/gallery/op02/OP02-093_p1.png',
                'https://onepiecetopdecks.com/wp-content/gallery/op03/OP03-040_p1.jpg',
                'https://onepiecetopdecks.com/wp-content/gallery/op05/op05-002p.jpg',
                'https://onepiecetopdecks.com/wp-content/gallery/op05/op05-060p.jpg',
                'https://onepiecetopdecks.com/wp-content/gallery/op05/op05-098p.jpg',
                'https://onepiecetopdecks.com/wp-content/gallery/op06/OP06-022_p1.jpg',
                'https://onepiecetopdecks.com/wp-content/gallery/op06/OP06-021_p1.jpg',
                'https://onepiecetopdecks.com/wp-content/gallery/op06/OP06-042_p1.jpg',
                'https://onepiecetopdecks.com/wp-content/gallery/op06/OP06-080_p1.jpg',
                'https://onepiecetopdecks.com/wp-content/gallery/op07/OP07-019-AA.jpg',
                'https://onepiecetopdecks.com/wp-content/gallery/op07/OP07-079-AA.jpg',
                'https://onepiecetopdecks.com/wp-content/gallery/op07/OP07-038.jpg',
                'https://onepiecetopdecks.com/wp-content/gallery/op08/OP08-002_p1.png',
                'https://onepiecetopdecks.com/wp-content/gallery/op08/OP08-058_p1.png',
                'https://onepiecetopdecks.com/wp-content/gallery/op08/OP08-098_p1.png',
                'https://onepiecetopdecks.com/wp-content/gallery/st10/ST10-002.jpg',
                'https://onepiecetopdecks.com/wp-content/gallery/st10/ST10-003.jpg',
                'https://onepiecetopdecks.com/wp-content/gallery/st11/ST11-001.jpg',
                'https://onepiecetopdecks.com/wp-content/gallery/st13/ST13-003_p1.jpg',
                'https://onepiecetopdecks.com/wp-content/gallery/st14/ST14-001.jpg',
                'https://onepiecetopdecks.com/wp-content/gallery/op09/op09-001-aa.jpg',
                'https://onepiecetopdecks.com/wp-content/gallery/op09/op09-022-aa.jpg',
                'https://onepiecetopdecks.com/wp-content/gallery/op09/op09-042-aa.jpg',
                'https://onepiecetopdecks.com/wp-content/gallery/op09/op09-081-aa.jpg',
                'https://onepiecetopdecks.com/wp-content/gallery/prb01/PRB01-001_p1.png',
                'https://onepiecetopdecks.com/wp-content/gallery/op10/OP10-099.jpg',
                'https://onepiecetopdecks.com/wp-content/gallery/op10/OP10-042.jpg',
                'https://onepiecetopdecks.com/wp-content/gallery/op10/OP10-001.jpg'
                ]

leader_images = dict(zip(leader_list, leaders_png))

# Inizializza i dati della tabella
data = {}
for leader1 in leader_list:
    data[leader1] = {}
    for leader2 in leader_list:
        data[leader1][leader2] = 50  # Valore di default

# Aggiungi CSS personalizzato per rimuovere margini e padding
st.markdown(
    """
    <style>
    body, html {
        margin: 0;
        padding: 0;
    }
    .custom-table-container {
        width: 100%;
        margin: 0;
        padding: 0;
    }
    table {
        width: 100%;
        border-collapse: collapse;
    }
    th, td {
        width:50px;  
        box-sizing: border-box;
        padding: 0;
        margin: 0;
        text-align: center;
    }
    th img, td img {
        display: block;
        margin: 0 auto;
        width: 40px;
    }
    td input {
        width: 40px;                                /* Imposta la larghezza delle caselle di input */
        box-sizing: border-box;
        padding: 0;
        margin: 0 auto;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Crea la tabella HTML con stili CSS e contenitore div
html_table = """
<div class="custom-table-container">
    <table>
        <tr>
            <th></th>
"""

for leader in leader_list:
    html_table += f"<th><img src='{leader_images[leader]}' width='50'></th>"
html_table += "</tr>"

for leader1 in leader_list:
    html_table += f"<tr><th><img src='{leader_images[leader1]}' width='50'></th>"
    for leader2 in leader_list:
        html_table += f"<td><input type='number' value='{data[leader1][leader2]}' id='{leader1}-{leader2}' onchange='updateData(\"{leader1}\", \"{leader2}\", this.value)'></td>"
    html_table += "</tr>"

html_table += "</table></div>"

#####   # Visualizza la tabella HTML con st.components.v1.html
#####   components.html(html_table, height=1500, scrolling=True)

# JavaScript per aggiornare i dati
js = """
<script>
function updateData(leader1, leader2, value) {
    Streamlit.setComponentValue({ leader1: leader1, leader2: leader2, value: value });
}
</script>
"""

# Visualizza la tabella HTML e JavaScript
components.html(html_table + js, height=1500, scrolling=True)

# Gestione dei dati modificati tramite st.session_state
component_value = st.session_state.get("component_value")
if component_value:
    data[component_value['leader1']][component_value['leader2']] = int(component_value['value'])
    st.write(data)  # Visualizza i dati aggiornati