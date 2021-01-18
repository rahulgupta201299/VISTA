
#added start
from django.shortcuts import render
from django.conf import settings
from django.urls import reverse
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
#added after stripe start
from .models import Pay
from django.contrib.auth.models import User
#added after stripe end
import stripe


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from login_registeration_edit_prof.serializers import UserSerializer, GroupSerializer      
#please check the app name in ur folder structure to check the first name


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]



def index(request):
    return render(request, 'checkout/index.html')

def thanks(request):
    return render(request, 'checkout/thanks.html')

@csrf_exempt
def checkout(request):
    stripe.api_key = settings.STRIPE_PRIVATE_KEY
    print(stripe.api_key, ' = ',settings.STRIPE_PRIVATE_KEY)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1HiZ3ZFH3h9vdO8rcn152ayM',
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('thanks')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('index')),
    )
    print(session.id)
    #added after stripe start
    ssid = session.id
    pi_id = session.payment_intent
    user = User.objects.get(username = request.user.username)
    print(user)
    pay_info = Pay(ssid = ssid, pi_id = pi_id,user=user)
    pay_info.save()
    #added after stripe end
    return JsonResponse({
        'session_id' : session.id,
        'stripe_public_key' : settings.STRIPE_PUBLIC_KEY
    })
'''
@csrf_exempt
def stripe_webhook(request):

    print('WEBHOOK!')
    # You can find your endpoint's secret in your webhook settings
    endpoint_secret = 'whsec_Xj8wBk2qiUcjDEmYu5kfKkOrJCJ5UUjW'

    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print(session)
        line_items = stripe.checkout.Session.list_line_items(session['id'], limit=1)
        print(line_items)

    return HttpResponse(status=200)
'''

#added end
