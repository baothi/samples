Product.objects.all()
-- SELECT * FROM app_product

Product.objects.get(pk=1)
-- SELECT * FROM app_product WHERE id=1

Product.objects.get(code='IPX')
-- SELECT * FROM app_product WHERE code='IPX'

Product.objects.filter(name__contains='IPhone')
-- SELECT * FROM app_product WHERE name LIKE '%IPhone%'

Product.objects.filter(name__startswith='IPhone')
-- SELECT * FROM app_product WHERE name LIKE 'IPhone%'

Product.objects.filter(name__endswith='IPhone')
-- SELECT * FROM app_product WHERE name LIKE '%IPhone'

Product.objects.filter(price__gt=10.0)
-- SELECT * FROM app_product WHERE price > 10

Tương tự : __lt (less than), __gte (greater than or equal),
           __lte (less than or equal)
           
Product.objects.filter(code__contains='IP', price__gt=10.0)
Product.objects.filter(code__contains='IP').filter(price__gt=10.0)

-- SELECT * FROM app_product WHERE code LIKE '%IP%' 
--                              AND price > 10.0    

from django.db.models import Q

Product.objects.filter(Q(code__contains='IP')|Q(name__contains='IP'))
-- SELECT * FROM app_product WHERE code LIKE '%IP%' OR name LIKE '%IP%'
       
Product.objects.filter(~Q(code__contains='IP'))       
-- SELECT * FROM app_product WHERE code NOT LIKE '%IP%'

Product.objects.order_by('price')
-- SELECT * FROM app_product ORDER BY price

Product.objects.order_by('-price')
-- SELECT * FROM app_product ORDER BY price DESC

Product.objects.filter(category__id=1)

-- SELECT * FROM app_product JOIN app_category
               ON app_product.category_id=app_category.id
               WHERE app_category.id=1
               
Product.objects.filter(category__code='APPLE')

Product.objects.filter(category__name__contains='Apple')
