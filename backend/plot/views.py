from django.http import HttpResponse
from matplotlib import pylab
from pylab import *
import PIL, PIL.Image
import io

def test(request):
    longt = request.GET.get('longitude', 27.999912)
    lat = request.GET.get('latitude', 72.567)
    return get_graph(longt, lat)

def get_graph(long, lat):
    x = arange(0, 2*pi, 0.01)
    s = cos(x)**2
    plot(x, s)

    xlabel('xlabel(X)')
    ylabel('ylabel(Y)')
    title('Simple Graph!')
    grid(True)


    # Store image in a string buffer
    buffer = io.BytesIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pylab.close()

    # Send buffer in a http response the the browser with the mime type image/png set'''

    return HttpResponse(buffer.getvalue(), content_type="image/png")
