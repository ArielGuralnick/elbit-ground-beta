import os
from unicodedata import name
from app import app # importing app variable from app package


from src.handlers.skyLark.skyLark_Handler import skyLark_Handler
from src.handlers.skyLark.skyLark_instructor_Handler import skyLark_instructor_Handler
from src.handlers.skyLark.skyLark_technician_Handler import skyLark_technician_Handler
from src.handlers.skyLark.skyLark_mafil_Handler import skyLark_mafil_Handler
from src.handlers.skyLark.literature_Handler import literature_Handler
from src.handlers.order_training_Handler import order_training_Handler
from src.handlers.skyLark.pdf.pdf_safrot_mafil_Handler import pdf_safrot_mafil_Handler
from src.handlers.skyLark.pdf.pdf_safrot_simulator_Handler import pdf_safrot_simulator_Handler
from src.handlers.skyLark.pdf.skyLark_pdf_solutions_Handler import skyLark_pdf_solutions_Handler
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
from src.handlers.skyLark.edit.edit_maintenance_tecnician_mafil_Handler import edit_maintenance_technician_mafil_Handler
from src.handlers.skyLark.training_package_Handler import training_package_Handler


from src.handlers.manager.manager_Handler import manager_Handler
from src.handlers.manager.manager_choose_training_simulator_Handler import manager_choose_training_simulator_Handler
from src.handlers.manager.manager_feedbacks_Handler import manager_feedbacks_Handler

from src.handlers.mars.mars_Handler import mars_Handler
from src.handlers.mars.pdf.mars_pdf_solutions_Handler import mars_pdf_solutions_Handler
from src.handlers.mars.mars_instructor_Handler import mars_instructor_Handler
from src.handlers.mars.mars_technician_Handler import mars_technician_Handler
from src.handlers.mars.mars_mafil_Handler import mars_mafil_Handler
from src.handlers.mars.insert.mars_feedback_Handler import mars_feedback_Handler
from src.handlers.mars.show.mars_show_data_errors_technician_Handler import mars_show_data_errors_technician_Handler
from src.handlers.mars.show.mars_show_maintenance_technician_mafil_Handler import mars_show_maintenance_technician_mafil_Handler
from src.handlers.mars.edit.mars_edit_maintenance_technician_mafil_Handler import mars_edit_maintenance_technician_mafil_Handler
from src.handlers.mars.show.mars_show_warehouse_inventory_Handler import mars_show_warehouse_inventory_Handler
from src.handlers.mars.edit.mars_edit_warehouse_inventory_Handler import mars_edit_warehouse_inventory_Handler
from src.handlers.mars.insert.mars_insert_activity_Handler import mars_insert_activity_Handler
from src.handlers.mars.insert.mars_insert_error_Handler import mars_insert_error_Handler
from src.handlers.mars.show.mars_show_data_activity_Handler import mars_show_data_activity_Handler
from src.handlers.mars.show.mars_show_data_errors_mafil_Handler import mars_show_data_errors_mafil_Handler
from src.handlers.mars.edit.mars_edit_data_errors_mafil_Handler import mars_edit_data_errors_mafil_Handler
from src.handlers.mars.show.mars_show_work_plan_mafil_Handler import mars_show_work_plan_mafil_Handler
from src.handlers.mars.edit.mars_edit_work_plan_mafil_Handler import mars_edit_work_plan_mafil_Handler




from src.handlers.moreshet.moreshet_Handler import moreshet_Handler
from src.handlers.moreshet.pdf.moreshet_pdf_solutions_Handler import moreshet_pdf_solutions_Handler
from src.handlers.moreshet.moreshet_instructor_Handler import moreshet_instructor_Handler
from src.handlers.moreshet.moreshet_technician_Handler import moreshet_technician_Handler
from src.handlers.moreshet.moreshet_mafil_Handler import moreshet_mafil_Handler
from src.handlers.moreshet.insert.moreshet_feedback_Handler import moreshet_feedback_Handler
from src.handlers.moreshet.show.moreshet_show_maintenance_technician_mafil_Handler import moreshet_show_maintenance_technician_mafil_Handler
from src.handlers.moreshet.edit.moreshet_edit_maintenance_technician_mafil_Handler import moreshet_edit_maintenance_technician_mafil_Handler
from src.handlers.moreshet.show.moreshet_show_warehouse_inventory_Handler import moreshet_show_warehouse_inventory_Handler
from src.handlers.moreshet.edit.moreshet_edit_warehouse_inventory_Handler import moreshet_edit_warehouse_inventory_Handler
from src.handlers.moreshet.insert.moreshet_insert_error_Handler import moreshet_insert_error_Handler
from src.handlers.moreshet.insert.moreshet_insert_activity_Handler import moreshet_insert_activity_Handler
from src.handlers.moreshet.show.moreshet_show_data_activity_Handler import moreshet_show_data_activity_Handler
from src.handlers.moreshet.show.moreshet_show_work_plan_mafil_Handler import moreshet_show_work_plan_mafil_Handler
from src.handlers.moreshet.edit.moreshet_edit_work_plan_mafil_Handler import moreshet_edit_work_plan_mafil_Handler
from src.handlers.moreshet.show.moreshet_show_data_errors_technician_Handler import moreshet_show_data_errors_technician_Handler
from src.handlers.moreshet.show.moreshet_show_data_errors_mafil_Handler import moreshet_show_data_errors_mafil_Handler
from src.handlers.moreshet.edit.moreshet_edit_data_errors_mafil_Handler import moreshet_edit_data_errors_mafil_Handler



from src.handlers.driving.driving_Handler import driving_Handler
from src.handlers.driving.insert.driving_order_training_Handler import driving_order_training_Handler
from src.handlers.driving.pdf.driving_pdf_solutions_Handler import driving_pdf_solutions_Handler
from src.handlers.driving.driving_instructor_Handler import driving_instructor_Handler
from src.handlers.driving.driving_technician_Handler import driving_technician_Handler
from src.handlers.driving.driving_mafil_Handler import driving_mafil_Handler
from src.handlers.driving.insert.driving_feedback_Handler import driving_feedback_Handler
from src.handlers.driving.show.driving_show_maintenance_technician_mafil_Handler import driving_show_maintenance_technician_mafil_Handler
from src.handlers.driving.edit.driving_edit_maintenance_technician_mafil_Handler import driving_edit_maintenance_technician_mafil_Handler
from src.handlers.driving.show.driving_show_warehouse_inventory_Handler import driving_show_warehouse_inventory_Handler
from src.handlers.driving.edit.driving_edit_warehouse_inventory_Handler import driving_edit_warehouse_inventory_Handler
from src.handlers.driving.insert.driving_insert_error_Handler import driving_insert_error_Handler
from src.handlers.driving.insert.driving_insert_activity_Handler import driving_insert_activity_Handler
from src.handlers.driving.show.driving_show_data_activity_Handler import driving_show_data_activity_Handler
from src.handlers.driving.show.driving_show_data_errors_technician_Handler import driving_show_data_errors_technician_Handler
from src.handlers.driving.show.driving_show_data_errors_mafil_Handler import driving_show_data_errors_mafil_Handler
from src.handlers.driving.edit.driving_edit_data_errors_Handler import driving_edit_data_errors_Handler


from src.handlers.tzevet.tzevet_Handler import tzevet_Handler
from src.handlers.tzevet.insert.tzevet_order_training_Handler import tzevet_order_training_Handler
#from src.handlers.tzevet.pdf.tzevet_pdf_solutions_Handler import tzevet_pdf_solutions_Handler
from src.handlers.tzevet.tzevet_instructor_Handler import tzevet_instructor_Handler
from src.handlers.tzevet.tzevet_technician_Handler import tzevet_technician_Handler
from src.handlers.tzevet.tzevet_mafil_Handler import tzevet_mafil_Handler
from src.handlers.tzevet.insert.tzevet_feedback_Handler import tzevet_feedback_Handler
from src.handlers.tzevet.show.tzevet_show_maintenance_technician_mafil_Handler import tzevet_show_maintenance_technician_mafil_Handler
from src.handlers.tzevet.edit.tzevet_edit_maintenance_technician_mafil_Handler import tzevet_edit_maintenance_technician_mafil_Handler
from src.handlers.tzevet.show.tzevet_show_warehouse_inventory_Handler import tzevet_show_warehouse_inventory_Handler
from src.handlers.tzevet.edit.tzevet_edit_warehouse_inventory_Handler import tzevet_edit_warehouse_inventory_Handler
from src.handlers.tzevet.insert.tzevet_insert_error_Handler import tzevet_insert_error_Handler
from src.handlers.tzevet.insert.tzevet_insert_activity_Handler import tzevet_insert_activity_Handler
from src.handlers.tzevet.show.tzevet_show_data_activity_Handler import tzevet_show_data_activity_Handler
from src.handlers.tzevet.show.tzevet_show_data_errors_technician_Handler import tzevet_show_data_errors_technician_Handler
from src.handlers.tzevet.show.tzevet_show_data_errors_mafil_Handler import tzevet_show_data_errors_mafil_Handler
from src.handlers.tzevet.edit.tzevet_edit_data_errors_Handler import tzevet_edit_data_errors_Handler



from src.handlers.sheder.sheder_Handler import sheder_Handler
#from src.handlers.sheder.insert.sheder_order_training_Handler import sheder_order_training_Handler
#from src.handlers.sheder.pdf.sheder_pdf_solutions_Handler import sheder_pdf_solutions_Handler
#from src.handlers.sheder.sheder_instructor_Handler import sheder_instructor_Handler
from src.handlers.sheder.sheder_technician_Handler import sheder_technician_Handler
from src.handlers.sheder.sheder_mafil_Handler import sheder_mafil_Handler
#from src.handlers.sheder.insert.sheder_feedback_Handler import sheder_feedback_Handler
from src.handlers.sheder.show.sheder_show_maintenance_technician_mafil_Handler import sheder_show_maintenance_technician_mafil_Handler
from src.handlers.sheder.edit.sheder_edit_maintenance_technician_mafil_Handler import sheder_edit_maintenance_technician_mafil_Handler
from src.handlers.sheder.show.sheder_show_warehouse_inventory_Handler import sheder_show_warehouse_inventory_Handler
from src.handlers.sheder.edit.sheder_edit_warehouse_inventory_Handler import sheder_edit_warehouse_inventory_Handler
from src.handlers.sheder.insert.sheder_insert_error_Handler import sheder_insert_error_Handler
from src.handlers.sheder.insert.sheder_insert_activity_Handler import sheder_insert_activity_Handler
from src.handlers.sheder.show.sheder_show_data_activity_Handler import sheder_show_data_activity_Handler
from src.handlers.sheder.show.sheder_show_data_errors_technician_Handler import sheder_show_data_errors_technician_Handler
from src.handlers.sheder.show.sheder_show_data_errors_mafil_Handler import sheder_show_data_errors_mafil_Handler
from src.handlers.sheder.edit.sheder_edit_data_errors_Handler import sheder_edit_data_errors_Handler



from src.handlers.mini_raam.mini_raam_Handler import mini_raam_Handler
from src.handlers.mini_raam.insert.mini_raam_feedback_Handler import mini_raam_feedback_Handler
from src.handlers.mini_raam.show.mini_raam_show_data_errors_technician_Handler import mini_raam_show_data_errors_technician_Handler
from src.handlers.mini_raam.show.mini_raam_show_maintenance_technician_mafil_Handler import mini_raam_show_maintenance_technician_mafil_Handler
from src.handlers.mini_raam.edit.mini_raam_edit_maintenance_technician_mafil_Handler import mini_raam_edit_maintenance_technician_mafil_Handler
from src.handlers.mini_raam.show.mini_raam_show_warehouse_inventory_Handler import mini_raam_show_warehouse_inventory_Handler
from src.handlers.mini_raam.edit.mini_raam_edit_warehouse_inventory_Handler import mini_raam_edit_warehouse_inventory_Handler
from src.handlers.mini_raam.edit.mini_raam_edit_data_errors_Handler import mini_raam_edit_data_errors_Handler
from src.handlers.mini_raam.insert.mini_raam_insert_error_Handler import mini_raam_insert_error_Handler



from flask import Flask, request, render_template, redirect, url_for, flash
from flask_login import (LoginManager, current_user, login_required,
                            login_user, logout_user, UserMixin,
                            confirm_login, fresh_login_required)

from flask_login import AnonymousUserMixin

from app.forms import LoginForm

print("Setting login vars")



class User(UserMixin):
    def __init__(self, name, id, password, active=True):
        self.name = name
        self.id = id
        self.password = password
        self.active = active

    def is_active(self):
        return self.active




class Anonymous(AnonymousUserMixin):
    def __init__(self):
        self.username = 'Guest'


class Config(object):
    SECRET_KEY = "dOVljBuSkQ"  # yeah, not actually a secret


USERS = {
    1: User("admin", 1, "ariel"),
    2: User("sky", 2, "Integ123"),
    3: User("a", 3, "a"),
}


# USER_NAMES = dict( (u.name, u) for u in USERS.items() )
USER_NAMES = {
    USERS[1].name : USERS[1],
    USERS[2].name : USERS[2],
    USERS[3].name : USERS[3],
}





DEBUG = True


app.config.from_object(__name__)

login_manager = LoginManager()

login_manager.anonymous_user = Anonymous
login_manager.login_view = "login"
login_manager.login_message = ""
#login_manager.refresh_view = "reauth"


@login_manager.user_loader
def load_user(id):
    return USERS.get(int(id))


login_manager.setup_app(app)






@app.route('/')
@app.route('/index')
@fresh_login_required
def index():
    user_info = {
        'name':'User'
    }
    return render_template('home.html', user=user_info)


@app.route("/login", methods=["GET", "POST"])
def login():
    print("Checking login")
    inrequestForm = "username" in request.form
    isPostRequest = request.method == "POST"
    print("inrequestForm:", inrequestForm)
    print("isPostRequest:", isPostRequest)
    # form = LoginForm()
    error = None
    if request.method == 'POST':
        formUsername = request.form['username']
        if formUsername in USER_NAMES:
            user = USER_NAMES[formUsername]
            formPassword = request.form['password']
            if formPassword == user.password:
#                remember = request.form.get("remember", "no") == "yes"
                if login_user(user, remember=True):  # שיניתי מ remeber ל True
                    # flash('login successful')
                    return redirect(request.args.get("next") or url_for("index"))
                else:
                    flash("Sorry, but you could not log in.")
            else:
                print("FAILED LOGIN")
                flash("Your Username or password are incorrect, try again!")
        else:
            flash("Your Username or password are incorrect, try again!")
            print("Username is not on the list")
    return render_template('login.html', error=error)


@app.route("/reauth", methods=["GET", "POST"])
@login_required
def reauth():
    if request.method == "POST":
        confirm_login()
        flash(u"Reauthenticated.")
        return redirect(request.args.get("next") or url_for("index"))
    return render_template("reauth.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for("index"))


# מאמן רוכב שמיים

# ניתובים לבחירת משתמש, הדרכה, הפעלה ואחזקה
@app.route("/skyLark", methods=['GET'])
async def skyLark():
    return await skyLark_Handler(request)

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
async def skyLark_pdf_solutions():
    return await skyLark_pdf_solutions_Handler(request)


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

@app.route("/edit_maintenance_technician_mafil", methods=['GET','POST'])
async def edit_maintenance_technician_mafil():
    return await edit_maintenance_technician_mafil_Handler(request)



# הדפים של רעות ואייל

@app.route("/manager", methods=['GET','POST'])
async def manager():
    return await manager_Handler(request)

@app.route("/manager_choose_training_simulator", methods=['GET','POST'])
async def manager_choose_training_simulator():
    return await manager_choose_training_simulator_Handler(request) 

@app.route("/manager_feedbacks", methods=['GET','POST'])
async def manager_feedbacks():
    return await manager_feedbacks_Handler(request)    






# מאמן מרס

# מסמכי PDF
@app.route('/user/mars_instructor/pdf-solutions')
async def mars_pdf_solutions():
    return await mars_pdf_solutions_Handler(request)

# ניתובים לבחירת משתמש, הדרכה, הפעלה ואחזקה
@app.route("/mars", methods=['GET','POST'])
async def mars():
    return await mars_Handler(request)

@app.route("/mars_instructor", methods=['GET','POST'])
async def mars_instructor():
    return await mars_instructor_Handler(request)

@app.route("/mars_technician", methods=['GET','POST'])
async def mars_technician():
    return await mars_technician_Handler(request)

@app.route("/mars_mafil", methods=['GET','POST'])
async def mars_mafil():
    return await mars_mafil_Handler(request)



@app.route("/mars_feedback", methods=['GET','POST'])
async def mars_feedback():
    return await mars_feedback_Handler(request)

@app.route("/mars_show_data_activity", methods=['GET','POST'])
async def mars_show_data_activity():
    return await mars_show_data_activity_Handler(request)


# הפערים בין המפעיל לטכנאי

@app.route("/mars_show_maintenance_technician_mafil", methods=['GET','POST'])
async def mars_show_maintenance_technician_mafil():
    return await mars_show_maintenance_technician_mafil_Handler(request)

@app.route("/mars_edit_maintenance_technician_mafil", methods=['GET','POST'])
async def mars_edit_maintenance_technician_mafil():
    return await mars_edit_maintenance_technician_mafil_Handler(request)


# עריכה וצפייה מחסן מרס

@app.route("/mars_edit_warehouse_inventory", methods=['GET','POST'])
async def mars_edit_warehouse_inventory():
    return await mars_edit_warehouse_inventory_Handler(request)

@app.route("/mars_show_warehouse_inventory", methods=['GET','POST'])
async def mars_show_warehouse_inventory():
    return await mars_show_warehouse_inventory_Handler(request)


# הכנסת תקלה ופעילות

@app.route("/mars_insert_activity", methods=['GET','POST'])
async def mars_insert_activity():
    return await mars_insert_activity_Handler(request)

@app.route("/mars_insert_error", methods=['GET','POST'])
async def mars_insert_error():
    return await mars_insert_error_Handler(request)



# צפייה בתקלות טכנאי וצפייה ועריכה תקלות מפעיל

@app.route("/mars_show_data_errors_mafil", methods=['GET','POST'])
async def mars_show_data_errors_mafil():
    return await mars_show_data_errors_mafil_Handler(request)

@app.route("/mars_edit_data_errors_mafil", methods=['GET','POST'])
async def mars_edit_data_errors_mafil():
    return await mars_edit_data_errors_mafil_Handler(request)

@app.route("/mars_show_data_errors_technician", methods=['GET','POST'])
async def mars_show_data_errors_technician():
    return await mars_show_data_errors_technician_Handler(request)


# צפיה ועריכה תוכנית שנתית מרס

@app.route("/mars_show_work_plan_mafil", methods=['GET','POST'])
async def mars_show_work_plan_mafil():
    return await mars_show_work_plan_mafil_Handler(request)

@app.route("/mars_edit_work_plan_mafil", methods=['GET','POST'])
async def mars_edit_work_plan_mafil():
    return await mars_edit_work_plan_mafil_Handler(request)





# מאמן מורשת

# מסמכי PDF
@app.route('/user/moreshet_instructor/pdf-solutions')
async def moreshet_pdf_solutions():
    return await moreshet_pdf_solutions_Handler(request)

# ניתובים לבחירת משתמש, הדרכה, הפעלה ואחזקה
@app.route("/moreshet", methods=['GET','POST'])
async def moreshet():
    return await moreshet_Handler(request)

@app.route("/moreshet_instructor", methods=['GET','POST'])
async def moreshet_instructor():
    return await moreshet_instructor_Handler(request)

@app.route("/moreshet_technician", methods=['GET','POST'])
async def moreshet_technician():
    return await moreshet_technician_Handler(request)

@app.route("/moreshet_mafil", methods=['GET','POST'])
async def moreshet_mafil():
    return await moreshet_mafil_Handler(request)



@app.route("/moreshet_feedback", methods=['GET','POST'])
async def moreshet_feedback():
    return await moreshet_feedback_Handler(request)

@app.route("/moreshet_show_data_activity", methods=['GET','POST'])
async def moreshet_show_data_activity():
    return await moreshet_show_data_activity_Handler(request)

# הפערים בין המפעיל לטכנאי

@app.route("/moreshet_show_maintenance_technician_mafil", methods=['GET','POST'])
async def moreshet_show_maintenance_technician_mafil():
    return await moreshet_show_maintenance_technician_mafil_Handler(request)

@app.route("/moreshet_edit_maintenance_technician_mafil", methods=['GET','POST'])
async def moreshet_edit_maintenance_technician_mafil():
    return await moreshet_edit_maintenance_technician_mafil_Handler(request)


# עריכה וצפייה מחסן מורשת 

@app.route("/moreshet_edit_warehouse_inventory", methods=['GET','POST'])
async def moreshet_edit_warehouse_inventory():
    return await moreshet_edit_warehouse_inventory_Handler(request)

@app.route("/moreshet_show_warehouse_inventory", methods=['GET','POST'])
async def moreshet_show_warehouse_inventory():
    return await moreshet_show_warehouse_inventory_Handler(request)


# הכנסה תקלה ופעילות

@app.route("/moreshet_insert_error", methods=['GET','POST'])
async def moreshet_insert_error():
    return await moreshet_insert_error_Handler(request)

@app.route("/moreshet_insert_activity", methods=['GET','POST'])
async def moreshet_insert_activity():
    return await moreshet_insert_activity_Handler(request)


# צפייה ועריכה תוכנית שנתית מורשת

@app.route("/moreshet_show_work_plan_mafil", methods=['GET','POST'])
async def moreshet_show_work_plan_mafil():
    return await moreshet_show_work_plan_mafil_Handler(request)

@app.route("/moreshet_edit_work_plan_mafil", methods=['GET','POST'])
async def moreshet_edit_work_plan_mafil():
    return await moreshet_edit_work_plan_mafil_Handler(request)


# צפייה בתקלות טכנאי וצפייה ועריכה תקלות מפעיל

@app.route("/moreshet_show_data_errors_mafil", methods=['GET','POST'])
async def moreshet_show_data_errors_mafil():
    return await moreshet_show_data_errors_mafil_Handler(request)

@app.route("/moreshet_show_data_errors_technician", methods=['GET','POST'])
async def moreshet_show_data_errors_technician():
    return await moreshet_show_data_errors_technician_Handler(request)

@app.route("/moreshet_edit_data_errors_mafil", methods=['GET','POST'])
async def moreshet_edit_data_errors_mafil():
    return await moreshet_edit_data_errors_mafil_Handler(request)





# מאמני נהיגה

# הזמנת ימי אימון נהיגה
@app.route('/driving_order_training', methods=['GET','POST'])
async def driving_order_training():
    return await driving_order_training_Handler(request)

# מסמכי PDF
@app.route('/user/driving_instructor/pdf-solutions')
async def driving_pdf_solutions():
    return await driving_pdf_solutions_Handler(request)

# ניתובים לבחירת משתמש, הדרכה, הפעלה ואחזקה
@app.route("/driving", methods=['GET','POST'])
async def driving():
    return await driving_Handler(request)

@app.route("/driving_instructor", methods=['GET','POST'])
async def driving_instructor():
    return await driving_instructor_Handler(request)

@app.route("/driving_technician", methods=['GET','POST'])
async def driving_technician():
    return await driving_technician_Handler(request)

@app.route("/driving_mafil", methods=['GET','POST'])
async def driving_mafil():
    return await driving_mafil_Handler(request)




@app.route("/driving_feedback", methods=['GET','POST'])
async def driving_feedback():
    return await driving_feedback_Handler(request)

@app.route("/driving_show_data_activity", methods=['GET','POST'])
async def driving_show_data_activity():
    return await driving_show_data_activity_Handler(request)

# הפערים בין המפעיל לטכנאי

@app.route("/driving_show_maintenance_technician_mafil", methods=['GET','POST'])
async def driving_show_maintenance_technician_mafil():
    return await driving_show_maintenance_technician_mafil_Handler(request)

@app.route("/driving_edit_maintenance_technician_mafil", methods=['GET','POST'])
async def driving_edit_maintenance_technician_mafil():
    return await driving_edit_maintenance_technician_mafil_Handler(request)


# עריכה וצפייה מחסן נהיגה 

@app.route("/driving_edit_warehouse_inventory", methods=['GET','POST'])
async def driving_edit_warehouse_inventory():
    return await driving_edit_warehouse_inventory_Handler(request)

@app.route("/driving_show_warehouse_inventory", methods=['GET','POST'])
async def driving_show_warehouse_inventory():
    return await driving_show_warehouse_inventory_Handler(request)


# הכנסה תקלה ופעילות

@app.route("/driving_insert_error", methods=['GET','POST'])
async def driving_insert_error():
    return await driving_insert_error_Handler(request)

@app.route("/driving_insert_activity", methods=['GET','POST'])
async def driving_insert_activity():
    return await driving_insert_activity_Handler(request)



# צפייה בתקלות טכנאי וצפייה ועריכה תקלות מפעיל

@app.route("/driving_show_data_errors_mafil", methods=['GET','POST'])
async def driving_show_data_errors_mafil():
    return await driving_show_data_errors_mafil_Handler(request)

@app.route("/driving_show_data_errors_technician", methods=['GET','POST'])
async def driving_show_data_errors_technician():
    return await driving_show_data_errors_technician_Handler(request)

@app.route("/driving_edit_data_errors", methods=['GET','POST'])
async def driving_edit_data_errors():
    return await driving_edit_data_errors_Handler(request)




# מאמני צוות

# הזמנת ימי אימון צוות
@app.route('/tzevet_order_training', methods=['GET','POST'])
async def tzevet_order_training():
    return await tzevet_order_training_Handler(request)

# מסמכי PDF
#@app.route('/user/tzevet_instructor/pdf-solutions')
#async def tzevet_pdf_solutions():
#    return await tzevet_pdf_solutions_Handler(request)

# ניתובים לבחירת משתמש, הדרכה, הפעלה ואחזקה
@app.route("/tzevet", methods=['GET','POST'])
async def tzevet():
    return await tzevet_Handler(request)

@app.route("/tzevet_instructor", methods=['GET','POST'])
async def tzevet_instructor():
    return await tzevet_instructor_Handler(request)

@app.route("/tzevet_technician", methods=['GET','POST'])
async def tzevet_technician():
    return await tzevet_technician_Handler(request)

@app.route("/tzevet_mafil", methods=['GET','POST'])
async def tzevet_mafil():
    return await tzevet_mafil_Handler(request)




@app.route("/tzevet_feedback", methods=['GET','POST'])
async def tzevet_feedback():
    return await tzevet_feedback_Handler(request)

@app.route("/tzevet_show_data_activity", methods=['GET','POST'])
async def tzevet_show_data_activity():
    return await tzevet_show_data_activity_Handler(request)

# הפערים בין המפעיל לטכנאי

@app.route("/tzevet_show_maintenance_technician_mafil", methods=['GET','POST'])
async def tzevet_show_maintenance_technician_mafil():
    return await tzevet_show_maintenance_technician_mafil_Handler(request)

@app.route("/tzevet_edit_maintenance_technician_mafil", methods=['GET','POST'])
async def tzevet_edit_maintenance_technician_mafil():
    return await tzevet_edit_maintenance_technician_mafil_Handler(request)


# עריכה וצפייה מחסן נהיגה 

@app.route("/tzevet_edit_warehouse_inventory", methods=['GET','POST'])
async def tzevet_edit_warehouse_inventory():
    return await tzevet_edit_warehouse_inventory_Handler(request)

@app.route("/tzevet_show_warehouse_inventory", methods=['GET','POST'])
async def tzevet_show_warehouse_inventory():
    return await tzevet_show_warehouse_inventory_Handler(request)


# הכנסה תקלה ופעילות

@app.route("/tzevet_insert_error", methods=['GET','POST'])
async def tzevet_insert_error():
    return await tzevet_insert_error_Handler(request)

@app.route("/tzevet_insert_activity", methods=['GET','POST'])
async def tzevet_insert_activity():
    return await tzevet_insert_activity_Handler(request)



# צפייה בתקלות טכנאי וצפייה ועריכה תקלות מפעיל

@app.route("/tzevet_show_data_errors_mafil", methods=['GET','POST'])
async def tzevet_show_data_errors_mafil():
    return await tzevet_show_data_errors_mafil_Handler(request)

@app.route("/tzevet_show_data_errors_technician", methods=['GET','POST'])
async def tzevet_show_data_errors_technician():
    return await tzevet_show_data_errors_technician_Handler(request)

@app.route("/tzevet_edit_data_errors", methods=['GET','POST'])
async def tzevet_edit_data_errors():
    return await tzevet_edit_data_errors_Handler(request)





# מאמן שדר חם 


# ניתובים לבחירת משתמש, הדרכה, הפעלה ואחזקה
@app.route("/sheder", methods=['GET','POST'])
async def sheder():
    return await sheder_Handler(request)


@app.route("/sheder_technician", methods=['GET','POST'])
async def sheder_technician():
    return await sheder_technician_Handler(request)

@app.route("/sheder_mafil", methods=['GET','POST'])
async def sheder_mafil():
    return await sheder_mafil_Handler(request)





@app.route("/sheder_show_data_activity", methods=['GET','POST'])
async def sheder_show_data_activity():
    return await sheder_show_data_activity_Handler(request)

# הפערים בין המפעיל לטכנאי

@app.route("/sheder_show_maintenance_technician_mafil", methods=['GET','POST'])
async def sheder_show_maintenance_technician_mafil():
    return await sheder_show_maintenance_technician_mafil_Handler(request)

@app.route("/sheder_edit_maintenance_technician_mafil", methods=['GET','POST'])
async def sheder_edit_maintenance_technician_mafil():
    return await sheder_edit_maintenance_technician_mafil_Handler(request)


# עריכה וצפייה מחסן נהיגה 

@app.route("/sheder_edit_warehouse_inventory", methods=['GET','POST'])
async def sheder_edit_warehouse_inventory():
    return await sheder_edit_warehouse_inventory_Handler(request)

@app.route("/sheder_show_warehouse_inventory", methods=['GET','POST'])
async def sheder_show_warehouse_inventory():
    return await sheder_show_warehouse_inventory_Handler(request)


# הכנסה תקלה ופעילות

@app.route("/sheder_insert_error", methods=['GET','POST'])
async def sheder_insert_error():
    return await sheder_insert_error_Handler(request)

@app.route("/sheder_insert_activity", methods=['GET','POST'])
async def sheder_insert_activity():
    return await sheder_insert_activity_Handler(request)



# צפייה בתקלות טכנאי וצפייה ועריכה תקלות מפעיל

@app.route("/sheder_show_data_errors_mafil", methods=['GET','POST'])
async def sheder_show_data_errors_mafil():
    return await sheder_show_data_errors_mafil_Handler(request)

@app.route("/sheder_show_data_errors_technician", methods=['GET','POST'])
async def sheder_show_data_errors_technician():
    return await sheder_show_data_errors_technician_Handler(request)

@app.route("/sheder_edit_data_errors", methods=['GET','POST'])
async def sheder_edit_data_errors():
    return await sheder_edit_data_errors_Handler(request)





# מאמן מיני רעם


@app.route("/mini_raam", methods=['GET','POST'])
async def mini_raam():
    return await mini_raam_Handler(request)


@app.route("/mini_raam_feedback", methods=['GET','POST'])
async def mini_raam_feedback():
    return await mini_raam_feedback_Handler(request)


# הפערים בין המפעיל לטכנאי

@app.route("/mini_raam_show_maintenance_technician_mafil", methods=['GET','POST'])
async def mini_raam_show_maintenance_technician_mafil():
    return await mini_raam_show_maintenance_technician_mafil_Handler(request)

@app.route("/mini_raam_edit_maintenance_technician_mafil", methods=['GET','POST'])
async def mini_raam_edit_maintenance_technician_mafil():
    return await mini_raam_edit_maintenance_technician_mafil_Handler(request)


# עריכה וצפייה מחסן מרס

@app.route("/mini_raam_edit_warehouse_inventory", methods=['GET','POST'])
async def mini_raam_edit_warehouse_inventory():
    return await mini_raam_edit_warehouse_inventory_Handler(request)

@app.route("/mini_raam_show_warehouse_inventory", methods=['GET','POST'])
async def mini_raam_show_warehouse_inventory():
    return await mini_raam_show_warehouse_inventory_Handler(request)


# הכנסת תקלה

@app.route("/mini_raam_insert_error", methods=['GET','POST'])
async def mini_raam_insert_error():
    return await mini_raam_insert_error_Handler(request)


# צפייה בתקלות טכנאי וצפייה ועריכה תקלות מפעיל

@app.route("/mini_raam_edit_data_errors", methods=['GET','POST'])
async def mini_raam_edit_data_errors():
    return await mini_raam_edit_data_errors_Handler(request)

@app.route("/mini_raam_show_data_errors_technician", methods=['GET','POST'])
async def mini_raam_show_data_errors_technician():
    return await mini_raam_show_data_errors_technician_Handler(request)
