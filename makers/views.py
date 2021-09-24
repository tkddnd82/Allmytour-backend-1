import json, os

from django.views  import View
from django.http   import JsonResponse
from django.db     import transaction

from users.models  import User
from makers.models import Maker, MakerOption, ImageFile, Option
from users.utils   import login_required

class MakerView(View):
    @login_required
    @transaction.atomic
    def post(self, request):
        print(request)
        user            = request.user
        data            = request.POST
        licenses        = data.get('license','운전면허증').split(',')
        languages       = data.get('language','영어').split(',')
        profile_images  = request.FILES.get('profile_image')
        id_images       = request.FILES.get('id_image')
        license_images  = request.FILES.getlist('license_image')
        
        try:
            with transaction.atomic():
                maker, maker_created = Maker.objects.update_or_create(
                    user = user,
                    defaults={
                        'name'         : user.name,
                        'nickname'     : data.get('nickname',''),
                        'description'  : data.get('description',''),
                        'instagram'    : data.get('instagram',''),
                        'facebook'     : data.get('facebook',''),
                        'youtube'      : data.get('youtube',''),
                    }
                )
                option = maker.makeroption_set.filter(maker=maker)
                option.delete()
                [maker.option.add(Option.objects.get(upper_code=0,option_name=license))for license in licenses]
                [maker.option.add(Option.objects.get(upper_code=1,option_name=language))for language in languages]
                
                with transaction.atomic():
                    image = maker.imagefile_set.filter(maker=maker)
                    image.delete()
                    ImageFile.objects.bulk_create([
                       ImageFile(maker=maker, image=profile_images),
                       ImageFile(maker=maker, image=id_images),
                       ])
                    ImageFile.objects.bulk_create([
                       ImageFile(maker=maker, image=license_image)for license_image in license_images])
                
                return JsonResponse({'message': 'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

    @login_required
    def get(self, request): 
        user          = request.user
        makers        = Maker.objects.filter(user=user).prefetch_related('imagefile_set','option')

        results     = [{
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

        return JsonResponse({'results': results}, status=200)

    @login_required
    def delete(self, request, maker_id):
        user = request.user
        makers = Maker.objects.get(user = user)
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

