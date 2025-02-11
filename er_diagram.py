from graphviz import Digraph

# ER Diagram oluştur
er_diagram = Digraph('ER Diagram', filename='er_diagram', format='png')

# Varlıklar (Entities)
entities = [
    "CardTransaction", "Merchant", "Card", "Order", "Sector", "POS", "Location"
]

for entity in entities:
    er_diagram.node(entity, shape='box', style='filled', fillcolor='lightblue')

# İlişkiler (Relationships)
relationships = [
    ("CardTransaction", "Merchant", "Belongs To"),
    ("CardTransaction", "Card", "Uses"),
    ("CardTransaction", "Order", "Part of"),
    ("CardTransaction", "Sector", "Categorized As"),
    ("CardTransaction", "POS", "Processed By"),
    ("CardTransaction", "Location", "Happens At")
]

for src, dst, label in relationships:
    er_diagram.edge(src, dst, label)

# Diagramı kaydet ve göster
er_diagram_path = "C:\Program Files\Graphviz\bin"
er_diagram.render(er_diagram_path, format='png', cleanup=True)
er_diagram_path
