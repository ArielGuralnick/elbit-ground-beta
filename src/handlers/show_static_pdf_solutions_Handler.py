from flask import send_file

async def show_static_pdf_solutions_Handler(request):
    if request.method == 'GET':
        static_file =  open('elbit-ground-beta/app/solutions.pdf', 'rb')
        return send_file(static_file, attachment_filename='solutions.pdf')