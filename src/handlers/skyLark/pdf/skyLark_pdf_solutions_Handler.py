from flask import send_file

async def skyLark_pdf_solutions_Handler(request):
    if request.method == 'GET':
        static_file =  open('elbit-ground-beta/app/pdf_files/skyLark/solutions.pdf', 'rb')
        return send_file(static_file, attachment_filename='מדריך תקלות למדריכות.pdf')