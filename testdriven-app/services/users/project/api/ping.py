from flask import Blueprint
from flask_restx import Resource, Api
import osmnx as ox


ping_blueprint = Blueprint('ping', __name__)
api = Api(ping_blueprint)


class Ping(Resource):
    def get(self):
        G = ox.graph_from_place('Lutsk, Volyn, Ukraine', network_type='drive')
        G_proj = ox.project_graph(G)
        nodes_proj = ox.graph_to_gdfs(G_proj, edges=False)
        graph_area_m = nodes_proj.unary_union.convex_hull.area
        return {
            'status': 'success',
            'message': 'pong!',
            'message_my': 'Nice to meet you! Is my Docker',
            'ox.__version__': ox.__version__,
            'graph_area_m': graph_area_m
        }


api.add_resource(Ping, '/ping')
