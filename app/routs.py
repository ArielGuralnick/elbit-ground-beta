from app import app # importing app variable from app package
from flask import render_template,request

from src.handlers.user_Handler import user_Handler
from src.handlers.skyLark_instructor_Handler import skyLark_instructor_Handler
from src.handlers.skyLark_technician_Handler import skyLark_technician_Handler
from src.handlers.skyLark_mafil_Handler import skyLark_mafil_Handler
from src.handlers.literature_Handler import literature_Handler
from src.handlers.order_training_Handler import order_training_Handler
from src.handlers.show_static_pdf_safrot_mafil_Handler import show_static_pdf_safrot_mafil_Handler
from src.handlers.show_static_pdf_safrot_simulator_Handler import show_static_pdf_safrot_simulator_Handler
from src.handlers.show_static_pdf_solutions_Handler import show_static_pdf_solutions_Handler
from src.handlers.show_data_errors_technician_Handler import show_data_errors_technician_Handler
from src.handlers.show_data_errors_mafil_Handler import show_data_errors_mafil_Handler
from src.handlers.show_data_activity_Handler import show_data_activity_Handler
from src.handlers.feedback_Handler import feedback_Handler
from src.handlers.activity_Handler import activity_Handler
from src.handlers.insert_error_Handler import insert_error_Handler
from src.handlers.warehouse_inventory_Handler import warehouse_inventory_Handler
from src.handlers.maintenance_technician_mafil_Handler import maintenance_technician_mafil_Handler

from src.handlers.mars_Handler import mars_Handler
from src.handlers.moreshet_Handler import moreshet_Handler


@app.route("/", methods=['GET','POST'])
def home():
    return render_template("home.html")

@app.route("/user", methods=['GET'])
async def user():
    return await user_Handler(request)

@app.route("/skyLark_instructor", methods=['GET','POST'])
async def skyLark_instructor():
    return await skyLark_instructor_Handler(request)

@app.route("/skyLark_technician", methods=['GET','POST'])
async def skyLark_technician():
    return await skyLark_technician_Handler(request)

@app.route("/skyLark_mafil", methods=['GET','POST'])
async def skyLark_mafil():
    return await skyLark_mafil_Handler(request)

@app.route("/literature", methods=['GET'])
async def literature():
    return await literature_Handler(request)

@app.route("/order_training", methods=['GET'])
async def order_training():
    return await order_training_Handler(request)

@app.route('/user/skyLark_mafil/show-static-pdf-safrot_mafil')
async def show_static_pdf_safrot_mafil():
    return await show_static_pdf_safrot_mafil_Handler(request)


@app.route('/user/skyLark_mafil/show-static-pdf-safrot_simulator')
async def show_static_pdf_safrot_simulator():
    return await show_static_pdf_safrot_simulator_Handler(request)

@app.route('/show_data_errors_mafil')
async def show_data_errors_mafil():
    return await show_data_errors_mafil_Handler(request)


@app.route('/user/skyLark_instructor/show-static-pdf-solutions')
async def show_static_pdf_solutions():
    return await show_static_pdf_solutions_Handler(request)


@app.route('/show_data_errors_technician', methods=['GET','POST'])
async def show_data_errors_technician():
    return await show_data_errors_technician_Handler(request)


@app.route('/show_data_activity', methods=['GET','POST'])
async def show_data_activity():
    return await show_data_activity_Handler(request)
    
@app.route("/feedback", methods=['GET','POST'])
async def feedback():
    return await feedback_Handler(request)
   

@app.route("/activity", methods=['GET','POST'])
async def activity():
    return await activity_Handler(request)


@app.route("/insert_error", methods=['GET','POST'])
async def insert_error():
    return await insert_error_Handler(request)


@app.route("/warehouse_inventory", methods=['GET','POST'])
async def warehouse_inventory():
    return await warehouse_inventory_Handler(request)


@app.route("/maintenance_technician_mafil", methods=['GET','POST'])
async def maintenance_technician_mafil():
    return await maintenance_technician_mafil_Handler(request)

@app.route("/mars", methods=['GET','POST'])
async def mars():
    return await mars_Handler(request)

@app.route("/moreshet", methods=['GET','POST'])
async def moreshet():
    return await moreshet_Handler(request)