# from django.db import models
# from imagekit.models import ImageSpecField
# from imagekit.processors import ResizeToFill

# class Profile(models.Model):
# 	# this is uploading to a new file, but can we upload to just the user file?
#     avatar = models.ImageField(upload_to='avatars')
#     # why thumbnails?
#     avatar_thumbnail = ImageSpecField(source='avatar',
#                                       processors=[ResizeToFill(100, 50)],
#                                       format='JPEG',
#                                       options={'quality': 60})

# profile = Profile.objects.all()[0]
# print profile.avatar_thumbnail.url    # > /media/CACHE/images/982d5af84cddddfd0fbf70892b4431e4.jpg
# print profile.avatar_thumbnail.width  # > 100




################################################################################
# from django.db import models
# from imagekit.models import ProcessedImageField

# class Profile(models.Model):
#     avatar_thumbnail = ProcessedImageField(upload_to='avatars',
#                                            processors=[ResizeToFill(100, 50)],
#                                            format='JPEG',
#                                            options={'quality': 60})

# profile = Profile.objects.all()[0]
# print profile.avatar_thumbnail.url    # > /media/avatars/MY-avatar.jpg
# print profile.avatar_thumbnail.width  # > 100