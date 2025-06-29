import graphviz


def build_flowchart():
    """
    Returns SVG string of main logic flowchart.
    """
    dot = graphviz.Digraph(format='svg')
    steps = ['Start', 'Connect Wi-Fi', 'MQTT Init', 'Read Sensors', 'Publish Data',
             'Receive Commands', 'Actuator Control', 'Loop']
    for step in steps:
        dot.node(step, step)
    edges = [
        ('Start','Connect Wi-Fi'), ('Connect Wi-Fi','MQTT Init'),
        ('MQTT Init','Read Sensors'), ('Read Sensors','Publish Data'),
        ('Publish Data','Receive Commands'), ('Receive Commands','Actuator Control'),
        ('Actuator Control','Loop'), ('Loop','Read Sensors')
    ]
    for src,dst in edges:
        dot.edge(src, dst)
    return dot.pipe().decode('utf-8')


def build_dashboard():
    """
    Returns SVG string of a mock dashboard.
    """
    dash = graphviz.Digraph(format='svg')
    dash.attr(rankdir='LR')
    # sample nodes
    dash.node('Temp', '🌡 25°C')
    dash.node('Motion', '👀 No motion')
    dash.node('Light', '💡 Off')
    dash.node('Relay', '🔌 On')
    dash.edges([('Temp','Motion'), ('Motion','Light'), ('Light','Relay')])
    return dash.pipe().decode('utf-8')