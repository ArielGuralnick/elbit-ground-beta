from flask import send_file

async def pdf_safrot_mafil_Handler(request):
    if request.method == 'GET':
        static_file =  open('elbit-ground-beta/app/pdf_files/skyLark/safrot_mafil.pdf', 'rb')
        return send_file(static_file, attachment_filename='safrot_mafil.pdf')