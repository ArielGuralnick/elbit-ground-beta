from flask import send_file

async def pdf_solutions_Handler(request):
    if request.method == 'GET':
        static_file =  open('elbit-ground-beta/app/solutions.pdf', 'rb')
        return send_file(static_file, attachment_filename='solutions.pdf')