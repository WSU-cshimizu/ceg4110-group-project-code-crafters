class MAIN_Candidate(models.Model):
    modal_id = models.CharField(max_length=50, editable=False, default=modalID_generator)
    fullname = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="candidates", blank=True)
    bio = models.TextField(null=True)
    position = models.TextField(choices=(
        ('President','President'),
         ('Vice President','Vice President'),
         ('Treasurer','Treasurer'),
         ('Secretary','Secretary'),
         ('Event Coordinator','Event Coordinator'),
         ('Sports and Recreation Officer','Sports and Recreation Officer'),
         ('Cultural affairs officer','Cultural affairs officer'),
         ('Department Representative','Department Representative'),
        ), null=True)
    voters = models.ManyToManyField(Account, blank=True)

        
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "/static/sb_admin/img/user.png"
    
    def __str__(self):
        return f"{self.fullname}"
    
    class Meta:
        verbose_name = "MAIN-WSU Candidate"  
        verbose_name_plural = "MAIN-WSU Candidates"



class CECS_Candidate(models.Model):
    modal_id = models.CharField(max_length=50, editable=False, default=modalID_generator)
    fullname = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="candidates", blank=True)
    bio = models.TextField(null=True)
    position = models.TextField(choices=(
         ('President','President'),
         ('Vice President','Vice President'),
         ('Treasurer','Treasurer'),
         ('Secretary','Secretary'),
         ('Event Coordinator','Event Coordinator'),
         ('Sports and Recreation Officer','Sports and Recreation Officer'),
         ('Cultural affairs officer','Cultural affairs officer'),
         ('Department Representative','Department Representative'),
        ), null=True)
    voters = models.ManyToManyField(Account, blank=True)
    

        
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "/static/sb_admin/img/user.png"


    def __str__(self):
        return f"{self.fullname}"
    
    class Meta:
        verbose_name = "CECS Candidate"  
        verbose_name_plural = "CECS Candidates"


class CSM_Candidate(models.Model):
    modal_id = models.CharField(max_length=50, editable=False, default=modalID_generator)
    fullname = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="candidates", blank=True)
    bio = models.TextField(null=True)
    position = models.TextField(choices=(
         ('President','President'),
         ('Vice President','Vice President'),
         ('Treasurer','Treasurer'),
         ('Secretary','Secretary'),
         ('Event Coordinator','Event Coordinator'),
         ('Sports and Recreation Officer','Sports and Recreation Officer'),
         ('Cultural affairs officer','Cultural affairs officer'),
         ('Department Representative','Department Representative'),
        ), null=True)
    voters = models.ManyToManyField(Account, blank=True)

        
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "/static/sb_admin/img/user.png"
    
    def __str__(self):
        return f"{self.fullname}"
    
    class Meta:
        verbose_name = "CSM Candidate"  
        verbose_name_plural = "CSM Candidates"


class CLA_Candidate(models.Model):
    modal_id = models.CharField(max_length=50, editable=False, default=modalID_generator)
    fullname = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="candidates", blank=True)
    bio = models.TextField(null=True)
    position = models.TextField(choices=(
         ('President','President'),
         ('Vice President','Vice President'),
         ('Treasurer','Treasurer'),
         ('Secretary','Secretary'),
         ('Event Coordinator','Event Coordinator'),
         ('Sports and Recreation Officer','Sports and Recreation Officer'),
         ('Cultural affairs officer','Cultural affairs officer'),
         ('Department Representative','Department Representative'),
        ), null=True)
    voters = models.ManyToManyField(Account, blank=True)

        
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "/static/sb_admin/img/user.png"
    
    def __str__(self):
        return f"{self.fullname}"
    
    class Meta:
        verbose_name = "CLA Candidate"  
        verbose_name_plural = "CLA Candidates"


class CBUS_Candidate(models.Model):
    modal_id = models.CharField(max_length=50, editable=False, default=modalID_generator)
    fullname = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="candidates", blank=True)
    bio = models.TextField(null=True)
    position = models.TextField(choices=(
        ('President','President'),
         ('Vice President','Vice President'),
         ('Treasurer','Treasurer'),
         ('Secretary','Secretary'),
         ('Event Coordinator','Event Coordinator'),
         ('Sports and Recreation Officer','Sports and Recreation Officer'),
         ('Cultural affairs officer','Cultural affairs officer'),
         ('Department Representative','Department Representative'),
        ), null=True)
    voters = models.ManyToManyField(Account, blank=True)

        
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "/static/sb_admin/img/user.png"
    
    def __str__(self):
        return f"{self.fullname}"

    class Meta:
        verbose_name = "CBUS Candidate"  
        verbose_name_plural = "CBUS Candidates"