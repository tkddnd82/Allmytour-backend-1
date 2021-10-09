import json, os

from django.views  import View
from django.http   import JsonResponse
from django.db     import transaction

from users.models  import User
from makers.models import Maker, MakerOption, Option, ImageFile
from users.utils   import login_required

class MakerView(View):
    @login_required
    @transaction.atomic
    def post(self, request):
        print(request)
<<<<<<< HEAD
        user           = request.user
        data           = request.POST
        licenses       = data.get('license','운전면허증').split(',')
        languages      = data.get('language','영어').split(',')
        profile_images = request.FILES.get('profile_image','camera.png')
        id_images      = request.FILES.get('id_image','camera.png')
        license_images = request.FILES.getlist('license_image')
=======
        user            = request.user
        data            = request.POST
<<<<<<< HEAD
        licenses        = data.get('license','운전면허증').split(',')
        languages       = data.get('language','영어').split(',')
        profile_images  = request.FILES.get('profile_image')
        id_images       = request.FILES.get('id_image')
        license_images  = request.FILES.getlist('license_image')
>>>>>>> 4b0e389 (Add: 모델링)
=======
        licenses        = data.get('license',None).split(',')
        languages       = data.get('language',None).split(',')
        profile_images  = request.FILES.get('profile_image',None)
        id_images       = request.FILES.get('id_image',None)
        license_images  = request.FILES.getlist('license_image') 
>>>>>>> df7a403 (Add:makers5)
        
        try:
            with transaction.atomic():
                maker, maker_created = Maker.objects.update_or_create(
                    user = user,
                    defaults={
<<<<<<< HEAD
                        'name'       : user.name,
                        'nickname'   : data.get('nickname',''),
                        'description': data.get('description',''),
                        'instagram'  : data.get('instagram',''),
                        'facebook'   : data.get('facebook',''),
                        'youtube'    : data.get('youtube',''),
=======
                        'name'         : user.name,
                        'nickname'     : data.get('nickname',''),
                        'description'  : data.get('description',''),
                        'instagram'    : data.get('instagram',''),
                        'facebook'     : data.get('facebook',''),
                        'youtube'      : data.get('youtube',''),
>>>>>>> 4b0e389 (Add: 모델링)
                    }
                )
                options = maker.makeroption_set.filter(maker=maker)
                options.delete()
                [maker.option.add(Option.objects.get(option_name=license))for license in licenses]
                [maker.option.add(Option.objects.get(option_name=language))for language in languages]
 
                with transaction.atomic():
                    image = maker.imagefile_set.filter(maker=maker)
                    image.delete()
                    ImageFile.objects.bulk_create([
                       ImageFile(maker=maker, image=profile_images),
                       ImageFile(maker=maker, image=id_images),
                       ])
                    ImageFile.objects.bulk_create([
                       ImageFile(maker=maker, image=license_image)for license_image in license_images])
<<<<<<< HEAD
<<<<<<< HEAD

=======
                    
>>>>>>> df7a403 (Add:makers5)
                    makers = Maker.objects.get(user=user)
                    maker_id = {
                        'id' : makers.id
                    }
<<<<<<< HEAD
                
                return JsonResponse({'message': 'SUCCESS','maker_id':maker_id}, status=200)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
        except Option.DoesNotExist:
            return JsonResponse({'message':'NOT_LICENSE_OR_LANGUAGE'}, status=200)    

    @login_required
    def get(self, request,maker_id): 
        user = request.user
        try:
            makers = Maker.objects.filter(id=maker_id, user=user).prefetch_related('imagefile_set','option')

            results = [{
                'id'         : maker.id,
                'name'       : user.name,
                'nickname'   : maker.nickname,
                'description': maker.description,
                'instagram'  : maker.instagram,
                'facebook'   : maker.facebook,
                'youtube'    : maker.youtube,
                'licenses'   : [{
                    'id '    : option.id,
                    'license': option.option_name,
                }for option in maker.option.filter(upper_code=0)],
                'languages'  : [{
                    'id '     : option.id,
                    'language': option.option_name,
                }for option in maker.option.filter(upper_code=1)],
                'profile_image': [image.image.url for image in maker.imagefile_set.filter(maker = maker)][0],
                'id_image'     : [image.image.url for image in maker.imagefile_set.filter(maker = maker)][1],
            }for maker in makers]
            
        except ValueError:
            return JsonResponse({'MESSAGE': 'NO_IMAGE'}, status=200)
=======
                
                return JsonResponse({'message': 'SUCCESS'}, status=200)
=======

                return JsonResponse({'message': 'SUCCESS','maker_id':maker_id}, status=200)
>>>>>>> df7a403 (Add:makers5)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=200)
        except Option.DoesNotExist:
            return JsonResponse({"message": "NOT_LICENSE_OR_LANGUAGE"}, status=200)

    @login_required
    def get(self, request, maker_id): 
        user   = request.user
        try:
            makers = Maker.objects.filter(id=maker_id,user=user).prefetch_related('imagefile_set','option')

            results = [{
                'id'         : maker.id,
                'name'       : user.name,
                'nickname'   : maker.nickname,
                'description': maker.description,
                'instagram'  : maker.instagram,
                'facebook'   : maker.facebook,
                'youtube'    : maker.youtube,
                'licenses'   : [{
                    'id '    : option.id,
                    'license': option.option_name,
                }for option in maker.option.filter(upper_code=0)],
                'languages'  : [{
                    'id '     : option.id,
                    'language': option.option_name,
                }for option in maker.option.filter(upper_code=1)],
                'profile_image': [image.image.url for image in maker.imagefile_set.filter(maker = maker)][0],
                'id_image'     : [image.image.url for image in maker.imagefile_set.filter(maker = maker)][1],
                'license_image': [image.image.url for image in maker.imagefile_set.filter(maker = maker)][2:]
            }for maker in makers]

<<<<<<< HEAD
>>>>>>> 4b0e389 (Add: 모델링)
=======
        except TypeError:
            return JsonResponse({'MESSAGE': 'NO_MAKER_ID'}, status=200)
        except ValueError:
            return JsonResponse({'MESSAGE': 'NO_IMAGE'}, status=200)
>>>>>>> df7a403 (Add:makers5)
        return JsonResponse({'results': results}, status=200)

    @login_required
    def delete(self, request, maker_id):
        user = request.user
<<<<<<< HEAD
        makers = Maker.objects.get(id = maker_id, user = user)
=======
        makers = Maker.objects.get(user = user)
>>>>>>> 4b0e389 (Add: 모델링)
        makers.delete()

        return JsonResponse({'message':'DELETE_SUCCESS'}, status = 200)

# class OptionView(View):
#     def get(self, request):
#         option = {
#             'licenses' : [{
#                 'id'         : license.id,
#                 'upper_code' : license.upper_code,
#                 'option_name': license.option_name
#             }for license in Option.objects.filter(upper_code=0)],
#             'languages' : [{
#                 'id'         : language.id,
#                 'upper_code' : language.upper_code,
#                 'option_name': language.option_name
#             }for language in Option.objects.filter(upper_code=1)]
#         }
#         return JsonResponse({'results': option}, status=200)

