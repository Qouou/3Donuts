from django.shortcuts import render
from django.http import FileResponse
from .models import User_picture
from django.contrib.auth.models import User
import os
import time
from django.utils import timezone
import subprocess
# Create your views here.

def index(request):
    donuts_user_picture = User_picture.objects.all()
    return render(request, 'base.html')

def model(request):
    donuts_user_picture = User_picture.objects.all()
    return render(request, 'model/index.html', locals())

def add(request):
    ctx ={}
    donuts_user_picture = User_picture.objects.all()

    if request.method == "POST":
        user = request.user  # 對應剛剛add.html 中的input name
        user_img = request.FILES.get('user_image')
        name = user.get_username() # username (str)
        now_path = os.getcwd()        
        user_picture = User_picture(user_name=name, user_image=user_img, upload_time=timezone.now())
        user_picture.save()
        #user_picture.save()
        print(str(user_picture.user_image))
        picture_path = now_path + '/media/'+str(user_picture.user_image)
        print(picture_path)
        try:
            os.popen('removebg --api-key jjsL3zr8oVHVjn6myEjypJxa '+picture_path)
            ctx['status'] = 'Success!'
            ctx['file'] = picture_path[:-4] +'-removebg.png'
            user_picture.user_image_after =  str(user_picture.user_image)[:-4] + '-removebg.png'
            user_picture.save() 
            while os.path.isfile(ctx['file']) == False:
                time.sleep(.5)
            ctx['file'] = str(user_picture.user_image)[:-4] + '-removebg.png'
            print('After: ' + ctx['file'])
            return render(request, 'model/index.html', ctx)
            #print(picture_path[:-4]+'-removebg.png')  
        except:
            ctx['status'] = 'Fail!'
            return render(request, 'model/index.html', ctx)
         
        #print(user_picture.user_image) # path image/<file_name>

       
    # =====新增的程式碼=====#
    return render(request, 'model/index.html', locals())

def pifu(request):
    ctx ={}
    donuts_user_picture = User_picture.objects.all()

    if request.method == "POST":
        # catch POST - image path and user
        user = request.user
        image = request.POST['image-to-model']

        # now path = ~/progress/mainsite
        now_path = os.getcwd()

        # image = image/<image_file_name>
        # picture path = ~/progress/mainsite/media/image/<image_file_name>
        picture_path = now_path + '/media/' + image
        print(os.getcwd())
        # change path to ~/progress/mainsite/pifuhd/pose
        # execute get_pose.py
        # get the points of pose estimation -> <image_file_name>_rect.txt
        try:
            os.chdir(r'../pifuhd/pose/')
        except:
            pass
        print(os.getcwd())
        os.popen('python -m get_pose -i '+ picture_path)
        while os.path.isfile(picture_path[:-4]+'_rect.txt') == False:
                time.sleep(.5)

        # put image and rect.txt to directionary
        new_dir_path = picture_path.replace("-removebg.png",'')
        os.popen('mkdir '+ new_dir_path)
        os.popen('cp ' + picture_path + ' '+ new_dir_path)
        os.popen('mv ' + picture_path.replace('.png','_rect.txt')+ ' '+ new_dir_path)

        # execute path : ~/progress/pifu
        os.chdir(r'../')
        subprocess.Popen(['python', '-m', 'apps.simple_test', '-r' ,'256' ,'--use_rect', '-i', new_dir_path ,'-o', new_dir_path])
        # python -m apps.simple_test -r 256 --use_rect -i $image_dir

        # change to original path
        os.chdir(now_path)
        print(os.getcwd())


    #print(locals())
    return render(request, 'model/index.html', locals())






"""
def download(request):
    user_name = request.user
    print(User.objects.get(username=user_name))
    filename = 'media/'+user_name+'.png'
    file=open(filename,'rb')
    response =FileResponse(file)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename='+filename
    return response
"""
