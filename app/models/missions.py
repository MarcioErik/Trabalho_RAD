from datetime import datetime
from app import db
from sqlalchemy.dialects.postgresql import JSON

class Missions(db.Model):
    __tablename__ = 'missions'
    __table_args__ = {'sqlite_autoincrement': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date, nullable=False)
    destination = db.Column(db.String(255), nullable=False)
    crew = db.Column(db.String, nullable=False)
    payload = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    info = db.Column(db.String, nullable=False)
    duration = db.Column(db.String, nullable=False)
    cost = db.Column(db.Numeric(precision=10, scale=2), nullable=False)

    def __init__(self, name, date, crew, destination, payload, status, info, duration, cost):
        self.name = name
        self.date = date
        self.crew = crew
        self.destination = destination
        self.payload = payload
        self.status = status
        self.info = info
        self.duration = duration
        self.cost = cost
        
    def save_missions(self, name, date, destination, crew, payload, status, info, duration, cost):
        try:
            date = datetime.strptime(date,'%Y-%m-%d').date()
            add_banco = Missions(name, date, crew, destination, payload, status, info, duration, cost)
            db.session.add(add_banco)
            db.session.commit()
            
        except Exception as e:
            print(f"Error in save_missions: {e}")
 
    def list_id(self, mission_id):
        try: 
            missions = db.session.query(Missions).filter(Missions.id == mission_id).all()
            missions_dict = [{'id': mission.id,
                              'name': mission.name,
                              'date': mission.date.strftime('%Y-%m-%d'),
                              'crew': mission.crew,
                              'destination': mission.destination,
                              'payload': mission.payload,
                              'status': mission.status,
                              'info': mission.info,
                              'duration': mission.duration,
                              'cost': float(mission.cost)}
                               for mission in missions]
            return missions_dict
        except Exception as e:
            print(e)
    
    def list_all(self):
        try:
            missions = db.session.query(Missions).order_by(Missions.date.desc()).all()
            missions_dict = [{'id': mission.id, 
                              'name': mission.name,
                              'date': mission.date.strftime('%Y-%m-%d'),
                              'destination': mission.destination,
                              'crew': mission.crew,
                              'payload': mission.payload,
                              'status': mission.status,
                              'info': mission.info,
                              'duration': mission.duration,
                              'cost': float(mission.cost)}
                              for mission in missions]
            return missions_dict
        except Exception as e:
            print(e)
        
    def list_by_date_range(self, start_date, end_date):
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date,'%Y-%m-%d').date()
            missions = db.session.query(Missions).filter(Missions.date.between(start_date, end_date)).all()
            missions_list = [{'id': mission.id, 'name': mission.name,
                              'date': mission.date.strftime('%Y,%m,%d'),
                              'destination': mission.destination,
                              'crew': mission.crew, 'payload': mission.payload,
                              'status': mission.status, 'info': mission.info,
                              'duration': mission.duration, 'cost': float(mission.cost)}
                               for mission in missions]
            return missions_list
        except Exception as e:
            print(e)
           
    def update_missions(self, id, name, date, destination, crew, payload, status, info, duration, cost):
        try:
            mission_date = datetime.strptime(date, '%Y-%m-%d').date()
            db.session.query(Missions).filter(Missions.id == id).update({
                "name": name,
                "date": mission_date,
                "destination": destination,
                "crew": crew,
                "payload": payload,
                'status': status,
                'info': info,
                'duration': duration,
                'cost': cost
            })
            db.session.commit()
        except Exception as e:
            print(f"Error in update_missions: {e}")

    def delete_missions(self, id):
        try:
            db.session.query(Missions).filter(Missions.id == id).delete()
            db.session.commit()
        except Exception as e:
            print(f"Erro ao excluir missão: {e}")