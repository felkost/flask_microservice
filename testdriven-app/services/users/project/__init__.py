import os
from flask import Flask, jsonify
import osmnx as ox

# instantiate the app
app = Flask(__name__)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)


@app.route('/users/ping', methods=['GET'])
def ping_pong():
    G = ox.graph_from_place('Kovel, Volyn, Ukraine', network_type='drive')
    G_proj = ox.project_graph(G)
    nodes_proj = ox.graph_to_gdfs(G_proj, edges=False)
    graph_area_m = nodes_proj.unary_union.convex_hull.area
    return jsonify({
        'status': 'success',
        'message': 'pong!',
        'message_my': 'Nice to meet you! Is my Docker',
        'ox.__version__': ox.__version__,
        'graph_area_m': graph_area_m
    })
