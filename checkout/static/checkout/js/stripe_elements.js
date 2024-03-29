var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

// CSS below directly from stripe.com
var card = elements.create('card', {
    style: {
      base: {
        iconColor: '#3c4142',
        color: '#3c4142',
        fontWeight: '500',
        fontFamily: 'Roboto, Open Sans, Segoe UI, sans-serif',
        fontSize: '16px',
        fontSmoothing: 'antialiased',
        ':-webkit-autofill': {
          color: '#3c4142',
        },
        '::placeholder': {
          color: '#87BBFD',
        },
      },
      invalid: {
        iconColor: '#dc3545',
        color: '#dc3545',
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
  $('#payment-form').fadeToggle(100);
  $('#loading-overlay').fadeToggle(100);

  var saveInfo = Boolean($('#id-save-info').attr('checked'));
  // from {% csrf_token %} in form
  var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
  var postData = {
    'csrfmiddlewaretoken': csrfToken,
    'client_secret': clientSecret,
    'save_info': saveInfo,
  };
  var url = '/checkout/cache_checkout_data/';

  $.post(url, postData).done(function(){
    stripe.confirmCardPayment(clientSecret, {
      payment_method: {
        card: card,
        billing_details: {
          name: $.trim(form.full_name.value),
          phone: $.trim(form.phone_number.value),
          email: $.trim(form.email.value),
          address: {
            line1: $.trim(form.street_address1.value),
            line2: $.trim(form.street_address2.value),
            city: $.trim(form.town_or_city.value),
            country: $.trim(form.country.value),
            state: $.trim(form.county.value),
          },
        },
      },
      shipping: {
        name: $.trim(form.full_name.value),
        phone: $.trim(form.phone_number.value),
        address: {
          line1: $.trim(form.street_address1.value),
          line2: $.trim(form.street_address2.value),
          city: $.trim(form.town_or_city.value),
          country: $.trim(form.country.value),
          postal_code: $.trim(form.postcode.value),
          state: $.trim(form.county.value),
        },       
      },
    }).then(function(result) {
      if (result.error) {
        var errorDiv = document.getElementById('card-errors');
        var html =
          `<span>${result.error.message}</span>`;
        $(errorDiv).html(html);
        $('#payment-form').fadeToggle(100);
        $('#loading-overlay').fadeToggle(100);
        card.update({'disabled': false});
        $('#submit-button').attr('disabled', false);
      } else {
        if (result.paymentIntent.status === 'succeeded') {  
          form.submit();
        }
      }
    });
  }).fail(function () {
    location.reload();
  })
});