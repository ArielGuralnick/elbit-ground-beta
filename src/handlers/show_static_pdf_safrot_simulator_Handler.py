from flask import send_file

async def show_static_pdf_safrot_simulator_Handler(request):
    if request.method == 'GET':
        static_file =  open('elbit-ground-beta/app/safrot_simulator.pdf', 'rb')
        return send_file(static_file, attachment_filename='safrot_simulator.pdf')