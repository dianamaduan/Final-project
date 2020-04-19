from django.urls import path
from . import views

urlpatterns = [
    path('products', views.ProductViews.as_view()),
    path('products/<int:pk>', views.DeleteProductView.as_view()),
    path('createProducts', views.CreateProductViews.as_view()),
    path('comments/<int:product_id>', views.CommentsViews.as_view()),
    path('comments', views.CreateCommentsViews.as_view()),
    path('comments/<int:pk>', views.DeleteCommentsView.as_view()),
    path('categories', views.CategoriesViews.as_view()),
    path('getcategories', views.GetCategoriesViews.as_view()),
    path('categories/<int:pk>', views.DeleteCategoryView.as_view()),
    path('getproducts', views.GetProductViews.as_view()),
    path('baskets', views.BasketView.as_view()),
    path('baskets/<int:pk>', views.DeleteBasketView.as_view()),
    path('order', views.OrderCreateView.as_view()),
    path('rating', views.RatingViews.as_view())
]