# # from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render
# from django.http import HttpResponse
# from .forms import MessageForm
# import pywhatkit as kit

# def send_whatsapp_message(request):
#     if request.method == 'POST':
#         form = MessageForm(request.POST)
#         if form.is_valid():
#             phone_number = form.cleaned_data['phone_number']
#             message = form.cleaned_data['message']
            
#             # Automatically add +91 to the phone number
#             recipient_number = "+91" + phone_number

#             try:
#                 # Send the message instantly
#                 kit.sendwhatmsg_instantly(recipient_number, message)
#                 return HttpResponse("Message sent successfully!")
#             except Exception as e:
#                 return HttpResponse(f"An error occurred: {e}")
#     else:
#         form = MessageForm()

#     return render(request, 'sendmessage/send_message.html', {'form': form})


from django.shortcuts import render
from django.http import HttpResponse
from .forms import MessageForm
import pywhatkit as kit

def send_whatsapp_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            phone_numbers_raw = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            
            # Split by comma and clean up spaces
            phone_numbers = [num.strip() for num in phone_numbers_raw.split(',') if num.strip()]
            errors = []

            for number in phone_numbers:
                recipient_number = "+91" + number  # You can customize this as needed
                
                try:
                    # Send message instantly to each number
                    kit.sendwhatmsg_instantly(recipient_number, message)
                except Exception as e:
                    errors.append(f"Failed to send to {recipient_number}: {e}")
            
            if errors:
                return HttpResponse(f"Some messages failed:<br>" + "<br>".join(errors))
            else:
                return HttpResponse("Messages sent successfully to all numbers!")
    else:
        form = MessageForm()

    return render(request, 'sendmessage/send_message.html', {'form': form})
