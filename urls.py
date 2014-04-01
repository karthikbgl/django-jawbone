from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('django_jawbone.views',
	
	url(r'authorize/jawbone/$', 
			'authorize_jawbone', 
			name='authorize-jawbone'),

	url(r'authorize/jawbone/complete/$',
			'authorize_jawbone_complete', 
			name='authorize-jawbone-complete')
)
