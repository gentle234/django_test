from django.shortcuts import render


def home(request):
    context = {
        'Welcome_message' : 'Welcome to Tatafomedia',
        'images': [
            {'src': 'image1.jpg', 'caption': 'Leopard'},
            {'src': 'image2.jpg', 'caption': 'Kangroo'},
            {'src': 'image3.jpg', 'caption': 'Time is Ticking'},
            
        ],
        'videos': [
            {'src': "https://www.youtube.com/embed/qDwdMDQ8oX4?si=k3eTJXKXs7v_P3LW"},
            {'src': "https://www.youtube.com/embed/qDwdMDQ8oX4?si=k3eTJXKXs7v_P3LW"},
            {'src': "https://www.youtube.com/embed/qDwdMDQ8oX4?si=k3eTJXKXs7v_P3LW"}, 
        ],
        'files': [
            {'href': 'documents/file1.pdf', 'name': 'File 1'},
            {'href': 'documents/file2.pdf', 'name': 'File 2'},
        ],
    }
    
    return render(request, 'application/home.html', context)

def about(request):
    return render(request, 'application/about.html')

# Create your views here.
