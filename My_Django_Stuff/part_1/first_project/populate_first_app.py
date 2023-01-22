import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')



import django
django.setup()


# fake pop script


import random
from first_app.models import Accessrecord,Webpage,Topic
from faker import Faker

fakegen = Faker()

topic=['Search','Social','Maeketplace','News','News']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topic))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):

        # get the topic for the entry
        top=add_topic()

        # create the fake data for the entry
        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()


        #create the new webpage entry

        webpg=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        # create a fake access record for that webpage

if __name__=='__main__':
    print('populating scripts!')
    populate(20)
    print('populating complete!')
