import datetime
from haystack import indexes
from samples.models import Sample, Extraction, C14, Project

class SampleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    acad_num = indexes.IntegerField(model_attr="acad_num")
    other_num = indexes.CharField(model_attr="other_num")
    category = indexes.CharField(model_attr="category")
    extracted_by_date = indexes.CharField(model_attr="extracted_by_date")
    acad_location = indexes.CharField(model_attr="acad_location")
    date_of_entry = indexes.DateField(model_attr="date_of_entry", null=True)
    abc_num = indexes.CharField(model_attr="abc_num")
    organism = indexes.CharField(model_attr="organism", null=True)
    common_name = indexes.CharField(model_attr="common_name")
    genus = indexes.CharField(model_attr="genus")
    species = indexes.CharField(model_attr="species")
    subspecies = indexes.CharField(model_attr="subspecies")
    notes = indexes.CharField(model_attr="notes")
    region = indexes.CharField(model_attr="region")
    country = indexes.CharField(model_attr="country")
    state = indexes.CharField(model_attr="state")
    locality = indexes.CharField(model_attr="locality")
    location = indexes.CharField(model_attr="location")
    collection_date = indexes.DateField(model_attr="collection_date", null=True)
    collected_by = indexes.CharField(model_attr="collected_by")
    quality = indexes.CharField(model_attr="quality")
    museum = indexes.CharField(model_attr="museum")
    museum_num = indexes.CharField(model_attr="museum_num")
    sampled_by = indexes.CharField(model_attr="sampled_by")
    sample_date = indexes.DateField(model_attr="sample_date", null=True)
    mismatch_reason = indexes.CharField(model_attr="mismatch_reason")
    sample_repat = indexes.CharField(model_attr="sample_repat")
    extracted = indexes.BooleanField()
    extracted_by = indexes.CharField()
    carbon_date = indexes.CharField()
    project = indexes.CharField()

    def get_model(self):
        return Sample

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

    def prepare_organism(self, obj):
        if obj.organism:
            return "{} {} {}".format(obj.organism.id, obj.organism.get_long_name(), obj.organism.common)

    def prepare_extracted(self, obj):
        if Extraction.objects.filter(extractresult__sample=obj.acad_num):
            return True
        else:
            return False

    def prepare_extracted_by(self, obj):
        names = []
        extractions = Extraction.objects.filter(extractresult__sample=obj.acad_num)
        for e in extractions:
            if e.extracted_by not in names:
                names.append(e.extracted_by)
        return names

    def prepare_carbon_date(self, obj):
        dates = []
        c14_list = C14.objects.filter(sample=obj.acad_num)
        for c14 in c14_list:
            dates.append(str(c14.date))
        return dates

    def prepare_project(self, obj):
        titles = []
        projects = Project.objects.filter(sample=obj.acad_num)
        for p in projects:
            if p.title not in titles:
                titles.append(p.title)
        return titles
