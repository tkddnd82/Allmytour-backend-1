import json

from django.views  import View
from django.http   import JsonResponse
from django.db     import transaction

from users.models  import User
from makers.models import Maker, MakerOption, ImageFile, Option 
from users.utils   import login_required

class MakerView(View):
    @login_required
    def post(self, request):
        print(request)
        user          = request.user
        data          = request.POST
        licenses      = data.getlist('license')
        #etc           = data.get('etc')
        languages     = data.get('language').split(',')
        profile_image = request.FILES.get('profile_image')
        id_card_image = request.FILES.get('id_card_image','')
        license_image = request.FILES.getlist('license_image')
        
        try:
            with transaction.atomic():
                if data['name'] == '':
                    return JsonResponse({'message':'NOT_NAME'}, status = 400)

                if data['nickname'] == '':
                    return JsonResponse({'message':'NOT_NICKNAME'}, status = 400)
                
                if data['description'] == '':
                    return JsonResponse({'message':'NOT_DESCRIPTION'}, status = 400)

                if data['instagram'] == '' and data['facebook'] == '' and data['youtube'] == '':
                    return JsonResponse({'message':'NOT_SNS'}, status = 400)

                if profile_image == '' or license_image == '':
                    return JsonResponse({'message':'NOT_IMAGE'}, status = 400)
                        
                # if not data['license'] == Option.objects.filter(upper_code = 0).exists():
                #     return JsonResponse({'message':'NOT_LICENSE_CODE'}, status = 400)
                
                maker, maker_created = Maker.objects.update_or_create(
                    user     = user,
                    name     = user.name,
                    defaults = {
                        'nickname'     : data['nickname'],
                        'description'  : data['description'],
                        'instagram'    : data.get('instagram'),
                        'facebook'     : data.get('facebook'),
                        'youtube'      : data.get('youtube'),
                        'another_sns1' : data.get('another_sns1',''),
                        'another_sns2' : data.get('another_sns2',''),
                        'another_sns3' : data.get('another_sns3',''),
                    }                
                )    
                if not maker_created :
                    maker.name         = data['name']
                    maker.nickname     = data['nickname']
                    maker.description  = data['description']
                    maker.instagram    = data['instagram']
                    maker.facebook     = data['facebook']
                    maker.youtube      = data['youtube']
                    maker.another_sns1 = data['another_sns1']
                    maker.another_sns2 = data['another_sns2']
                    maker.another_sns3 = data['another_sns3']
                    maker.save()

                image, image_create = ImageFile.objects.update_or_create(
                    maker = maker,
                    defaults={
                        'license_image' : license_image,
                        'profile_image' : profile_image,
                        'id_card_image' : id_card_image,
                    }
                )
                if not image_create:
                    image.license_image = license_image
                    image.profile_image = profile_image
                    image.id_card_image = id_card_image
                
                image.delete()
                

                #[maker.option.remove(MakerOption.objects.filter(id = license).exists())for license in licenses]
                [maker.option.add(Option.objects.get(option_name = license))for license in licenses]
                #[maker.option.add(Option.objects.get(id = etc))for etc in etc]
                [maker.option.add(Option.objects.get(option_name = language))for language in languages]
                
                #[maker.option.delete(Option.objects.get(id = language))for language in languages]


                #select_option = Option.objects.get()

                #option, option_created = MakerOption.objects.update_or_create(
                #    maker    = maker,
                #    defaults = {
                #        #'option_id' : languages,
                #        #'licence'  : licenses,
                #        'etc'      : etc
                #    }
                #)
                #if not option_created and Option.objects.filter(option_name__icontains='기타'):
                #    #option.option_id = languages
                #    #option.option_id = licenses
                #    option.etc
                #    option.save()

                return JsonResponse({'message' : 'SUCCESS'}, status = 200)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
    



    @login_required
    def get(self, request, maker_id):
        print(request)
        user   = request.user
        makers = Maker.objects.filter(id = maker_id, user = user)

        results = [{
            'name'         : user.name,
            'nickname'     : maker.nickname,
            'description'  : maker.description,
            'instagram'    : maker.instagram,
            'facebook'     : maker.facebook,
            'youtube'      : maker.youtube,
            'another_sns1' : maker.another_sns1,
            'another_sns2' : maker.another_sns2,
            'another_sns3' : maker.another_sns3,
            'licenses'     : {
                'license'     : [option.option_name for option in maker.option.filter(upper_code=0)],
                'license_etc' : [option.etc for option in maker.makeroption_set.all()],
            },
            'languages'    : {
                'language'     : [option.option_name for option in maker.option.filter(upper_code=1)],
                'language_etc' : [option.etc for option in maker.option.filter(upper_code=1)]
            },
            'image_file'   : [{
                'profile_image' : image.profile_image, 
                'id_card_image' : image.id_card_image,
                'license_image' : image.license_image }for image in maker.imagefile_set.all()]
            }for maker in makers]

        return JsonResponse({'results': results}, status = 200)



        


        


