from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.core.files import File
from imagekit import ImageSpec
from imagekit.processors import ResizeToFill, Adjust
from django.conf import settings


class FilterImg(ImageSpec):
    processors = Adjust(contrast=1.2, sharpness=1.1, brightness =1.3),
    format 	   = 'JPEG'
    options    = {'quality': 100} 

#should pass a file
def changeBright(request):
    print "changeBright request"
    print "\n\n"
    # print "form: %s " % form
    print "the value of request.POST: %s" % request.POST
    print "the value of request.FILES: %s" % request.FILES

    #print "before assigning form: %s" % UploadFileForm(request.POST, request.FILES)
    # m = Image.open(infile)
    # im.save(outfile, "JPEG")
    #if request.method == 'POST':

    # base_dir_path = settings.BASE_DIR
    # img_list = os.path.join(os.path.dirname(base_dir_path),
    #     "static", "media")

	# source_file needs to take the request from the user
    source_file = open(settings.MEDIA_ROOT+'/test-images/elvis-duck.JPG')
    
    print "source_file :%s" % source_file  

    image_generator = FilterImg(source=source_file)
    result = image_generator.generate()

    #  this automatically creates directories with file output
	# filename = "/foo/bar/baz.txt"
	# if not os.path.exists(os.path.dirname(filename)):
	#     os.makedirs(os.path.dirname(filename))
	# with open(filename, "w") as f:
	#     f.write("FOOBAR")
    
    dest = file(settings.MEDIA_ROOT+'/test-images/test.jpg', 'w')
    dest.write(result.read())
    dest.close()
    return render_to_response('filter.html', context_instance=RequestContext(request))
   
    # data = {'form': form}
    # return render_to_response('filter.html', data, context_instance=RequestContext(request))