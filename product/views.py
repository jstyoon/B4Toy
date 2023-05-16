from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
# view

@login_required
def product_view(request):
    """
    GET : 상품 목록을 보여줍니다.
    POST : 상품을 생성합니다.
    """
    if request.method == 'POST':
        """ 상품 생성 """
        
    elif request.method == 'GET':
        """ 상품 조회 """

@login_required
def inbound_view(request):
    """ 상품 입고 """ 

@login_required
def outbound_view(request, product_id):
    """ 상품 출고 """ 