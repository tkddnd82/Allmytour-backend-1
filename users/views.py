import json
import bcrypt
import jwt, time
import re, requests, hashlib, hmac
import random, string
import datetime, base64

from datetime                           import datetime, timedelta
from json                               import JSONDecodeError
from .tokens                            import account_activation_token
from django.shortcuts                   import redirect
from django.contrib.sites.shortcuts     import get_current_site
from django.utils.http                  import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding              import force_bytes, force_text
from os                                 import name, pipe
from my_settings                        import ACCESS_KEY, AUTH_SECRET_KEY, FROM_PHONE_NUMBER, PHONE_CHECK, EMAIL, SERVICE_ID
from allmytour.settings                 import SECRET_KEY

from django.views                       import View
from django.http                        import JsonResponse, HttpResponse
from django .utils                      import timezone
from django.template.loader             import render_to_string
from django.utils.html                  import strip_tags

from users.models                       import  User, PhoneCheck, UserTemp
from users.utils                        import login_required
from django.core.mail                   import EmailMessage
from random                             import randint
from django.core                        import mail

def email_validation(email):
        p = re.compile('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$') 
        return not p.match(email)

def password_validation(password):
        p = re.compile('^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$')
        return not p.match(password)

        
class SignupView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            if email_validation(email=data['email']): 
                return JsonResponse({"MESSAGE":"INVALID_EMAIL"}, status=200)
            
            if password_validation(password=data['password']):
                return JsonResponse({"MESSAGE":"INVALID_PASSWORD"}, status=200)
                
            if User.objects.filter(email=data['email']).exists():
                 return JsonResponse({'MESSAGE' : 'EMAIL_ALREADY_EXISTS'}, status=200)
                
            if User.objects.filter(phone_number=data['phone_number']).exists():
               return JsonResponse({'MESSAGE' : 'PHONE_NUMBER_ALREADY_EXISTS'}, status=200)
                
                
            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            User.objects.create( 
               name          = data['name'],
               phone_number  = data['phone_number'],
               password      = hashed_password,
               email         = data['email'],
            )

            user = User.objects.get(email   =data['email'],name=data['name'])

            result = [{
                "name"    : user.name, 
            }]

            access_token = jwt.encode({'id' : user.id}, SECRET_KEY, algorithm = 'HS256')


            return JsonResponse({'MESSAGE':'SUCCESS', 'TOKEN': access_token, 'RESULT':result },status=200)
        except KeyError:
            return JsonResponse({"MESSAGE" : "KEY_ERROR"}, status = 200)

class NameView(View): 
    @login_required
    def get(self, request):
        user = request.user
        User.objects.get(id=user.id)
        result ={
            'name' : user.name
        }

        return JsonResponse({'result':result},status=200)

class EmailView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            if email_validation(email=data['email']):  
                return JsonResponse({"MESSAGE":"INVALID_EMAIL"}, status=200)

            if User.objects.filter(email=data['email']).exists(): 
                 return JsonResponse({'MESSAGE' : 'EMAIL_ALREADY_EXISTS'}, status=200)

            UserTemp.objects.create( 
                email   = data['email'],
            )
            return JsonResponse({"MESSAGE" : "SUCCESS"}, status = 200)
        except KeyError:
            return JsonResponse({"MESSAGE" : "KEY_ERROR"}, status = 200)

class SigninView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            password = data['password']
            
            if not User.objects.filter(email=data['email']).exists():
                return JsonResponse({"MESSAGE" : "INVALID_USER"}, status=200)
                
            user = User.objects.get(email=data['email'])
            
            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({'MESSAGE':'INVALID_USER'}, status=200)
                
            access_token = jwt.encode({'id' : user.id}, SECRET_KEY, algorithm = 'HS256')
            return JsonResponse({'MESSAGE':'SUCCESS', 'TOKEN': access_token },status=200)
        except KeyError:
            return JsonResponse({"MESSAGE" : "KEY_ERROR"}, status=200)

class PasswordResetView(View): #이메일 전송(만료시간5분/이메일 존재여부체크/유효성 체크)
    def post(self, request):
        try:
            data  = json.loads(request.body)
            email = data['email']


            if email_validation(email=data['email']): 
                return JsonResponse({"MESSAGE":"INVALID_EMAIL"}, status=200)

            if not User.objects.filter(email=email).exists():
                return JsonResponse({'MESSAGE': 'EMAIL_DOSENT_EXIST'}, status=200)

            user_info    = User.objects.get(email=email)
            expire_date  = datetime.now() + timedelta(minutes=2)

            token        = jwt.encode(
                {'user_id':user_info.id,'expired_at':str(expire_date)},
                SECRET_KEY,
                algorithm='HS256'
            )
           
            html_content = render_to_string('email.html',{
                'user_email':email,
                'user_token':f"http://localhost:3000/newpassword/{token}"
            })

            text_content = strip_tags(html_content)
            msg = mail.EmailMultiAlternatives(
                "Password Reset",
                text_content,
                EMAIL['EMAIL_HOST_USER'],
                [ email ]
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            return JsonResponse({'MESSAGE': 'EMAIL_SENDED',"TOKEN":token}, status=200)
        except json.decoder.JSONDecodeError:
            return JsonResponse({'MESSAGE': 'JSON_DECODE_ERROR'}, status=200)
        except KeyError:
            return JsonResponse({'MESSAGE': 'KEY_ERROR'}, status=200)
        except TypeError:
            return JsonResponse({'MESSAGE': 'TYPE_ERROR'}, status=200)
        except ValueError:
            return JsonResponse({'MESSAGE': 'VALUE_ERROR'}, status=200)
         
    def patch(self, request): #패스워드 수정
        try:
            data          = json.loads(request.body)
            token         = bytes(data['token'], 'utf-8')
            password      = data['password']
            new_password = data['new_password']

            decoded_token = jwt.decode(
                token,
                SECRET_KEY,
                algorithms = 'HS256'
            )
            if decoded_token['expired_at'] < str(datetime.now()):
                return JsonResponse({'MESSAGE': 'LINK_EXPIRED'}, status=200)

            if not data['password'] == data['new_password']:
                return JsonResponse({'MESSAGE':'CHECK_PASSWORD'}, status = 200)
            
            if password_validation(password=data['password']):
                return JsonResponse({"MESSAGE":"INVALID_PASSWORD"}, status=200)
                
            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            user          = User.objects.get(id=decoded_token['user_id'])
            user.password = hashed_password
            user.save()
            return JsonResponse({'MESSAGE': 'PASSWORD_CHANGED'}, status=200)
        except json.decoder.JSONDecodeError:
            return JsonResponse({'MESSAGE': 'JSON_DECODE_ERROR'}, status=200)
        except KeyError:    
            return JsonResponse({'MESSAGE': 'KEY_ERROR'}, status=200)
        except TypeError:
            return JsonResponse({'MESSAGE': 'TYPE_ERROR'}, status=200)
        except ValueError:
            return JsonResponse({'MESSAGE': 'VALUE_ERROR'}, status=200)

class SMSVerificationView(View):
    def send_verification(self, phone_number, auth_number):
        SMS_URL = 'https://sens.apigw.ntruss.com/sms/v2/services/' + f'{SERVICE_ID}' + '/messages'
        timestamp = str(int(time.time() * 1000))
        secret_key = bytes(AUTH_SECRET_KEY, 'utf-8')

        method = 'POST'
        uri = '/sms/v2/services/' + f'{SERVICE_ID}' + '/messages'
        message = method + ' ' + uri + '\n' + timestamp + '\n' + ACCESS_KEY

        message = bytes(message, 'utf-8')

        signingKey = base64.b64encode(
            hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())

        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'x-ncp-apigw-timestamp': timestamp,
            'x-ncp-iam-access-key': ACCESS_KEY,
            'x-ncp-apigw-signature-v2': signingKey,
        }

        body = {
            'type': 'SMS',
            'contentType': 'COMM',
            'countryCode': '82',
            'from': f'{FROM_PHONE_NUMBER}',
            'content': f'인녕하세요. 올마이투어 입니다. 인증번호 [{auth_number}]를 입력해주세요.',
            'messages': [
                {
                    'to': phone_number
                }
            ]
        }
        encoded_data = json.dumps(body)
        res = requests.post(SMS_URL, headers=headers, data=encoded_data)
        return HttpResponse(res.status_code)

    def post(self, request):
        try:
            data = json.loads(request.body)
            phone_number = data['phone_number']

            auth_number = str(randint(100000, 999999))
            
            PhoneCheck.objects.update_or_create(
                phone_number=phone_number,
                defaults={
                    'phone_number': phone_number,
                    'auth_number' : auth_number,
                    'expired_at' : timezone.now() + timezone.timedelta(minutes=1)
                })
            self.send_verification(
                phone_number=phone_number,
                auth_number=auth_number
            )
            return JsonResponse({'MESSAGE': 'SUCCESS'}, status=200)
        except KeyError as e:
            return JsonResponse({'MESSAGE': f'KEY_ERROR: =>  {e}'}, status=200)

        except ValueError as e:
            return JsonResponse({'MESSAGE': f'VALUE_ERROR: =>  {e}'}, status=200)

class SMSVerificationConfirmView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            phone_number = data['phone_number']
            auth_number = data['auth_number']

            phone_check  = PhoneCheck.objects.filter(phone_number=phone_number, auth_number=auth_number).exists()
            if not phone_check:
                return JsonResponse({'MESSAGE':'INVALID_AUTH_NUMBER'}, status=200)
            
            time_check = PhoneCheck.objects.get(phone_number=data['phone_number'])
            
            if time_check.expired_at < timezone.now():
                return JsonResponse({'MESSAGE':'EXPIRED_CODE'}, status=200)
            return JsonResponse({'MESSAGE':'SUCCESS'}, status=200)
        
        except KeyError as e:
            return JsonResponse({'MESSAGE': f'KEY_ERROR: =>  {e}'}, status=200)

        except ValueError as e:
            return JsonResponse({'MESSAGE': f'VALUE_ERROR: =>  {e}'}, status=200)
