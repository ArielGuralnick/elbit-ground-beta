from flask import send_file

async def show_static_pdf_safrot_mafil_Handler(request):
    if request.method == 'GET':
        static_file =  open('elbit-ground-beta/app/safrot_mafil.pdf', 'rb')
        return send_file(static_file, attachment_filename='safrot_mafil.pdf')