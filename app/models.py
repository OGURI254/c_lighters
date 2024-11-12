from django.db import models

class Category(models.Model):
    title =  models.CharField(max_length=220, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('is_active', 'created_at')
        verbose_name_plural = 'Categories'

class Service(models.Model):
    title =  models.CharField(max_length=220, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    overview = models.TextField(max_length=300)
    icon = models.ImageField(upload_to="services/icon/")
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('is_active', 'created_at')

class ServiceImage(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service')
    img = models.ImageField(upload_to="services/images/")

    def __str__(self):
        return self.img.name

class Ministry(models.Model):
    title =  models.CharField(max_length=220, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    front_img = models.ImageField(upload_to="ministry/")
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('is_active', 'created_at')
        verbose_name_plural = 'Ministries'

class MinistryImage(models.Model):
    ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE, related_name='ministry')
    img = models.ImageField(upload_to="ministry/images/")

    def __str__(self):
        return self.img.name

class Blog(models.Model):
    title =  models.CharField(max_length=220, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    img = models.ImageField(upload_to="blog/")
    description = models.TextField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('is_published', 'created_at')

class Sermon(models.Model):
    title =  models.CharField(max_length=220, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='sermons')
    category  = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sermons')
    img = models.ImageField(upload_to="blog/")
    description = models.TextField(null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('is_active', 'created_at')

class CellGroup(models.Model):
    title =  models.CharField(max_length=220, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    whatsapp_link  = models.URLField()
    img = models.ImageField(upload_to="blog/")
    description = models.TextField(null=True, blank=True, max_length=300)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('is_active', 'created_at')

class Pastor(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='user')
    position = models.CharField(max_length=120)
    img = models.ImageField(upload_to="pastor/")
    fb_url = models.URLField(max_length=220, unique=True, null=True, blank=True)
    ig_url = models.URLField(max_length=220, unique=True, null=True, blank=True)
    linkedin_url = models.URLField(max_length=220, unique=True, null=True, blank=True)
    x_url = models.URLField(max_length=220, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name
    
    class Meta:
        ordering = ('position', 'created_at')

class Gallery(models.Model):
    img = models.ImageField(upload_to="gallery/")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.img.name
    
    class Meta:
        ordering = ('is_active', 'created_at')
        verbose_name_plural = 'Galleries'

class Contact(models.Model):
    first_name =  models.CharField(max_length=60)
    last_name =  models.CharField(max_length=60)
    email =  models.EmailField(max_length=255)
    phone_number =  models.CharField(max_length=13)
    description = models.TextField(null=True, blank=True)
    is_addressed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"
    
    class Meta:
        ordering = ('is_addressed', 'created_at')