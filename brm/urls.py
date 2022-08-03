from django.urls import path
from . import views
urlpatterns=[
    path('new-book/',views.newBook),
    path('view-books/',views.viewBooks),
    path('delete-book/',views.deleteBook),
    path('edit-book/',views.editBook),
    path('edit/',views.edit),
    path('add/',views.addBook),
    path('search-book/',views.searchBook),
    path('search/',views.search),
    path('login/',views.userLogin),
    path('logout/',views.userLogout),
    

]
