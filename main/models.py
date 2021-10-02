from django.db import models

# Wait this may be really bad.
class Task(models.Model):
    est_time = models.FloatField(blank=True, null=True)
    notes    = models.CharField(max_length=1000, blank=True, null=True)
    requires = models.CharField(max_length=1000, blank=True, null=True)
    created  = models.DateTimeField(auto_now_add=True)
    archive  = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return "{0} {1} {2} {3} {4}".format(self.est_time, self.notes, self.requires, self.created, self.archive)

