from django.conf.urls import include, url
from django.contrib import admin
from samples import views, models

from haystack.generic_views import SearchView
from samples.forms import RawSearchForm

urlpatterns = [
    url(r'^$', views.index, name='index'),
#
    url(r'^sample/$', views.sample_index, name='sample_index'),
    url(r'^sample/samples_table_form/$', views.samples_table_form, name="samples_table_form"),
    url(r'^sample/add/$', views.SampleCreate.as_view(), name='sample_create'),
    url(r'^sample/(?P<pk>\w+)/$', views.sample_detail, name='sample_detail'),
    url(r'^sample/(?P<pk>\w+)/edit/$', views.SampleEdit.as_view(), name='sample_edit'),
    url(r'^sample/(?P<pk>\w+)/delete/$', views.SampleDelete.as_view(), name='sample_delete'),
    url(r'^sample/(?P<pk>\w+)/attach/$', views.attach_file, {"model": models.Sample}, name='sample_attachfile'),
    url(r'^sample/(?P<pk>\w+)/exportcsv/$', views.export_sample_to_csv, name='sample_export_csv'),
#
    url(r'^c14/$', views.c14_index, name='c14_index'),
    url(r'^c14/add/$', views.C14Create.as_view(), name='c14_create'),
    url(r'^c14/(?P<slug>[-\w]+)/edit/$', views.C14Edit.as_view(), name='c14_edit'),
#
    url(r'^samplegroup/$', views.samplegroup_index, name='samplegroup_index'),
    url(r'^samplegroup/add/$', views.SampleGroupCreate.as_view(), name='samplegroup_create'),
    url(r'^samplegroup/(?P<pk>\w+)/$', views.samplegroup_detail, name='samplegroup_detail'),
    url(r'^samplegroup/(?P<pk>\w+)/edit/$', views.SampleGroupEdit.as_view(), name='samplegroup_edit'),
    url(r'^samplegroup/(?P<pk>\w+)/delete/$', views.SampleGroupDelete.as_view(), name='samplegroup_delete'),
#
    url(r'^permit/$', views.permit_index, name='permit_index'),
    url(r'^permit/add/$', views.PermitCreate.as_view(), name='permit_create'),
    url(r'^permit/(?P<pk>\w+)/$', views.permit_detail, name='permit_detail'),
    url(r'^permit/(?P<pk>\w+)/edit/$', views.PermitEdit.as_view(), name='permit_edit'),
    url(r'^permit/(?P<pk>\w+)/delete/$', views.PermitDelete.as_view(), name='permit_delete'),
    url(r'^permit/(?P<pk>\w+)/attach/$', views.attach_file, {"model": models.Permit}, name='permit_attachfile'),
#
    url(r'^organism/$', views.organism_index, name='organism_index'),
    url(r'^organism/add/$', views.OrganismCreate.as_view(), name='organism_create'),
    url(r'^organism/(?P<pk>\w+)/$', views.organism_detail, name='organism_detail'),
    url(r'^organism/(?P<pk>\w+)/edit/$', views.OrganismEdit.as_view(), name='organism_edit'),
    url(r'^organism/(?P<pk>\w+)/delete/$', views.OrganismDelete.as_view(), name='organism_delete'),
#
    url(r'^project/$', views.project_index, name='project_index'),
    url(r'^project/add/$', views.ProjectCreate.as_view(), name='project_create'),
    url(r'^project/(?P<pk>\w+)/$', views.project_detail, name='project_detail'),
    url(r'^project/(?P<pk>\w+)/edit/$', views.ProjectEdit.as_view(), name='project_edit'),
    url(r'^project/(?P<pk>\w+)/delete/$', views.ProjectDelete.as_view(), name='project_delete'),
    url(r'^project/(?P<pk>\w+)/attach/$', views.attach_file, {"model": models.Project}, name='project_attachfile'),
#
    url(r'^extraction/$', views.extraction_index, name='extraction_index'),
    url(r'^extraction/add/$', views.ExtractionCreate.as_view(), name='extraction_create'),
    url(r'^extraction/(?P<pk>\w+)/$', views.extraction_detail, name='extraction_detail'),
    url(r'^extraction/(?P<pk>\w+)/edit/$', views.ExtractionEdit.as_view(), name='extraction_edit'),
    url(r'^extraction/(?P<pk>\w+)/delete/$', views.ExtractionDelete.as_view(), name='extraction_delete'),
    url(r'^extraction/(?P<pk>\w+)/addresult/$', views.extraction_addresult, name='extraction_addresult'),
    url(r'^extraction/(?P<pk>\w+)/attach/$', views.attach_file, {"model": models.Extraction}, name='extraction_attachfile'),
    url(r'^extractresult/(?P<pk>\w+)/edit/$', views.ExtractResultEdit.as_view(), name='extractresult_edit'),
#
    url(r'^amplification/$', views.amplification_index, name='amplification_index'),
    url(r'^amplification/add/$', views.AmplificationCreate.as_view(), name='amplification_create'),
    url(r'^amplification/(?P<pk>\w+)/$', views.amplification_detail, name='amplification_detail'),
    url(r'^amplification/(?P<pk>\w+)/edit/$', views.AmplificationEdit.as_view(), name='amplification_edit'),
    url(r'^amplification/(?P<pk>\w+)/delete/$', views.AmplificationDelete.as_view(), name='amplification_delete'),
    url(r'^amplification/(?P<pk>\w+)/addresult/$', views.amplification_addresult, name='amplification_addresult'),
    url(r'^amplification/(?P<pk>\w+)/attach/$', views.attach_file, {"model": models.Amplification}, name='amplification_attachfile'),
    url(r'^amplificationresult/(?P<pk>\w+)/edit/$', views.AmplificationResultEdit.as_view(), name='amplificationresult_edit'),
#
    url(r'^enrichment/$', views.enrichment_index, name='enrichment_index'),
    url(r'^enrichment/add/$', views.EnrichmentCreate.as_view(), name='enrichment_create'),
    url(r'^enrichment/(?P<pk>\w+)/$', views.enrichment_detail, name='enrichment_detail'),
    url(r'^enrichment/(?P<pk>\w+)/edit/$', views.EnrichmentEdit.as_view(), name='enrichment_edit'),
    url(r'^enrichment/(?P<pk>\w+)/delete/$', views.EnrichmentDelete.as_view(), name='enrichment_delete'),
    url(r'^enrichment/(?P<pk>\w+)/addresult/$', views.enrichment_addresult, name='enrichment_addresult'),
    url(r'^enrichment/(?P<pk>\w+)/attach/$', views.attach_file, {"model": models.Enrichment}, name='enrichment_attachfile'),
    url(r'^enrichmentresult/(?P<pk>\w+)/edit/$', views.EnrichmentResultEdit.as_view(), name='enrichmentresult_edit'),
#
    url(r'^sequence/$', views.sequence_index, name='sequence_index'),
    url(r'^sequence/add/$', views.SequenceCreate.as_view(), name='sequence_create'),
    url(r'^sequence/(?P<pk>\w+)/$', views.sequence_detail, name='sequence_detail'),
    url(r'^sequence/(?P<pk>\w+)/edit/$', views.SequenceEdit.as_view(), name='sequence_edit'),
    url(r'^sequence/(?P<pk>\w+)/delete/$', views.SequenceDelete.as_view(), name='sequence_delete'),
#
    url(r'^file/$', views.file_index, name='file_index'),
#
    url(r'^admin/', include(admin.site.urls)),
    url('^', include('django.contrib.auth.urls')),
    url(r'^myaccount/$', views.UserEdit.as_view(), name="myaccount"),
#
    url(r'^usergroup/$', views.usergroup_index, name='usergroup_index'),
    url(r'^usergroup/add/$', views.UserGroupAdd.as_view(), name='usergroup_create'),
    url(r'^usergroup/(?P<pk>\w+)/$', views.usergroup_detail, name='usergroup_detail'),
    url(r'^usergroup/(?P<pk>\w+)/edit/$', views.UserGroupEdit.as_view(), name='usergroup_edit'),
    url(r'^usergroup/(?P<pk>\w+)/delete/$', views.UserGroupDelete.as_view(), name='usergroup_delete'),
#
    url(r'^upload/samples/$', views.upload_samples, name='upload_samples'),
    url(r'^upload/c14/$', views.upload_c14, name='upload_c14'),
    url(r'^upload/samplegroups/$', views.upload_samplegroups, name='upload_samplegroups'),
#
    url(r'^upload_file/$', views.upload_file, name='upload_file'),
    url(r'^download_file/(?P<fileid>\w+)$', views.download_file, name="download_file"),
#
    url(r'^search/', views.MySearchView.as_view(), name='search'),
    url(r'^ajax/search/', views.search, name='ajax_search'),
#
    url(r'^ajax/delete_extractresult/(?P<result_id>\w+)/$', views.delete_extractresult, name="delete_extractresult"),
    url(r'^ajax/delete_amplificationresult/(?P<result_id>\w+)/$', views.delete_amplificationresult, name="delete_amplificationresult"),
    url(r'^ajax/delete_enrichmentresult/(?P<result_id>\w+)/$', views.delete_enrichmentresult, name="delete_enrichmentresult"),
    url(r'^ajax/delete_c14/(?P<slug>[-\w]+)/$', views.delete_c14, name="delete_c14"),
    url(r'^ajax/delete_file/(?P<file_id>\w+)/$', views.delete_file, name="delete_file"),
#
]
