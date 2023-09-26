from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse, HttpResponseRedirect
from gymapp.models import *
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from django.urls import reverse
from django.contrib import messages


# Create your views here.
def home(request):
    today_date = datetime.now().strftime('%d-%m-%Y')
    params = {'todays_date': today_date}
    return render(request, 'Home.html', params)

def registration(request):
    due_date_dict = {'monthly':1, 'three_months':3, 'six_months':6, 'one_year':12}
    fees = Fee.objects.all()
    trainers = Trainer.objects.all()
    trainer_dict = {}
    trainer_list = []
    plan_dict = {}
    pt_plan_dict = {}
    for fee in fees:
        # print('plan: ', fee.membership_plan_type)
        # print('fee:', fee.fee)
        plan_dict[fee.membership_plan_type] = fee.fee

    for pt_fee in fees:
        # print('PTplan: ', pt_fee.membership_plan_type)
        # print('PTfee:', pt_fee.pt_fee)
        pt_plan_dict[pt_fee.membership_plan_type] = pt_fee.pt_fee

    for trainer in trainers:
        trainer_list.append(trainer.name)

    trainer_dict['trainer_list'] = trainer_list

    if request.method == 'POST':

        name = request.POST['name']                           #form
        email = request.POST['email']                         #form
        mobile = request.POST['mobile']                       #form
        address = request.POST['address']                     #form
        height = request.POST['height']                       #form
        weight = request.POST['weight']                       #form
        input_dob = request.POST['dob']                       #form
        datetime_format = "%Y-%m-%d"
        dob = datetime.strptime(input_dob, datetime_format)   #logic
        gender = request.POST['gender']                       #form
        age = (datetime.now().year - dob.year)                #logic
        purpose = request.POST['purpose']                     #form
        membership_plan = request.POST['membership_plan']   #form
        personal_trainer = request.POST.get('check_personal_trainer', 0) #form    
        print("personal_trainer: ", personal_trainer)
        if personal_trainer != '1':
            total_fees = plan_dict[membership_plan]               #logic
            personal_trainer = False
        else:
            total_fees = pt_plan_dict[membership_plan]           #logic 
            personal_trainer = True
        fees_paid = request.POST['fees_paid']                 #form
        fees_remaining = request.POST['fees_remaining']       #form
        input_last_paid_date = request.POST['last_paid_date']       #form
        last_paid_date = datetime.strptime(input_last_paid_date, datetime_format)
        updated_plan_date = datetime.now()                   #logic
        input_date_of_join = request.POST['date_of_join']                  #logic
        date_of_join = datetime.strptime(input_date_of_join, datetime_format)
        fees_due_date = date_of_join + relativedelta(months=due_date_dict[membership_plan])                                   #logic
        # date_of_join = datetime.strptime(input_date_of_join, datetime_format)
        batch_time = request.POST['batch_time'] #form
        if personal_trainer == True:
            personal_trainer_name = request.POST['personal_trainer'] #form
        else:
            personal_trainer_name = 'Not Applicable'
        
        total_fees = total_fees + int(fees_remaining)

        print('Name: ', name)
        print('Email: ', email)
        print('Mobile: ', mobile)
        print('Address: ', address)
        print('Height: ', height)
        print('Weight: ', weight)
        print('Dob: ', dob)
        print('Gender: ', gender)
        print('Age: ', age)
        print('Purpose: ', purpose)
        print('Membership Plan: ', membership_plan)
        print('Total Fees: ', total_fees)
        print('Fees Paid: ', fees_paid)
        print('Fees Remaining: ', fees_remaining)
        print('Last Paid Date: ', last_paid_date)
        print('Updated Plan Date: ', updated_plan_date)
        print('Fees Due Date: ', fees_due_date)
        print('Date Of Join: ', date_of_join)
        print('Personal Trainer: ', personal_trainer)
        print('Batch Time: ', batch_time)
        print('Personal Trainer Name: ', personal_trainer_name)

        member = Member(name=name, email=email, mobile=mobile, address=address, height=height, weight=weight, dob=dob, 
                        gender=gender, age=age, purpose=purpose, membership_plan=membership_plan, total_fees=total_fees, 
                        fees_paid=fees_paid, fees_remaining = fees_remaining, last_paid_date=last_paid_date, 
                        fees_due_date=fees_due_date, date_of_join=date_of_join, updated_plan_date=updated_plan_date, 
                        personal_trainer=personal_trainer, batch_time=batch_time, personal_trainer_name=personal_trainer_name)
        member.save()
        messages.success(request, 'Hurry!!! Member added successfully.')
        return render(request, 'Registration_form.html')
    else:
        print('Plan Dict: ', plan_dict)
        print('PT Plan Dict: ',pt_plan_dict)
        print('Trainer Dict: ', trainer_dict)
        params = {'plan_dict': plan_dict, 'pt_plan_dict': pt_plan_dict, 'trainer_dict': trainer_dict}
        return render(request, 'Registration_form.html', params)

def manage_members(request):
    if 'search' in request.GET:
        print('Search')
        search = request.GET['search']
        all_member_list = Member.objects.filter(name__icontains=search)
    else:
        all_member_list = Member.objects.all()  

    fees_due_member = []
    unpaid_member = []

    for mem in all_member_list:
        if mem.fees_due_date.day - date.today().day <= 3 and mem.fees_due_date.day - date.today().day > 0:
            fees_due_member.append(mem)

    for mem in all_member_list:
        # if mem.fees_remaining != 0 and mem.fees_due_date < date.today():
        if mem.fees_due_date < date.today():
            unpaid_member.append(mem)
    params = {'member_count': all_member_list, 'today': date.today(), 'due_members':fees_due_member, 
            'unpaid_members':unpaid_member}
    return render(request, 'Manage_members.html', params)

def update_member(request, member_id):
    # message = 'Timepass'
    due_date_dict = {'monthly':1, 'three_months':3, 'six_months':6, 'one_year':12}
    fees = Fee.objects.all()
    trainers = Trainer.objects.all()
    trainer_dict = {}
    trainer_list = []
    plan_dict = {}
    pt_plan_dict = {}
    for fee in fees:
        # print('plan: ', fee.membership_plan_type)
        # print('fee:', fee.fee)
        plan_dict[fee.membership_plan_type] = fee.fee

    for pt_fee in fees:
        # print('PTplan: ', pt_fee.membership_plan_type)
        # print('PTfee:', pt_fee.pt_fee)
        pt_plan_dict[pt_fee.membership_plan_type] = pt_fee.pt_fee

    for trainer in trainers:
        trainer_list.append(trainer.name)

    trainer_dict['trainer_list'] = trainer_list
    member = get_object_or_404(Member, id=member_id)
    remaining_fees = member.fees_remaining

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        dob = request.POST.get('dob')
        membership_plan = request.POST.get('membership_plan')
        fees_paid = request.POST.get('fees_paid')
        last_paid_date = request.POST.get('last_paid_date')
        personal_trainer = request.POST.get('need_trainer', 0)
        if personal_trainer != '1':
            total_fees = plan_dict[membership_plan]               #logic
            personal_trainer = False
        else:
            total_fees = pt_plan_dict[membership_plan]           #logic 
            personal_trainer = True
        
        # personal_trainer_update = request.POST.get('trainer')

        if personal_trainer == True:
            personal_trainer_update = request.POST['trainer'] #form
        else:
            personal_trainer_update = 'Not Applicable'
        
        fees_remaining = request.POST.get('fees_remaining')
        updated_plan_date = datetime.now()
        

        print('name', name)
        print('email', email)
        print('mobile', mobile)
        print('height', height)
        print('weight', weight)
        print('dob', dob)
        print('membership_plan', membership_plan)
        print('fees_paid', fees_paid)
        print('last_paid_date', last_paid_date)
        print('personal_trainer', personal_trainer)
        print('personal_trainer_update', personal_trainer_update)
        print('fees_remaining', fees_remaining)
        print('updated_plan_date', updated_plan_date)
        print('total_fees', total_fees)
        
       
        member = Member.objects.get(id=member_id)
        member.name = name
        member.email = email
        member.mobile = mobile
        member.height = height
        member.weight = weight
        member.dob = dob
        member.membership_plan = membership_plan
        member.fees_paid = fees_paid
        member.last_paid_date = last_paid_date
        member.personal_trainer = personal_trainer
        member.personal_trainer_name = personal_trainer_update
        member.fees_remaining = fees_remaining
        member.updated_plan_date = updated_plan_date
        member.total_fees = total_fees+int(fees_remaining)
        member.fees_due_date = updated_plan_date + relativedelta(months=due_date_dict[membership_plan])     
        member.save()
        params = {'member': member, 'plan_dict': plan_dict, 'pt_plan_dict': pt_plan_dict, 'trainer_dict': trainer_dict,
            'fees_remaining': remaining_fees}
        
    else:
        params = {'member': member, 'plan_dict': plan_dict, 'pt_plan_dict': pt_plan_dict, 'trainer_dict': trainer_dict,
                  'fees_remaining': remaining_fees}
    return render(request, 'Update_member.html', params)

def show_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    params = {'member': member}
    return render(request, 'Show_member.html', params)

def update_fees(request):
    # message = ''
    fees = Fee.objects.all()
    plan_dict = {}
    pt_plan_dict = {}

    for fee in fees:
        # print('plan: ', fee.membership_plan_type)
        # print('fee:', fee.fee)
        plan_dict[fee.membership_plan_type] = fee.fee

    for pt_fee in fees:
        # print('PTplan: ', pt_fee.membership_plan_type)
        # print('PTfee:', pt_fee.pt_fee)
        pt_plan_dict[pt_fee.membership_plan_type] = pt_fee.pt_fee

    if request.method == 'POST':
        monthly_fees = request.POST.get('monthly_fees')
        three_month_fees = request.POST.get('three_month_fees')
        six_month_fees = request.POST.get('six_month_fees')
        one_year_fees = request.POST.get('one_year_fees')
        pt_monthly_fees = request.POST.get('pt_monthly_fees')
        pt_three_month_fees = request.POST.get('pt_three_month_fees')
        # print('PT_THREE_MONTH', pt_three_month_fees)
        monthly_fees_update = Fee.objects.filter(membership_plan_type='monthly')
        three_months_fees_update = Fee.objects.filter(membership_plan_type='three_months')
        six_months_fees_update = Fee.objects.filter(membership_plan_type='six_months')
        one_year_fees_update = Fee.objects.filter(membership_plan_type='one_year')

        monthly_fees_update.update(fee=monthly_fees, pt_fee=pt_monthly_fees)
        three_months_fees_update.update(fee=three_month_fees, pt_fee=pt_three_month_fees)
        six_months_fees_update.update(fee=six_month_fees, pt_fee=0)
        one_year_fees_update.update(fee=one_year_fees, pt_fee=0)
        params = {'plan_dict':plan_dict, 'pt_plan_dict':pt_plan_dict}    
        return render(request, 'Update_fees.html', params)  

        # messages.success(request,'Fees updated successfully!!!')
        # message = 'Fees updated successfully!!!'
        # print(message)
        # return render(request, 'Update_fees.html', params) 
        
    # messages.success(request,'Fees updated successfully!!!')
    # print('PT_THREE_MONTH_OUTSIDE', plan_dict)
    params = {'plan_dict':plan_dict, 'pt_plan_dict':pt_plan_dict}    
    return render(request, 'Update_fees.html', params)  
    
def manage_trainer(request):
    if request.method == 'POST':
        trainer_name = request.POST['name']
        trainer_email = request.POST['email']
        trainer_address = request.POST['address']
        trainer_mobile = request.POST['mobile']
        input_trainer_dob = request.POST['dob']
        trainer_gender = request.POST['gender']
        trainer_join_date = request.POST['join_date']
                       
        datetime_format = "%Y-%m-%d"
        trainer_dob = datetime.strptime(input_trainer_dob, datetime_format) 

        print('name: ', trainer_name)
        print('email: ', trainer_email)
        print('mobile: ', trainer_mobile)
        print('dob: ', trainer_dob)
        print('gender: ', trainer_gender)
        print('join_date: ', trainer_join_date)

        trainer_age = (datetime.now().year - trainer_dob.year)

        trainer = Trainer(name=trainer_name, email=trainer_email, mobile=trainer_mobile, address=trainer_address,
                date_of_birth=trainer_dob, gender=trainer_gender, date_of_join=trainer_join_date, age=trainer_age)
        trainer.save()
        params = {'trainers': trainer}
        # return render(request, 'Manage_trainer.html', params)
    trainer = Trainer.objects.all()
    params = {'trainers': trainer}
    return render(request, 'Manage_trainer.html', params)

def delete_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    member.delete()
    return redirect(reverse('manage_members'))

def delete_trainer(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    trainer.delete()
    return redirect(reverse('manage_trainer'))