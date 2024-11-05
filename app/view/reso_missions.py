from flask_restful import Resource, reqparse
from flask import jsonify
from app.models.missions import Missions
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError

# Adicionar
argumentos = reqparse.RequestParser()
argumentos.add_argument('name', type=str, required=True, help="Name cannot be blank!")
argumentos.add_argument("date", type=str, required=True, help="Date cannot be blank!")
argumentos.add_argument("destination", type=str, required=True, help="Destination cannot be blank!")
argumentos.add_argument("crew", type=str, required=True, help="Crew cannot be blank!")
argumentos.add_argument("payload", type=str, required=True, help="Payload cannot be blank!")
argumentos.add_argument("status", type=str, required = True, help="Status cannot be blank!")
argumentos.add_argument("info", type=str,required = True, help="Info cannot be blank!" )
argumentos.add_argument("duration", type=str, required = True, help="Duration cannot be blank!")
argumentos.add_argument("cost", type=float, required = True, help="Cost cannot be blank!" )



# Atualizar
argumentos_update = reqparse.RequestParser()
argumentos_update.add_argument('id', type=int)
argumentos_update.add_argument("name", type=str)
argumentos_update.add_argument("date", type=str)
argumentos_update.add_argument("destination", type=str)
argumentos_update.add_argument("crew", type=str)
argumentos_update.add_argument("payload", type=str)
argumentos_update.add_argument("status", type=str)
argumentos_update.add_argument("info", type=str)
argumentos_update.add_argument("duration", type=str)
argumentos_update.add_argument("cost", type=float)

# Deletar
argumentos_delete = reqparse.RequestParser()
argumentos_delete.add_argument('id', type=int)

args = reqparse.RequestParser()
args.add_argument('id', type=int)

class MissionById(Resource):
    def get(self):
        try:
            datas = args.parse_args()
            missions = Missions.list_id(self, datas['id'])
            if missions:
                return missions 
            else:
                return {'message': f'Mission with ID {datas['id']} not found'}, 404
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500
        
class MissionList(Resource):
    def get(self):
        try:
            missions = Missions.list_all(self)
            if missions:
                return missions
            else:
                return jsonify({'message': 'no mission found.'}), 404
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500
        
class MissionByDate(Resource):
    argumentos.add_argument('start_date', type=str, required=True, help="start_date cannot be blank!")
    argumentos.add_argument('end_date', type=str, required=True, help="start_date cannot be blank!")
    def get(self):
        try:  
            datas = args.parse_args()
            start_date = datas['start_date']
            end_date = datas['end_date']
            missions = Missions.list_by_date_range(self, start_date, end_date)
            if missions:
                return missions
            else:
                return jsonify({'message': 'no mission found'}), 404
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500

class MissionDelete(Resource):
    def delete(self):
        try:
            datas = argumentos_delete.parse_args()
            Missions.delete_missions(self, datas['id'])
            return {"message": 'Mission deleted successfully!'}, 200
        except Exception as e:  
            return jsonify({'status': 500, 'msg': f'{e}'}), 500

class MissionUpdate(Resource):
    def put(self):
        try:
            datas = argumentos_update.parse_args()
            Missions.update_missions(self, datas['id'], datas['name'],
                                     datas['date'], datas['destination'],
                                     datas['crew'], datas['payload'],
                                     datas['status'], datas['info'],
                                     datas['duration'], datas['cost'])
            return {'message': 'Product updated successfully!'}
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500

class MissionCreate(Resource):
    def post(self):
        try:
            datas = argumentos.parse_args()
            Missions.save_missions(self, datas['name'],
                                         datas['date'], datas['destination'],
                                         datas['crew'], datas['payload'],
                                         datas['status'], datas['info'],
                                         datas['duration'], datas['cost'])
            return {'message': 'Mission create successfully!'}, 200
        except Exception as e:
            return jsonify({'status':500,'msg':f'{e}'}), 500

class Index(Resource):
    def get(self):
        return jsonify("Sistema de Gerenciamento de Expedição Espacial")
    
