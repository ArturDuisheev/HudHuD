from django.urls import path

from . import views
app_name = 'DjangoHUDApp'
urlpatterns = [
    path('oauth/index/', views.index, name='index'),


    path('404/', views.error404, name='error404'),
    path('analytics/', views.analytics, name='analytics'),
    path('oauth/', views.pageOauth, name='oauth'),
    path('email/inbox/', views.emailInbox, name='emailInbox'),
    path('email/detail/', views.emailDetail, name='emailDetail'),
    path('email/compose/', views.emailCompose, name='emailCompose'),
    path('widgets/', views.widgets, name='widgets'),
    path('pos/customer-order/', views.posCustomerOrder, name='posCustomerOrder'),
    path('pos/kitchen-order/', views.posKitchenOrder, name='posKitchenOrder'),
    path('pos/counter-checkout/', views.posCounterCheckout, name='posCounterCheckout'),
    path('pos/table-booking/', views.posTableBooking, name='posTableBooking'),
    path('pos/menu-stock/', views.posMenuStock, name='posMenuStock'),
    path('ui/bootstrap/', views.uiBootstrap, name='uiBootstrap'),
    path('ui/buttons/', views.uiButtons, name='uiButtons'),
    path('ui/card/', views.uiCard, name='uiCard'),
    path('ui/icons/', views.uiIcons, name='uiIcons'),
    path('ui/modal-notifications/', views.uiModalNotifications, name='uiModalNotifications'),
    path('ui/typography/', views.uiTypography, name='uiTypography'),
    path('ui/tabs-accordions/', views.uiTabsAccordions, name='uiTabsAccordions'),
    path('form/elements/', views.formElements, name='formElements'),
    path('form/plugins/', views.formPlugins, name='formPlugins'),
    path('form/wizards/', views.formWizards, name='formWizards'),
    path('table/elements/', views.tableElements, name='tableElements'),
    path('table/plugins/', views.tablePlugins, name='tablePlugins'),
    path('chart/js/', views.chartJs, name='chartJs'),
    path('chart/apex/', views.chartApex, name='chartApex'),
    path('map/', views.map, name='map'),
    path('layout/starter', views.layoutStarter, name='layoutStarter'),
    path('layout/fixed-footer', views.layoutFixedFooter, name='layoutFixedFooter'),
    path('layout/full-height', views.layoutFullHeight, name='layoutFullHeight'),
    path('layout/full-width', views.layoutFullWidth, name='layoutFullWidth'),
    path('layout/boxed-layout', views.layoutBoxedLayout, name='layoutBoxedLayout'),
    path('layout/collapsed-sidebar', views.layoutCollapsedSidebar, name='layoutCollapsedSidebar'),
    path('layout/top-nav', views.layoutTopNav, name='layoutTopNav'),
    path('layout/mixed-nav', views.layoutMixedNav, name='layoutMixedNav'),
    path('layout/mixed-nav-boxed-layout', views.layoutMixedNavBoxedLayout, name='layoutMixedNavBoxedLayout'),
    path('page/scrum-board', views.pageScrumBoard, name='pageScrumBoard'),
    path('page/product', views.pageProduct, name='pageProduct'),
    path('page/product-details', views.pageProductDetails, name='pageProductDetails'),
    path('page/order', views.pageOrder, name='pageOrder'),
    path('page/groups', views.pageGroups, name='pageGroups'),

    path('page/order-details', views.pageOrderDetails, name='pageOrderDetails'),
    path('page/gallery', views.pageGallery, name='pageGallery'),
    path('page/search-results', views.pageSearchResults, name='pageSearchResults'),
    path('page/coming-soon', views.pageComingSoon, name='pageComingSoon'),
    path('page/error', views.pageError, name='pageError'),
    path('', views.pageLogin, name='pageLogin'),
    path('page/register', views.pageRegister, name='pageRegister'),
    path('page/messenger', views.pageMessenger, name='pageMessenger'),
    path('page/data-management', views.pageDataManagement, name='pageDataManagement'),
    path('page/file-manager', views.pageFileManager, name='pageFileManager'),
    path('page/pricing', views.pagePricing, name='pagePricing'),
    path('profile/', views.profile, name='profile'),
    path('calendar/', views.calendar, name='calendar'),
    path('settings/', views.settings, name='settings'),
    path('helper/', views.helper, name='helper')
]