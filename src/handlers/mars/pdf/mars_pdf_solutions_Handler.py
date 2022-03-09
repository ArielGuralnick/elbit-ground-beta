from flask import send_file

async def mars_pdf_solutions_Handler(request):
    if request.method == 'GET':
        static_file =  open('app/pdf_files/mars/solutions.pdf', 'rb')
        return send_file(static_file, attachment_filename='מדריך תקלות למדריכות.pdf')