from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db' 
api = Api(app)
db = SQLAlchemy(app)

from app.models.missions import Missions
with app.app_context(): 
    db.create_all()

from app.view.reso_missions import Index,MissionCreate, MissionUpdate, MissionDelete,MissionById, MissionList, MissionByDate
api.add_resource(Index, "/")
api.add_resource(MissionCreate, "/create")
api.add_resource(MissionUpdate, "/update")
api.add_resource(MissionDelete, "/delete")
api.add_resource(MissionList, '/missions')
api.add_resource(MissionById, '/missions/search')
api.add_resource(MissionByDate, '/missions/date_range')


'''@app.route("/index")

def index():
    #return "<h1> Minha Aplicação em Flask </h1>"
    return render_template("index.html")'''
