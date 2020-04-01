from django.shortcuts import redirect, render
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request,'you have already made an inquiry for this listing')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, phone=phone, email=email, message=message, user_id=user_id)

        contact.save()

        # send_mail(
        #     'Property Listing Inquiry',
        #     'There has been an inquiry for listing ' + listing + '. Check out at the admin panel for more details.',
        #     'rahulsai9152@gmail.com',
        #     [realtor_email, 'rahulsaipratap@gmail.com'],
        #     fail_silently=False
        # )

        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon.')

        return redirect('/listings/'+listing_id)