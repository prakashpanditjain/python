def apply_discount(discount_amount):
    def decorator(fun):
        def wrapper(total_amount):
            discount = total_amount * discount_amount
            total = total_amount - discount
            return fun(total)

        return wrapper

    return decorator
