var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

/* CSS below directly from stripe.com */
var card = elements.create('card', {
    style: {
      base: {
        iconColor: '#c4f0ff',
        color: '#fff',
        fontWeight: '500',
        fontFamily: 'Roboto, Open Sans, Segoe UI, sans-serif',
        fontSize: '16px',
        fontSmoothing: 'antialiased',
        ':-webkit-autofill': {
          color: '#fce883',
        },
        '::placeholder': {
          color: '#87BBFD',
        },
      },
      invalid: {
        iconColor: '#FFC7EE',
        color: '#FFC7EE',
      },
    },
  });

card.mount('#card-element');

// Handle realtime validation errors on card element
card.addEventListener('change', function(event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html =
            `<span>${event.error.message}</span>`
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
    }
)

// Handle form submit event

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
  ev.preventDefault(); // Prevent POST 
  card.update({'disabled': true});
  $('#submit-button').attr('disabled', true);
  stripe.confirmCardPayment(clientSecret, {
    payment_method: {
      card: card,
    }
  }).then(function(result) {
    if (result.error) {
        var errorDiv = document.getElementById('card-errors');
        var html =
          `<span>${result.error.message}</span>`;
        $(errorDiv).html(html);
        card.update({'disabled': false});
        $('#submit-button').attr('disabled', false);
    } else {
      if (result.paymentIntent.status === 'succeeded') {  
        form.submit();
      }
    }
})
});