from django.conf.urls.static import static
from django.urls import path

from Cottage import settings
from new_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('indexx', views.indexx, name='indexx'),
    path('login', views.login, name='login'),
    path('industry', views.industry, name='industry'),
    path('consumer', views.consumer, name='consumer'),
    path('consumer_registration', views.consumer_registration, name='consumer_registration'),
    path('industry_registration', views.industry_registration, name='industry_registration'),
    path('adminbase', views.adminbase, name='adminbase'),
    path('consumerbase', views.consumerbase, name='consumerbase'),
    path('industrybase', views.industrybase, name='industrybase'),
    path('view_industry', views.view_industry, name='view_industry'),
    path('admin_view_industry', views.admin_view_industry, name='admin_view_industry'),
    path('consumer_view_industry/', views.consumer_view_industry, name='consumer_view_industry'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),


    path('consumer_view_products', views.consumer_view_products, name='consumer_view_products'),
    path('purchase/<int:product_id>/', views.purchase_product, name='purchase_product'),
    path('purchase/<int:product_id>/consumer/consumer_purchase_confirm/', views.consumer_purchase_confirm, name='consumer_purchase_confirm'),
    path('view_consumer', views.view_consumer, name='view_consumer'),
    path('submit_complaint/', views.submit_complaint, name='submit_complaint'),
    path('view_complaints/', views.view_complaints, name='view_complaints'),
    path('complaint/<int:complaint_id>/', views.view_complaint_detail, name='view_complaint_detail'),
    path('admin_view_complaints/', views.admin_view_complaints, name='admin_view_complaints'),  # Admin complaints view
    path('admin_view_complaint_detail/<int:complaint_id>/', views.admin_view_complaint_detail, name='admin_view_complaint_detail'),
    # Admin complaint detail
    path('add_industry', views.add_industry, name='add_industry'),
    path("update_industry/<int:id>/", views.update_industry, name="update_industry"),
    path('delete_industry/<int:id>/', views.delete_industry, name='delete_industry'),

    path("approve_industry/<int:user_id>/", views.approve_industry, name="approve_industry"),
    path("reject_industry/<int:user_id>/", views.reject_industry, name="reject_industry"),

    path('admin_view_industry/', views.admin_view_industry, name='admin_view_industry'),
    path('admin_view_consumers/', views.admin_view_consumer, name='admin_view_consumer'),



    path('consumer_notifications/', views.consumer_notifications, name='consumer_notifications'),

    path("feedback", views.feedback, name="feedback"),
    path("view", views.view, name="view"),
    path('feedbacks', views.feedbacks, name='feedbacks'),
    path("reply_feedback/<int:id>/", views.reply_feedback, name="reply_feedback"),
    path('add_product', views.add_product, name='add_product'),
    path("industry_profile/", views.industry_profile, name="industry_profile"),
    path('product_list', views.product_list, name='product_list'),
    path("update_product/<int:id>/", views.update_product, name="update_product"),
    path('update_products/<int:product_id>/', views.update_products, name='update_products'),
    path('payment/<int:order_id>/', views.payment_page, name='payment_page'),
    path('payment_success/<int:payment_id>/', views.payment_success, name='payment_success'),


    path('order_history/', views.order_history, name='order_history'),
    path('order_detail/<int:order_id>/', views.order_detail, name='order_detail'),
    path('reorder/<int:order_id>/', views.reorder, name='reorder'),

    path('feedback_ratings_graph/', views.feedback_ratings_graph, name='feedback_ratings_graph'),
    path('complaints_pie_chart/', views.complaints_pie_chart, name='complaints_pie_chart'),
    path('products_pie_chart/', views.products_pie_chart, name='products_pie_chart'),

    path('update_order_status/<int:order_id>/', views.update_order_status, name='update_order_status'),
    path('track_order/', views.track_order, name='track_order'),
    path('order_list/', views.order_list, name='order_list'),

    path('consumer_dashboard/', views.consumer_dashboard, name='consumer_dashboard'),

    path('create_job_post/', views.create_job_post, name='create_job_post'),
    path('industry_job_list/', views.industry_job_list, name='industry_job_list'),

    path('job/<int:job_id>/applications/', views.view_job_applications, name='view_job_applications'),
    path('application/<int:application_id>/<str:action>/', views.manage_application, name='manage_application'),

    path('consumer_job_list/', views.consumer_job_list, name='consumer_job_list'),
    path('jobs/<int:job_id>/apply/', views.job_detail_and_apply, name='job_detail_and_apply'),




    path('add_meeting/', views.add_meeting, name='add_meeting'),
    path('meeting_list', views.meeting_list, name='meeting_list'),
    path('view_meeting_list', views.view_meeting_list, name='view_meeting_list'),

    path('rsvp_list<int:pk>/rsvps/', views.rsvp_list, name='rsvp_list'),
    path('meeting_detail<int:pk>/', views.meeting_detail, name='meeting_detail'),





    path("logout_view", views.logout_view, name="logout_view"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)