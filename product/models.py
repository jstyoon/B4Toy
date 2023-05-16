from django.db import models

# 과제에 포함된 커스텀 모델 예시를 사용합니다.

# model


class Product(models.Model):
    """
    상품 모델입니다.
    상품 코드, 상품 이름, 상품 설명, 상품 가격, 사이즈 필드를 가집니다.
    """
    SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )
    code = models.CharField(verbose_name="코드", max_length=20)
    # 필수는 아니지만 "필드이름"을 기입하면 테스트할 때 한글로 한눈에 확인할 수 있어서 가독성 좋음
    # 이를 verbose_name 이라고 한다. 없어도 장고의 강력한 유저db 생성 기능으로 자동생성 되지만
    # verbose_name을 명시하면 나중에 코드를 관리하기가 편하다?
    # 참고 https://djangojeng-e.github.io/2020/08/02/Django-Models-6%ED%8E%B8-Fields-verbose-field-names/
    name = models.CharField(verbose_name="코드", max_length=20)
    description = models.TextField(verbose_name="상품설명")
    # TextField는 max_length가 필요 없죠?
    price = models.PositiveIntegerField(verbose_name="상품가격")
    # price는 음수로 내려갈 일이 없으므로 양수형 필드PostiveIntegetField를 사용할 수 있다
    size = models.CharField(choices=SIZES, max_length=10)  # 10으로 변경
    """
    max_length=1로 해놓았을 때 지금은 문제가 없지만 사이즈를 추가해주면
    2가 되어 1보다 크기 때문에 DB에 따라 에러가 발생할 수 있다?
    그래서 max_length는 넉넉하게 잡는게 좋고 DB환경도 고려하는 게 중요하다?
    """
    """
    choices 매개변수는 Django 모델 필드에서 사용하는 매개변수 중 하나로
    해당 필드에서 선택 가능한 옵션을 지정하는 역할을 합니다.
    변수를 통해 튜플 리스트를 받으면 첫번째 요소는 실제 DB에 저장되는 값이 되고,
    두번째 요소는 사용자가 볼 수 있는 레이블(옵션의 이름)이 됩니다.
    """

#     이건 필요 없는 코드인가?
#     def __str__(self):
#         return self.code

#     def save(self, *args, **kwargs):
#         # 생성될 때 stock quantity를 0으로 초기화 로직 이건 왜 삭제되는 지 모르겠다


class Invetory(models.Model):
    """
    창고의 제품과 수량 정보를 담는 모델입니다.
    상품, 수량 필드를 작성합니다.
    작성한 Product 모델을 OneToOne 관계로 작성합시다.
    """
    # 이 둘은 똑같은 코드이다
    # # product = models.ForeignKey(Product, on_delete=models.CASCADE, unique=True)
    product= models.OneToOneField(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(verbose_name="상품수량")
    """
    ForeignKey인데 OneToOneField로 해야된다?
    related_name은 지정해주면 역참조할 때 좋다고 한다?
    인벤토리는 product라는 테이블을 참조하고 있기 때문에 관계가 형성이 되는데
    만약 참조하고 있는 프로덕트 데이터가 삭제되면 어떤 이벤트를 할거냐는 의미이다
    여기선 on_delete는 프로덕트가 사라지면 인벤토리에서도 삭제한다는 의미?
    """



class Inbound(models.Model):
    """
    입고 모델입니다.
    상품, 수량, 입고 날짜, 금액 필드를 작성합니다.
    """
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(verbose_name="입고상품수량")
    created_at = models.DateTimeField(verbose_name="입고일자", auto_now_add=True) 
    # auto_now_add=True : 생성되는 순간 이후로 변경되지 않는다
    # auto_now=True : 생성될 때 뿐만 아니라 수정할 때에도 시간 변동
    price = models.PositiveIntegerField(verbose_name="입고가격")
    
class Outbound(models.Model):
    """
    출고 모델입니다.
    상품, 수량, 입고 날짜, 금액 필드를 작성합니다.
    """
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(verbose_name="출고상품수량")
    created_at = models.DateTimeField(verbose_name="출고일자", auto_now_add=True)
    price = models.PositiveIntegerField(verbose_name="출고가격") 