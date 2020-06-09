from .cart import Cart


def cart(request):
    # print('[*] I\'m Cart context processor and I\'m running...', Cart(request))
    return {'cart': Cart(request)}
