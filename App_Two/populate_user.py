import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_two.settings')
sys.path.append('C:\Users\lenovo R3\Desktop\second_app\project_two')

import django
django.setup()

from App_Two.models import user
from faker import Faker

fakegen=Faker()

def populate(N=1):

    for entry in range(N):
        fake_name=fakegen.name().split()
        fake_first_name=fake_name[0]
        fake_last_name=fake_name[1]
        fake_email=fakegen.email()

        user1=user.objects.get_or_create(First_name=fake_first_name,
                                        Last_name=fake_last_name,
                                        email_id=fake_email)[0]

if __name__=='__main__':
    print("populating database")
    populate(20)
    print("complete")