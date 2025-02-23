from microservicio__procesarventa import create_app
from flask_restful import Resource,Api
from flask import Flask, request, jsonify
import requests

app = create_app()
app_context = app.app_context()
app_context.push()

api = Api(app)

class VistaProcesarVenta(Resource):
    @app.route('/procesar_venta', methods=['POST'])
    def registrar_venta():

        data = request.get_json()
        
        if 'cantidades' not in data or 'precios' not in data:
            return jsonify({'error': 'Faltan parámetros: cantidades y precios son requeridos.'}), 400
        
        cantidades = data['cantidades']
        precios = data['precios']
        
        if len(cantidades) != len(precios):
            return jsonify({'error': 'Las listas de cantidades y precios deben tener el mismo tamaño.'}), 400
        
        total_venta = sum(cantidad * precio for cantidad, precio in zip(cantidades, precios))
        
        return jsonify({'total_venta': total_venta}), 200
    
    


