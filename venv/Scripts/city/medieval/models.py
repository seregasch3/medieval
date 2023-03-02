from django.db import models
 

class status(models.Model):
	status = models.CharField(max_length=30)
class feodals(models.Model):
	name = models.CharField(max_length=30)
	age = models.CharField(max_length=30)
	status = models.ForeignKey(status,on_delete=models.CASCADE)
	#status = models.CharField(max_length=30)
	income = models.CharField(max_length=30)
class seniors(models.Model):
	name = models.CharField(max_length=30)
	age = models.CharField(max_length=30)
	status = models.ForeignKey(status,on_delete=models.CASCADE)
	#status = models.CharField(max_length=30)
	income = models.CharField(max_length=30)
	feodal_id = models.ForeignKey(feodals,on_delete=models.CASCADE)


class citizens(models.Model):
	name = models.CharField(max_length=30)
	age = models.CharField(max_length=30)
	status = models.ForeignKey(status,on_delete=models.CASCADE)
	#status = models.CharField(max_length=30)
	income = models.CharField(max_length=30)
	senior_id = models.ForeignKey(seniors,on_delete=models.CASCADE)
