import json
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ofcourse.settings")
# import django
# django.setup()
from course.models import Course, Stacks, Course_Stacks, Company, Related_Stacks,Company_Stacks

# Course data
f = open(f'json/modify.json', encoding='UTF-8')
data = json.loads(f.read())  
# stack data
f = open(f'json/스택별.json', encoding='UTF-8')
data2 = json.loads(f.read()) 
# company data
f = open(f'json/회사별.json', encoding='UTF-8')
data3 = json.loads(f.read()) 


# Course 테이블 저장
# def run():
    # for i in data:
    #     url = data[i]['url']
    #     img_url = data[i]['image']
    #     title = i
    #     teacher = data[i]['teacher']
    #     headline = data[i]['headline']
    #     level = data[i]['level']
    #     score = data[i]['score']
    #     courseTime = data[i]['courseTime']
    #     studentCnt = data[i]['student']
    #     recommend = data[i]['recommend']
    #     reviewCnt = data[i]['reviewCnt']
    #     price = data[i]['price']
    #     rank = data[i]['rank']
    #     Course(
    #         url=url, 
    #         img_url=img_url, 
    #         title=title,
    #         teacher=teacher,
    #         headline=headline,
    #         level=level,
    #         score=score,
    #         courseTime=courseTime,
    #         studentCnt=studentCnt,
    #         recommend=recommend,
    #         reviewCnt=reviewCnt,
    #         price=price,
    #         rank=rank
    #     ).save()
    # #Stacks테이블 저장
    # for i in data2:
    #     stack = i
    #     logo = data2[i]['logo']
    #     assort = data2[i]['assort']
    #     described = data2[i]['described']
        
    #     Stacks(
    #         name = stack,
    #         logo = logo,
    #         assort = assort,
    #         described = described            
    #     ).save()

    # # Course_Stacks 중간테이블
    # for i in data2:
    #     for j in data:
    #         if i in data[j]['stacks']:
    #             Course_Stacks(course_id=Course.objects.get(title=j).pk,stacks_id=Stacks.objects.get(name=i).pk).save()

    # # Company 테이블
    # for i in data3:
    #     name = i
    #     logo = data3[i]['logo']
    #     stack_info = data3[i]['stack_info']

    #     Company(name=name, logo=logo, stack_info=stack_info).save()

    # # related_stack 테이블
    # for i in data2:
    #     stack_name_id = Stacks.objects.get(name=i).pk
    #     for j in data2[i]['related_stacks']:
    #         Related_Stacks(stack_name_id=stack_name_id,related_stacks=j ).save()
def run():
    # Company_Stacks 테이블
    # for i in data2:
    #     for j in data3:
    #         print(data3[j]['stacks'])
    #         if i in data3[j]['stacks']:
    #             Company_Stacks(company_id=Company.objects.get(name=j).pk,stacks_id=Stacks.objects.get(name=i).pk).save()
    for i in data3:
        for k,v in data3[i]['stacks'].items():
            if v != None and v != []:
                for stack in data3[i]['stacks'][k]:
                    Company_Stacks(company_id=Company.objects.get(name=i).pk,stacks_id=Stacks.objects.get(name=stack).pk).save()
                # name = i
                # stack = v[0][0]
                # Company_Stacks(Company_id=)

    print('DB저장완료')
            




