def create_stripe_subscription(customer_id,token,subscription_plan_id,planId,userId,coupon_code,is_coupon_applied):
    conn,cur = get_connection(DB_CONNECTION_STR)
    
    #creating subscription on stripe using the customer id
    try:
        stripe.PaymentMethod.attach(
            token,
            customer=customer_id
        )
        
        stripe.Customer.modify(
            customer_id,    
            invoice_settings={
                "default_payment_method": token,
            },
        )
        #
        # Step 3: Create a PaymentIntent for the initial payment
        amount = get_subscription_amount(planId)
        print('amount',amount)
        if not amount:
            def_dict = {'message': 'Subscription plan does not exist','status':400,'success':False}
            return def_dict
        
        amount_data = checkStripeCoupon(DB_CONNECTION_STR,userId,coupon_code,planId)
        amount_data = amount_data['final_price']
        
        # payment_intent = stripe.PaymentIntent.create(
        #     amount=amount,
        #     currency="usd",  # Replace with your currency
        #     customer=customer_id,
        #     payment_method=token,
        #     confirmation_method="automatic",
        #     confirm=True,
        # )
        payment_intent = stripe.PaymentIntent.create(
            amount=int(float(amount) * 100),
            currency="usd",  # Replace with your currency
            customer=customer_id,
            payment_method=token,
            # confirmation_method="automatic",
            confirm=True,
            automatic_payment_methods={
                "enabled": True,
                "allow_redirects": "never"
            }
        )

        # Step 4: Handle PaymentIntent status
        if payment_intent.status == "requires_action":
            def_dict = {'message': '3DS authentication required','status':400,'success': False,'client_secret': payment_intent.client_secret}
            return def_dict
        
        subscription = stripe.Subscription.create(
            customer=customer_id,
            items=[
                {
                    'plan': subscription_plan_id,
                },
            ],
            coupon=coupon_code
        )
        csc_result = check_subscription_created(DB_CONNECTION_STR,subscription,planId,userId,coupon_code,is_coupon_applied,customer_id)
        return csc_result
    except stripe.error.StripeError as e:
        conn.rollback()
        def_dict = {'message':'Subscription creation on Stripe failed','status':400,'success':False}
        return def_dict