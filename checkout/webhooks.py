from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWebhook_Handler

import stripe


@require_POST
@csrf_exempt
def webhook(request):
    """Listen for webhooks from stripe"""

    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get webhook data and verify signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret)
    except ValueError:
        # Invalid payload error
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        # Invalid signature error
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    print('Success')
    # return HttpResponse(status=200)

    handler = StripeWebhook_Handler(request)

    # Map webhook events to handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed':
            handler.handle_payment_intent_payment_failed,
    }

    # Get webhook type
    event_type = event['type']

    # Get handler from event_map or use default.
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call event handler with event
    response = event_handler(event)
    return response
