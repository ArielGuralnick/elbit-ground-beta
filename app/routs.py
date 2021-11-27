from app import app # importing app variable from app package
from flask import render_template,request

from src.handlers.skyLark.skyLark_user_Handler import skyLark_user_Handler
from src.handlers.skyLark.skyLark_instructor_Handler import skyLark_instructor_Handler
from src.handlers.skyLark.skyLark_technician_Handler import skyLark_technician_Handler
from src.handlers.skyLark.skyLark_mafil_Handler import skyLark_mafil_Handler
from src.handlers.skyLark.literature_Handler import literature_Handler
from src.handlers.skyLark.insert.order_training_Handler import order_training_Handler
from src.handlers.skyLark.pdf.pdf_safrot_mafil_Handler import pdf_safrot_mafil_Handler
from src.handlers.skyLark.pdf.pdf_safrot_simulator_Handler import pdf_safrot_simulator_Handler
from src.handlers.skyLark.pdf.pdf_solutions_Handler import pdf_solutions_Handler
from src.handlers.skyLark.show.show_data_errors_technician_Handler import show_data_errors_technician_Handler
from src.handlers.skyLark.show.show_data_errors_mafil_Handler import show_data_errors_mafil_Handler
from src.handlers.skyLark.edit.edit_data_errors_mafil_Handler import edit_data_errors_mafil_Handler
from src.handlers.skyLark.show.show_work_plan_mafil_Handler import show_work_plan_mafil_Handler
from src.handlers.skyLark.edit.edit_work_plan_mafil_Handler import edit_work_plan_mafil_Handler
from src.handlers.skyLark.show.show_data_activity_Handler import show_data_activity_Handler
from src.handlers.skyLark.insert.skyLark_feedback_Handler import skyLark_feedback_Handler
from src.handlers.skyLark.insert.insert_activity_Handler import insert_activity_Handler
from src.handlers.skyLark.insert.insert_error_Handler import insert_error_Handler
from src.handlers.skyLark.show.show_warehouse_inventory_Handler import show_warehouse_inventory_Handler
from src.handlers.skyLark.edit.edit_warehouse_inventory_Handler import edit_warehouse_inventory_Handler
from src.handlers.skyLark.show.show_maintenance_technician_mafil_Handler import show_maintenance_technician_mafil_Handler
from src.handlers.skyLark.insert.insert_maintenance_tecnician_mafil_Handler import insert_maintenance_technician_mafil_Handler
from src.handlers.skyLark.edit.edit_maintenance_tecnician_mafil_Handler import edit_maintenance_technician_mafil_Handler
from src.handlers.skyLark.training_package_Handler import training_package_Handler


from src.handlers.manager.manager_Handler import manager_Handler
from src.handlers.manager.show.show_training_days_Handler import show_training_days_Handler
from src.handlers.manager.manager_feedbacks_Handler import manager_feedbacks_Handler

from src.handlers.mars.mars_Handler import mars_Handler
from src.handlers.mars.insert.mars_insert_activity_Handler import mars_insert_activity_Handler
from src.handlers.mars.insert.mars_insert_error_Handler import mars_insert_error_Handler
from src.handlers.moreshet.moreshet_Handler import moreshet_Handler


@app.route("/", methods=['GET','POST'])
def home():
    return render_template("home.html")

@app.route("/skyLark_user", methods=['GET'])
async def skyLark_user():
    return await skyLark_user_Handler(request)

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

@app.route("/training_package", methods=['GET'])
async def training_package():
    return await training_package_Handler(request)

@app.route("/order_training", methods=['GET','POST'])
async def order_training():
    return await order_training_Handler(request)

@app.route('/user/skyLark_mafil/pdf-safrot_mafil')
async def pdf_safrot_mafil():
    return await pdf_safrot_mafil_Handler(request)


@app.route('/user/skyLark_mafil/pdf-safrot_simulator')
async def pdf_safrot_simulator():
    return await pdf_safrot_simulator_Handler(request)


# צפייה ועריכה תקלות למפעיל
@app.route('/show_data_errors_mafil', methods=['POST', 'GET'])
async def show_data_errors_mafil():
    return await show_data_errors_mafil_Handler(request)

@app.route('/edit_data_errors_mafil', methods=['POST', 'GET'])
async def edit_data_errors_mafil():
    return await edit_data_errors_mafil_Handler(request)


# תוכנית עבודה שנתית למפעיל
@app.route('/show_work_plan_mafil', methods=['POST', 'GET'])
async def show_work_plan_mafil():
    return await show_work_plan_mafil_Handler(request)

@app.route('/edit_work_plan_mafil', methods=['POST', 'GET'])
async def edit_work_plan_mafil():
    return await edit_work_plan_mafil_Handler(request)


@app.route('/user/skyLark_instructor/pdf-solutions')
async def pdf_solutions():
    return await pdf_solutions_Handler(request)


@app.route('/show_data_errors_technician', methods=['GET','POST'])
async def show_data_errors_technician():
    return await show_data_errors_technician_Handler(request)


@app.route('/show_data_activity', methods=['GET','POST'])
async def show_data_activity():
    return await show_data_activity_Handler(request)
    
@app.route("/skyLark_feedback", methods=['GET','POST'])
async def skyLark_feedback():
    return await skyLark_feedback_Handler(request)
   

@app.route("/insert_activity", methods=['GET','POST'])
async def insert_activity():
    return await insert_activity_Handler(request)


@app.route("/insert_error", methods=['GET','POST'])
async def insert_error():
    return await insert_error_Handler(request)



# צפייה ועריכה מחסן רוכש

@app.route("/edit_warehouse_inventory", methods=['GET','POST'])
async def edit_warehouse_inventory():
    return await edit_warehouse_inventory_Handler(request)

@app.route("/show_warehouse_inventory", methods=['GET','POST'])
async def show_warehouse_inventory():
    return await show_warehouse_inventory_Handler(request)


# הפערים בין המפעיל לטכנאי

@app.route("/show_maintenance_technician_mafil", methods=['GET','POST'])
async def show_maintenance_technician_mafil():
    return await show_maintenance_technician_mafil_Handler(request)

@app.route("/insert_maintenance_technician_mafil", methods=['GET','POST'])
async def insert_maintenance_technician_mafil():
    return await insert_maintenance_technician_mafil_Handler(request)

@app.route("/edit_maintenance_technician_mafil", methods=['GET','POST'])
async def edit_maintenance_technician_mafil():
    return await edit_maintenance_technician_mafil_Handler(request)



# הדפים של רעות ואייל

@app.route("/manager", methods=['GET','POST'])
async def manager():
    return await manager_Handler(request)

@app.route("/show_training_days", methods=['GET','POST'])
async def show_training_days():
    return await show_training_days_Handler(request)    

@app.route("/manager_feedbacks", methods=['GET','POST'])
async def manager_feedbacks():
    return await manager_feedbacks_Handler(request)    



# מאמן מרס

@app.route("/mars", methods=['GET','POST'])
async def mars():
    return await mars_Handler(request)

@app.route("/mars_insert_activity", methods=['GET','POST'])
async def mars_insert_activity():
    return await mars_insert_activity_Handler(request)

@app.route("/mars_insert_error", methods=['GET','POST'])
async def mars_insert_error():
    return await mars_insert_error_Handler(request)




# מאמן מורשת

async def moreshet():
    return await moreshet_Handler(request)