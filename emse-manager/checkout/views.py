from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import stripe
from carts.cart import Cart

stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.
@login_required(login_url='/accounts/login/')
def checkout(request):
	cart = Cart(request)
	publishKey = settings.STRIPE_PUBLISHABLE_KEY
	customer_id = request.user.userstripe.stripe_id
	if request.method == 'POST':
		token = request.POST['stripeToken']
		# Charge the user's card:
		try:
			customer = stripe.Customer.retrieve(customer_id)
			customer.sources.create(source=token)
			charge = stripe.Charge.create(
				amount=int(cart.summary())*100,
				currency="usd",
				description="Example charge",
				customer = customer,
			)
			cart.clear()
		except stripe.error.CardError as e:
			#The card has been declined
			pass 

	context = {'publishKey': publishKey, 'cart': cart}
	template = 'checkout.html'
	return render(request,template,context)