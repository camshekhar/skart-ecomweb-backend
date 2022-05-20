from rest_framework.response import Response
from .models import Category, SubCategory, Product, Cart, OrderSummary
from .serializers import ProductSerializer, CategorySerializer, SubCategorySerializer, CartSerializer, OrderSummarySerializer
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def productDetails(request, subCategory):
    product = Product.objects.get(subCategory = subCategory)
    serializer = ProductSerializer(product, many= False)
    return Response(serializer.data)

@api_view(['GET'])
def categories(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def subCategory(request, category ):
    categories = SubCategory.objects.filter(category = category)
    serializer = SubCategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def subCategory2(request, pk):
    category = SubCategory.objects.get(id=pk)
    serializer = SubCategorySerializer(category, many= False)
    return Response(serializer.data)
@api_view(['GET'])
def cart(request):
    cartDetail = Cart.objects.all()
    serializer = CartSerializer(cartDetail, many= True)
    return Response(serializer.data)

@api_view(['POST'])
def addtoCart(request):
    cartItem = CartSerializer(data = request.data)
    # print(cartItem)
    if cartItem.is_valid():
        cartItem.save()
        # message = "Item Added to Cart"
        return Response(cartItem.data, status=status.HTTP_201_CREATED)
    # message = "Item Already in Cart"
    return Response(cartItem.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateCartQty(request, id, scope):
    cartItem = Cart.objects.get(id = id)
    if scope == "inc":
        cartItem.quantity = int(cartItem.quantity) + 1 if(int(cartItem.quantity) + 1) < 10 else 10;
    elif scope == "dec":
        cartItem.quantity = int(cartItem.quantity) - 1 if (int(cartItem.quantity) - 1) > 1 else 1;    
    cartItem.save() 
    return Response(status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def deleteCartItem(request, id):
    cartItem = Cart.objects.get(id = id)
    cartItem.delete();
    return Response(status=status.HTTP_200_OK)    
        
        
def orderSummary(request):
    order = OrderSummary.objects.all()
    cart = Cart.objects.all()
    for price in cart:
        price = cart.price * cart.quantity
    order.subtotal = price
    if order.subtotal < 500:
        order.total = order.subtotal
        order.save()    
        
    else:
        order.total = order.subtotal + order.shippingCharge 
        order.save()    
        
    order.save()    
    serializer = OrderSummarySerializer(order, many= True)
    return Response(serializer.data)    