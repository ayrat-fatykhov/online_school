import stripe

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY[1:]


def create_product(name, description):
    print(STRIPE_API_KEY)
    product = stripe.Product.create(
        name=name,
        description=description
    )
    return product.id


def create_price(product_id, price_amount, currency):
    """Создать цену в Stripe"""
    if price_amount is not None:
        price_amount = int(price_amount) * 100
        price = stripe.Price.create(
            product=product_id,
            unit_amount=price_amount,
            currency=currency
        )
        return price.id
    else:
        return None


def create_checkout_session(price_id):
    session = stripe.checkout.Session.create(
        success_url='http://127.0.0.1:8000/',
        line_items=[
            {
                "price": price_id,
                "quantity": 1
            }
        ],
        mode="payment"
    )
    return session.get('id'), session.get('url')
