
from django.db import models

class AdmissionDetails(models.Model):
    sname = models.CharField(max_length=20)  # Removed primary_key and unique since it's part of unique_together
    gender = models.CharField(max_length=20, blank=True, null=True)
    admission_year = models.IntegerField()  # Removed unique since it's part of unique_together
    admission_mode = models.CharField(max_length=20, blank=True, null=True)
    first_year_left = models.CharField(max_length=20, blank=True, null=True)
    special_adid = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'admission_details'
        unique_together = (('sname', 'admission_year'),)

    def __str__(self):
        return f"{self.sname} ({self.admission_year})"


from mininba.models import AdmissionDetails
from django.db import models


class Students(models.Model):
   
    admission_details = models.ForeignKey(
        AdmissionDetails,
        on_delete=models.DO_NOTHING,
        db_column='admission_details_id',
        blank=True,
        null=True,
        related_name='students',
    )
    sem1_sub1 = models.IntegerField(blank=True, null=True)
    sem1_sub1_res = models.CharField(max_length=10, blank=True, null=True)
    sem1_sub2 = models.IntegerField(blank=True, null=True)
    sem1_sub2_res = models.CharField(max_length=10, blank=True, null=True)
   
    
    sem1_sub1 = models.IntegerField(blank=True, null=True)
    sem1_sub1_res = models.CharField(max_length=10, blank=True, null=True)
    sem1_sub2 = models.IntegerField(blank=True, null=True)
    sem1_sub2_res = models.CharField(max_length=10, blank=True, null=True)
    sem1_sub3 = models.IntegerField(blank=True, null=True)
    sem1_sub3_res = models.CharField(max_length=10, blank=True, null=True)
    sem1_sub4 = models.IntegerField(blank=True, null=True)
    sem1_sub4_res = models.CharField(max_length=10, blank=True, null=True)
    sem1_sub5 = models.IntegerField(blank=True, null=True)
    sem1_sub5_res = models.CharField(max_length=10, blank=True, null=True)
    sem1_sub6 = models.IntegerField(blank=True, null=True)
    sem1_sub6_res = models.CharField(max_length=10, blank=True, null=True)
    sem1_sub7 = models.IntegerField(blank=True, null=True)
    sem1_sub7_res = models.CharField(max_length=10, blank=True, null=True)
    sem1_sub8 = models.IntegerField(blank=True, null=True)
    sem1_sub8_res = models.CharField(max_length=10, blank=True, null=True)
    sem1_total = models.IntegerField(blank=True, null=True)
    
    sem2_sub1 = models.IntegerField(blank=True, null=True)
    sem2_sub1_res = models.CharField(max_length=10, blank=True, null=True)
    sem2_sub2 = models.IntegerField(blank=True, null=True)
    sem2_sub2_res = models.CharField(max_length=10, blank=True, null=True)
    sem2_sub3 = models.IntegerField(blank=True, null=True)
    sem2_sub3_res = models.CharField(max_length=10, blank=True, null=True)
    sem2_sub4 = models.IntegerField(blank=True, null=True)
    sem2_sub4_res = models.CharField(max_length=10, blank=True, null=True)
    sem2_sub5 = models.IntegerField(blank=True, null=True)
    sem2_sub5_res = models.CharField(max_length=10, blank=True, null=True)
    sem2_sub6 = models.IntegerField(blank=True, null=True)
    sem2_sub6_res = models.CharField(max_length=10, blank=True, null=True)
    sem2_sub7 = models.IntegerField(blank=True, null=True)
    sem2_sub7_res = models.CharField(max_length=10, blank=True, null=True)
    sem2_sub8 = models.IntegerField(blank=True, null=True)
    sem2_sub8_res = models.CharField(max_length=10, blank=True, null=True)
    sem2_total = models.IntegerField(blank=True, null=True)

    sem3_sub1 = models.IntegerField(blank=True, null=True)
    sem3_sub1_res = models.CharField(max_length=10, blank=True, null=True)
    sem3_sub2 = models.IntegerField(blank=True, null=True)
    sem3_sub2_res = models.CharField(max_length=10, blank=True, null=True)
    sem3_sub3 = models.IntegerField(blank=True, null=True)
    sem3_sub3_res = models.CharField(max_length=10, blank=True, null=True)
    sem3_sub4 = models.IntegerField(blank=True, null=True)
    sem3_sub4_res = models.CharField(max_length=10, blank=True, null=True)
    sem3_sub5 = models.IntegerField(blank=True, null=True)
    sem3_sub5_res = models.CharField(max_length=10, blank=True, null=True)
    sem3_sub6 = models.IntegerField(blank=True, null=True)
    sem3_sub6_res = models.CharField(max_length=10, blank=True, null=True)
    sem3_sub7 = models.IntegerField(blank=True, null=True)
    sem3_sub7_res = models.CharField(max_length=10, blank=True, null=True)
    sem3_sub8 = models.IntegerField(blank=True, null=True)
    sem3_sub8_res = models.CharField(max_length=10, blank=True, null=True)
    sem3_total = models.IntegerField(blank=True, null=True)

    sem4_sub1 = models.IntegerField(blank=True, null=True)
    sem4_sub1_res = models.CharField(max_length=10, blank=True, null=True)
    sem4_sub2 = models.IntegerField(blank=True, null=True)
    sem4_sub2_res = models.CharField(max_length=10, blank=True, null=True)
    sem4_sub3 = models.IntegerField(blank=True, null=True)
    sem4_sub3_res = models.CharField(max_length=10, blank=True, null=True)
    sem4_sub4 = models.IntegerField(blank=True, null=True)
    sem4_sub4_res = models.CharField(max_length=10, blank=True, null=True)
    sem4_sub5 = models.IntegerField(blank=True, null=True)
    sem4_sub5_res = models.CharField(max_length=10, blank=True, null=True)
    sem4_sub6 = models.IntegerField(blank=True, null=True)
    sem4_sub6_res = models.CharField(max_length=10, blank=True, null=True)
    sem4_sub7 = models.IntegerField(blank=True, null=True)
    sem4_sub7_res = models.CharField(max_length=10, blank=True, null=True)
    sem4_sub8 = models.IntegerField(blank=True, null=True)
    sem4_sub8_res = models.CharField(max_length=10, blank=True, null=True)
    sem4_total = models.IntegerField(blank=True, null=True)

    sem5_sub1 = models.IntegerField(blank=True, null=True)
    sem5_sub1_res = models.CharField(max_length=10, blank=True, null=True)
    sem5_sub2 = models.IntegerField(blank=True, null=True)
    sem5_sub2_res = models.CharField(max_length=10, blank=True, null=True)
    sem5_sub3 = models.IntegerField(blank=True, null=True)
    sem5_sub3_res = models.CharField(max_length=10, blank=True, null=True)
    sem5_sub4 = models.IntegerField(blank=True, null=True)
    sem5_sub4_res = models.CharField(max_length=10, blank=True, null=True)
    sem5_sub5 = models.IntegerField(blank=True, null=True)
    sem5_sub5_res = models.CharField(max_length=10, blank=True, null=True)
    sem5_sub6 = models.IntegerField(blank=True, null=True)
    sem5_sub6_res = models.CharField(max_length=10, blank=True, null=True)
    sem5_sub7 = models.IntegerField(blank=True, null=True)
    sem5_sub7_res = models.CharField(max_length=10, blank=True, null=True)
    sem5_sub8 = models.IntegerField(blank=True, null=True)
    sem5_sub8_res = models.CharField(max_length=10, blank=True, null=True)
    sem5_total = models.IntegerField(blank=True, null=True)
    

    sem6_sub1 = models.IntegerField(blank=True, null=True)
    sem6_sub1_res = models.CharField(max_length=10, blank=True, null=True)
    sem6_sub2 = models.IntegerField(blank=True, null=True)
    sem6_sub2_res = models.CharField(max_length=10, blank=True, null=True)
    sem6_sub3 = models.IntegerField(blank=True, null=True)
    sem6_sub3_res = models.CharField(max_length=10, blank=True, null=True)
    sem6_sub4 = models.IntegerField(blank=True, null=True)
    sem6_sub4_res = models.CharField(max_length=10, blank=True, null=True)
    sem6_sub5 = models.IntegerField(blank=True, null=True)
    sem6_sub5_res = models.CharField(max_length=10, blank=True, null=True)
    sem6_sub6 = models.IntegerField(blank=True, null=True)
    sem6_sub6_res = models.CharField(max_length=10, blank=True, null=True)
    sem6_sub7 = models.IntegerField(blank=True, null=True)
    sem6_sub7_res = models.CharField(max_length=10, blank=True, null=True)
    sem6_sub8 = models.IntegerField(blank=True, null=True)
    sem6_sub8_res = models.CharField(max_length=10, blank=True, null=True)
    sem6_total = models.IntegerField(blank=True, null=True)

    sem7_sub1 = models.IntegerField(blank=True, null=True)
    sem7_sub1_res = models.CharField(max_length=10, blank=True, null=True)
    sem7_sub2 = models.IntegerField(blank=True, null=True)
    sem7_sub2_res = models.CharField(max_length=10, blank=True, null=True)
    sem7_sub3 = models.IntegerField(blank=True, null=True)
    sem7_sub3_res = models.CharField(max_length=10, blank=True, null=True)
    sem7_sub4 = models.IntegerField(blank=True, null=True)
    sem7_sub4_res = models.CharField(max_length=10, blank=True, null=True)
    sem7_sub5 = models.IntegerField(blank=True, null=True)
    sem7_sub5_res = models.CharField(max_length=10, blank=True, null=True)
    sem7_sub6 = models.IntegerField(blank=True, null=True)
    sem7_sub6_res = models.CharField(max_length=10, blank=True, null=True)
    sem7_sub7 = models.IntegerField(blank=True, null=True)
    sem7_sub7_res = models.CharField(max_length=10, blank=True, null=True)
    sem7_sub8 = models.IntegerField(blank=True, null=True)
    sem7_sub8_res = models.CharField(max_length=10, blank=True, null=True)
    sem7_total = models.IntegerField(blank=True, null=True)
    
    sem8_sub1 = models.IntegerField(blank=True, null=True)
    sem8_sub1_res = models.CharField(max_length=10, blank=True, null=True)
    sem8_sub2 = models.IntegerField(blank=True, null=True)
    sem8_sub2_res = models.CharField(max_length=10, blank=True, null=True)
    sem8_sub3 = models.IntegerField(blank=True, null=True)
    sem8_sub3_res = models.CharField(max_length=10, blank=True, null=True)
    sem8_sub4 = models.IntegerField(blank=True, null=True)
    sem8_sub4_res = models.CharField(max_length=10, blank=True, null=True)
    sem8_sub5 = models.IntegerField(blank=True, null=True)
    sem8_sub5_res = models.CharField(max_length=10, blank=True, null=True)
    sem8_sub6 = models.IntegerField(blank=True, null=True)
    sem8_sub6_res = models.CharField(max_length=10, blank=True, null=True)
    sem8_sub7 = models.IntegerField(blank=True, null=True)
    sem8_sub7_res = models.CharField(max_length=10, blank=True, null=True)
    sem8_sub8 = models.IntegerField(blank=True, null=True)
    sem8_sub8_res = models.CharField(max_length=10, blank=True, null=True)
    sem8_total = models.IntegerField(blank=True, null=True) 
    class Meta:
        managed = True
        db_table = 'students'
        
