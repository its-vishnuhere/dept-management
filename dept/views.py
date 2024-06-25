from django.shortcuts import redirect, render
from .models import *
from django.core.mail import send_mail
import random
from django.contrib import messages


# Create your views here.


def adduser(request):
    if request.method=='POST':
        email_id=request.POST.get('emailid')
        type_ur=request.POST.get('typeur')
        phone_no=request.POST.get('phoneno')
        dept_=request.POST.get('deptm')
        passwd_=request.POST.get('passwd')
        nameq=request.POST.get('mame')
        dobq=request.POST.get('dobb')
        genderq=request.POST.get('gende')
        addressq=request.POST.get('adddr')
        bloodgpq=request.POST.get('bloodp')
        regnoq=request.POST.get('regn')
        coursei=request.POST.get('coursew')
        batchi=request.POST.get('batchw')

        em=users(emailid=email_id,typeur=type_ur,phoneno=phone_no,deptm=dept_,passwd=passwd_,namep=nameq,reg_no=regnoq,dob=dobq,gender=genderq,address=addressq,blooddgp=bloodgpq)
        em.save()
        if(type_ur=="teacher"):
            em1=trprofiledata(name_tr=nameq,dob_tr=dobq,email_tr=email_id,dept_tr=dept_,phoneno_tr=phone_no,bloodgp_tr=bloodgpq,gender_tr=genderq,address_tr=addressq,passwd_tr=passwd_)
            em1.save()
        elif(type_ur=="student"):
            em2=stdprofiledata(name_sp=nameq,dob_sp=dobq,email_sp=email_id,dept_sp=dept_,phoneno_sp=phone_no,bloodgp_sp=bloodgpq,gender_sp=genderq,address_sp=addressq,passwd_sp=passwd_,reg_no_sp=regnoq,course_sp=coursei,batchyr_sp=batchi)
            em2.save()

        usercount=users.objects.all()
        count=0
        for i in usercount:
            count+=1
        cntusr={'count_user':count}


        # pt=users.objects.get(emailid=email_id)
        # print(pt.emailid)
        return render(request,'homepg.html',cntusr)
    return render(request,'adduser.html')

def login(request):
   
    try:
        if request.method=='POST':
            emailid0=request.POST.get('emailid')
            passwrd=request.POST.get('pass')
            user=users.objects.get(emailid=emailid0)
            dataobj=stdprofiledata.objects.all()
            dicti_o={'usertb':dataobj}
            
            if(user.emailid==emailid0):
                if(user.emailid==emailid0 and user.passwd==passwrd):
                    # print(user.typeur)
                    if(user.typeur=='Teacher'or user.typeur=='teacher'):
                        
                        datatr=users.objects.filter(emailid=emailid0)
                        data_tr=trprofiledata.objects.filter(email_tr=emailid0)
                        
                        myobj=stdprofiledata.objects.values()
                        adc={'dj':myobj}
                        lit=[]
                        lt=[]
            
                        for i in range(len(adc['dj'])):
                            a=adc['dj'][i]['batchyr_sp']
                            lit.append(a)
                        lit1=list(set(lit))

                        for j in range(len(adc['dj'])):
                            b=adc['dj'][j]['course_sp']
                            lt.append(b)
                        lt1=list(set(lt))
                            

                        dicti_o={'usertb':dataobj ,'trdata':datatr,'dataoftr':data_tr,'dat':lit1,'dat1':lt1}

                        return render(request,'teachr.html',dicti_o)
                    
                    elif(user.typeur=='Student' or user.typeur=='parent' or user.typeur=='student'):
                        users_spdata=users.objects.filter(emailid=emailid0)
                        std_data=stdprofiledata.objects.filter(email_sp=emailid0)
                        users_spdata1=users.objects.filter(emailid=emailid0).values()
                        mediaobj=study_material.objects.all()
                        mediaobj1=time_table.objects.all()
                        user_dict=users_spdata1[0]
                        print(user_dict)
                        markob=marks.objects.filter(email_m=emailid0)
                        notifictionobj=stdNotifications.objects.filter(notifydept=user_dict['deptm'])
                        stddataobjct=stdattends.objects.filter(emailidatt=emailid0)
                        userdict={'marksusr':markob,'datauser':std_data,'dataus':users_spdata,'dataattendstd':stddataobjct,'notificationkey':notifictionobj,'study':mediaobj,'ttable':mediaobj1}
                        

                        return render(request,'studentparent.html',userdict)
                    

                    elif(user.typeur=='principal'):
                        # print("This is principal")
                        datatrpr=users.objects.filter(emailid=emailid0)
                        
                        myobj=stdprofiledata.objects.values()
                        adc={'dj':myobj}
                        lit=[]
                        lt=[]
            
                        for i in range(len(adc['dj'])):
                            a=adc['dj'][i]['batchyr_sp']
                            lit.append(a)
                        lit1=list(set(lit))

                        for j in range(len(adc['dj'])):
                            b=adc['dj'][j]['course_sp']
                            lt.append(b)
                        lt1=list(set(lt))
                            

                        dicti_o={'newuser':datatrpr,'usertb':dataobj,'dat':lit1,'dat1':lt1}

                        return render(request,'principl.html',dicti_o)
                    
                    elif(user.typeur=='admin'):
                        usercount=users.objects.all()
                        count=0
                        for i in usercount:
                            count+=1
                        cntusr={'count_user':count}
                            
                        return render(request,'homepg.html',cntusr)
                    
                else:
                    myfn=True
                    return render(request,'loginhtml.html',{'myfn':myfn})
                # return render(request,'loginhtml.html')
            # print(user)
            else:
                return render(request,'loginhtml.html')
    except:
        return render(request,'loginhtml.html')
    return render(request,'loginhtml.html')
    
    
def logdata(request):
    dataretr=users.objects.all()
    datadict={"alluser":dataretr}
    # print(datadict)
    return render(request,'logdata.html',datadict)
def manage(request):
    if request.method=='POST':
        id=request.POST.get('userid')
        namei=request.POST.get('namea')
        email=request.POST.get('emaild')
        typeusr=request.POST.get('userty')
        phonen=request.POST.get('phonen')
        dept=request.POST.get('dept')
        passd=request.POST.get('pass')
        opt=request.POST.get('optn')
        us=request.POST.get('usertyp')
        # print(namei)
        if us=='Student'or'student':
             mydata=users.objects.filter(id=id)
             usdic={"mydata1":mydata}
             return render(request,'stdmanage.html',usdic)
        else:
             mydata=users.objects.filter(id=id)
             usdic={"mydata1":mydata}
             if opt=='update':
                    mydata.update(namep=namei,emailid=email,typeur=typeusr,phoneno=phonen,deptm=dept,passwd=passd)    
                    return redirect('logdata')  
             elif opt=='remove':
                     mydata.delete()
                     return redirect('logdata')
             return render(request,'profiledata.html',usdic)
        # print(opt)
        # mydata.delete()
        # print(usdic)
        # return redirect('logdata')
    return render(request,'homepg.html')

def profiledata(request):
    return render(request,'profiledata.html')

def attendance1(request):
    course=request.POST.get('dept')
    batch_yr=request.POST.get('batchq')
    mydataat=stdprofiledata.objects.filter(course_sp=course,batchyr_sp=batch_yr)
    # dt={'dt1':mydataat}
    
    stdats=stdattends.objects.all().values()
    dt={'dt1':mydataat,'atdnc':stdats}
   

        
        # print(stdats)
    return render(request,'attendanceteahrpg.html',dt)
    
    
    # mydataat=users.objects.filter(deptm=dept_)
    # dt={'dt1':mydataat}

    #     # print(mydataat)
            
    
    # return render(request,'attendanceteahrpg.html')
def dltattrec(request):
    emmail=request.POST.get('e_email')
    course=request.POST.get('crse')
    batch_yr=request.POST.get('btch')

    sid=request.POST.get('ssid') 
    mng=request.POST.get('managestd')

    dldata=stdattends.objects.filter(id=sid)
    dictdldata={'editatt':dldata,'crs':course,'btc':batch_yr}
    print(emmail,sid)
    if mng=='remove':
        mydataat=stdprofiledata.objects.filter(course_sp=course,batchyr_sp=batch_yr)
        dldata.delete()
        stdats=stdattends.objects.all().values()
        dt={'dt1':mydataat,'atdnc':stdats}
        
        

        
        # print(stdats)
        return render(request,'attendanceteahrpg.html',dt)
    

        
    return render(request,'editattend.html',dictdldata)
    

def attendancerec(request):
    if request.method=='POST':
        e_mail=request.POST.get('e_id')
        d_t=request.POST.get('datet')
        a_mor=request.POST.get('morning')
        course_=request.POST.get('deptm') 
        batch_y=request.POST.get('batch_')
        a_eve=request.POST.get('eve')
        if a_eve!='present':
            a_eve='absent'
        if a_mor!='present':
            a_mor='absent'
        newdat=stdprofiledata.objects.filter(email_sp=e_mail)
        data1={'dt2':newdat}
        # print(data1)
        for dt in data1['dt2']:     
            regno=dt.reg_no_sp
                                                                # taking regno from users table
        mydataat=stdprofiledata.objects.filter(course_sp=course_,batchyr_sp=batch_y)
        em1=stdprofiledata.objects.get(email_sp=e_mail)
        em_name=em1.name_sp
        # print(type(e_mail),regno,d_t,a_eve,a_mor)
        em=stdattends(nameatt=em_name,emailidatt=e_mail,regnoatt=regno,dateatt=d_t,checklistmor=a_mor,checklisteve=a_eve,courseatt=course_,batchatt=batch_y)
        print(e_mail)
        
        # print(em_name.namep)
        print(em_name)
        em.save()
        stdats=stdattends.objects.all().values()
        dt={'dt1':mydataat,'atdnc':stdats}
        

        
        # print(stdats)
        return render(request,'attendanceteahrpg.html',dt)
    
    return redirect('attendance1')

def teacher(request):
    
    return render(request,'teachr.html')

def stdmanage(request):
     if request.method=='POST':
        id=request.POST.get('userid')
        namei=request.POST.get('namea')
        email=request.POST.get('emaild')
        typeusr=request.POST.get('userty')
        phonen=request.POST.get('phonen')
        dept=request.POST.get('dept')
        passd=request.POST.get('pass')
        opt=request.POST.get('optn')
        # print('hey',email,opt,id)
        # us=request.POST.get('usertyp')
        mydata=users.objects.filter(emailid=email)
        if opt=='update':
            # print('hey',email,opt,id)
            mydata.update(namep=namei,emailid=email,typeur=typeusr,phoneno=phonen,deptm=dept,passwd=passd,reg_no=id)    
            # mydata.save()
            return redirect('logdata')  
        elif opt=='remove':
            mydata.delete()
            return redirect('logdata')
        return render(request,'stdmanage.html')
        # print(opt)
        # mydata.delete()
        # print(usdic)
        # return redirect('logdata')
     return render(request,'homepg.html')

def notification_students(request):
    mydatanot=stdNotifications.objects.all()
    data1={'datanot':mydatanot}
    if request.method=='POST':
        datenoti=request.POST.get('datenot')
        msgnoti=request.POST.get('msg_std')
        deptnoti=request.POST.get('deptnot')
        
        msgobj=stdNotifications(notifydate=datenoti,notifymsg=msgnoti,notifydept=deptnoti)
        msgobj.save()
                
    return render(request, 'add_notification.html',data1)

def view_notification(request):
    viewmsg=stdNotifications.objects.all()
    msgdict={'msges':viewmsg}
    return render(request,'stdprofile.html',msgdict)

###########
def add_student(request):
    if request.method=='POST':
        name_add=request.POST.get('namest_add')
        dept_add=request.POST.get('deptst_add')
        blood_add=request.POST.get('bloodst_add')
        email_add=request.POST.get('emailst_add')
        regno_add=request.POST.get('regnost_add')
        course_add=request.POST.get('coursest_add')
        batch_add=request.POST.get('batchst_add')
        phoneno_add=request.POST.get('phonest_add')
        dob_add=request.POST.get('dobst_add')
        gender_add=request.POST.get('genderst_add')
        address_add=request.POST.get('addrst_add')
        pass_add=request.POST.get('passwdst_add')

        if (len(phoneno_add) !=10):
            phonefn=True
            return render(request,'addstudentpg.html',{'phonefn':phonefn})
        else:
            stddatasaveobj=stdprofiledata(name_sp=name_add,reg_no_sp=regno_add,email_sp=email_add,dept_sp=dept_add,phoneno_sp=phoneno_add,bloodgp_sp=blood_add,batchyr_sp=batch_add,dob_sp=dob_add,gender_sp=gender_add,course_sp=course_add,address_sp=address_add,passwd_sp=pass_add)
            stddatasaveobj.save()
            usertabledata=users(namep=name_add,emailid=email_add,typeur='student',phoneno=phoneno_add,deptm=course_add,passwd=pass_add,reg_no=regno_add)
            usertabledata.save()
            return render(request,'addstudentpg.html')
        # print(name_add,dept_add,blood_add,email_add,regno_add,course_add,batch_add,phoneno_add,dob_add,address_add)
    return render(request,'addstudentpg.html')

def upload_tt(request):
    if request.method=='POST':
        batcht=request.POST.get('batch_tt')
        courset=request.POST.get('course_tt')
        ttfile=request.FILES.get('timetables')
        print(ttfile,batcht,courset)
        if courset and ttfile:
            ttobj=time_table(batch_t_t=batcht,course_t_t=courset,doc_t_t=ttfile)
            ttobj.save()
            mydataat=stdprofiledata.objects.filter(course_sp=courset,batchyr_sp=batcht)
            stdats=stdattends.objects.all().values()
            dt={'dt1':mydataat,'atdnc':stdats}
            return render(request,'attendanceteahrpg.html',dt)
        return render(request,'attendanceteahrpg.html',dt)
    return render(request,'attendanceteahrpg.html')

##########
def upload_doc(request):
    if request.method=='POST':
        docnm=request.POST.get('namedoc')
        batchdoc=request.POST.get('batch_doc')
        coursedoc=request.POST.get('course_doc')
        docmfile=request.FILES.get('materials')
        print('first if of materials')
        if coursedoc and docmfile:
            docobj=study_material(batch_doc_1=batchdoc,course_doc_1=coursedoc,doc_mat=docmfile,doc_name=docnm)
            docobj.save()
            mydataat=stdprofiledata.objects.filter(course_sp=coursedoc,batchyr_sp=batchdoc)
    # dt={'dt1':mydataat}
    # print(mydataat)
            stdats=stdattends.objects.all().values()
            dt={'dt1':mydataat,'atdnc':stdats}
            return render(request,'attendanceteahrpg.html',dt)
        return render(request,'attendanceteahrpg.html',dt)


        
        # print(stdats)
    return render(request,'attendanceteahrpg.html')
        

def add_teacher(request):
    if request.method=='POST':
        nametr=request.POST.get('nametr_add')
        emailtr=request.POST.get('emailtr_add')
        depttr=request.POST.get('depttr_add')
        bloodtr=request.POST.get('bloodtr_add')
        phonenotr=request.POST.get('phonetr_add')
        dobtr=request.POST.get('dobtr_add')
        gendertr=request.POST.get('gendertr_add')
        addresstr=request.POST.get('addrtr_add')
        passtr=request.POST.get('passwdtr_add')
        # opttr=request.POST.get('optn_add')
        mydata1=trprofiledata.objects.filter(email_tr=emailtr)
        mydatausr1=users.objects.filter(emailid=emailtr)
        # print(mydata)
        mydata1.update(name_tr=nametr,email_tr=emailtr,dept_tr=depttr,bloodgp_tr=bloodtr,dob_tr=dobtr,phoneno_tr=phonenotr,gender_tr=gendertr,address_tr=addresstr,passwd_tr=passtr)
        mydatausr1.update(namep=nametr,emailid=emailtr,phoneno=phonenotr,deptm=depttr,typeur='teacher',passwd=passtr,reg_no='null',dob=dobtr,gender=gendertr,address=addresstr,blooddgp=bloodtr)
        # stdats=stdattends.objects.all()
        dataobj=stdprofiledata.objects.all()
        # dicti_o={'usertb':dataobj}
        dicti_o={'dataoftr':mydata1,'usertb':dataobj}
        
        return render(request,'teachr.html',dicti_o)
    print("hi")
    return render(request,'teachr.html')

otp=[]
def protp():
    op=random.randint(1000,9999)
    otp.append(op)

def emailget(request):
    return render(request,'forgotpass.html')


def sendotp(request):
    repemail=request.POST.get('emailfg')
    userps=users.objects.all()
    datat={'passt':userps}
    if repemail:
        for i in datat['passt']:
            if(i.emailid==repemail):
                print("True")
                protp()
                msg=''
                rel=otp[-1]
                msg=msg+str(rel)
                recp_email=repemail
                snd_email=' Dept Management'
                send_mail("You OTP to change password is "+snd_email,msg,snd_email,[recp_email],fail_silently=False)
                emdic={'email1':repemail}
                return render(request,'genotp.html',emdic)
    return render(request,'forgotpass.html')

def snmail(request):
     otps=request.POST.get('ottp')
     ema=request.POST.get('emailr1')
     emdic1={'email2':ema}
    #  print(totp)
     if otps==str(otp[-1]):
              return render(request,'changepass.html',emdic1)
     return render(request,'genotp.html')

def cpasswd(request):
    pass1=request.POST.get('passwoed')
    pass2=request.POST.get('confirm_passwoed')
    emge=request.POST.get('emailr2')
    usrdata=users.objects.filter(emailid=emge).values()
    dataurdic={'datak':usrdata}
    urty=dataurdic['datak'][0]['typeur']
    
    if(pass1==pass2):
        if urty=='teacher' or urty=='Teacher':
            trur=trprofiledata.objects.filter(email_tr=emge)
            trur.update(passwd_tr=pass2)
            usrdata.update(passwd=pass2)
            return render(request,'loginhtml.html')
            
        elif urty=='student' or urty=='Student':
            
            stdur=stdprofiledata.objects.filter(email_sp=emge)
            stdur.update(passwd_sp=pass2)
            usrdata.update(passwd=pass2)
            return render(request,'loginhtml.html')

    else:
        return render(request,'changepass.html')
    return render(request,'changepass.html')



def princ_stdprof(request):
    course=request.POST.get('deptpr')
    batch_yr=request.POST.get('batchqpr')
    mydataat=stdprofiledata.objects.filter(course_sp=course,batchyr_sp=batch_yr)
    dt={'dt1':mydataat}
    return render(request,'stdprofpgprinci.html',dt)

def stdprincprof(request):
    emle=request.POST.get('emailofstd')
    stdetails=stdprofiledata.objects.filter(email_sp=emle)
    attndstd=stdattends.objects.filter(emailidatt=emle)
    markstd=marks.objects.filter(email_m=emle)
    stdatadictionary={'crntstd':stdetails,'crntattnd':attndstd,'crntmark':markstd}
    return render(request,'stddetailprinci.html',stdatadictionary)

def princi_trdt(request):
    trdtp=trprofiledata.objects.all().values()
    trdip={'trdatapr':trdtp}
    return render(request,'trprinci.html',trdip)


def matstd(request):
     mediaobj=study_material.objects.all()
     dict_media={'study':mediaobj}
     return render(request,'materialstd.html',dict_media)


def updatetrprofile(request):
    if request.method=='POST':
        eml=request.POST.get('e_id')
        trr=trprofiledata.objects.filter(email_tr=eml).values()
        trdi={'dt1tr':trr}
        return render(request,'addtr.html',trdi)
    
def marksstd(request):
    if request.method=='POST':
        regno_mrk=request.POST.get('regnomarks')
        name_mrk=request.POST.get('namemark')
        email_mrk=request.POST.get('emailmark')
        course_mrk=request.POST.get('coursemark')
        sem_mrk=request.POST.get('semmark')
        sgpa_mrk=request.POST.get('sgpamark')
        # print(regno_mrk,name_mrk,email_mrk,course_mrk,sem_mrk,sgpa_mrk)
        stdn=stdprofiledata.objects.filter(reg_no_sp=regno_mrk).values()
        stdmark={'markst':stdn}
        if sgpa_mrk:
            sav=marks(name_m=name_mrk,email_m=email_mrk,course_m=course_mrk,sem_m=sem_mrk,reg_m=regno_mrk,sgpa_m=sgpa_mrk)
            sav.save()
            return render(request,'marklst.html',stdmark)
        return render(request,'marklst.html',stdmark)
    return render(request,'marklst.html')