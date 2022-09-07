# from django.http import HttpResponse
# from .models import RateLimit

# def apilimit(get_response):
#     def func(request):
#         count=0
#         user = request.user
#         if user.is_authenticated:
#             count+=1

#             print(count)
#             if count<=10:
#                 response = get_response(request)
#                 return response
#         else:
#             return HttpResponse('API Rate Limit Exceeded!')
#     return func