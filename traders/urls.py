from django.urls import path

# We will use views from notes app - so we need to import it.
from . import views 

'''
    The urls file is a map of routes called url patterns 
    urlpatterns contains the list of routes that the browser will respond to. 
    
    Each route specifies the route that will be requested (an "endpoint")
    and the function (in the views file - "views.") that will respond to the request.
'''
urlpatterns = [
    path('', views.ProductsListView.as_view(), name="product-list"),  # List view at /products/
    path('<int:pk>/', views.ProductsDetailView.as_view(), name="product-detail"),  # Detail view
    path('new/', views.ProductsCreateView.as_view(), name='product-create'),  # Create view
    path('<int:pk>/update/', views.ProductsUpdateView.as_view(), name='product-update'),  # Update view
    path('<int:pk>/delete/', views.ProductsDeleteView.as_view(), name='product-delete'),  # Delete view
]