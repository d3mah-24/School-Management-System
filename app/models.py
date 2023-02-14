from django.db import models

# Create your models here.

keb = (("1", "01"), ("2", "02"), ("3", "03"), ("4", "04"))
gen = (("m", "M"), ("f", "F"))
clas = (("9", "9"), ("10", "10"), ("11", "11"), ("12", "12"))


class std(models.Model):
    name = models.CharField(max_length=10, default="")
    fname = models.CharField(max_length=10, default="")
    lname = models.CharField(max_length=10, default="")
    pass1 = models.CharField(max_length=20, default="")
    std_phone_num = models.CharField(max_length=10, default="")
    parent_phone_num = models.CharField(max_length=10, default="")
    parent_name = models.CharField(max_length=10, default="")
    parent_password = models.CharField(max_length=35, default="")
    # photo = models.FileField(upload_to="")
    unique_id = models.CharField(max_length=31, default="")
    room = models.CharField(max_length=1, default="A")

    kebele = models.CharField(max_length=1, default=4, choices=keb)
    gender = models.CharField(max_length=1, default="m", choices=gen)
    grade = models.CharField(max_length=2, default="12", choices=clas)
    age = models.IntegerField(default=16)

    os = models.CharField(max_length=140, default="")

    admin_type = models.CharField(max_length=5, default="stude")
    view_counter = models.IntegerField(default=1)
    no_forget = models.IntegerField(default=0)
    date_register = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class teach(models.Model):
    name = models.CharField(max_length=10, default="")
    fname = models.CharField(max_length=10, default="")
    lname = models.CharField(max_length=10, default="")
    subject = models.CharField(max_length=10, default="")
    grade = models.CharField(max_length=10, default="")
    room = models.CharField(max_length=10, default="")
    all_class = models.CharField(max_length=10, default="")
    unique_id = models.CharField(max_length=10, default="")
    pass1 = models.CharField(max_length=20, default="")
    std_phone_num = models.CharField(max_length=10, default="")

    os = models.CharField(max_length=140, default="")

    admin_type = models.CharField(max_length=5, default="teach")
    view_counter = models.IntegerField(default=1)
    no_forget = models.IntegerField(default=0)
    date_register = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.unique_id


class mark_ict(models.Model):
    std_data = models.ForeignKey(std, on_delete=models.CASCADE)
    ten1 = models.CharField(max_length=3, default=5)
    ten2 = models.CharField(max_length=3, default=5)
    ten3 = models.CharField(max_length=3, default=5)
    twenty = models.CharField(max_length=3, default=15)
    fifty = models.CharField(max_length=3, default=35)
    hundred = models.CharField(max_length=3, default=65)

    def __str__(self):
        return self.std_data.name
