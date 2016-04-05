#from django.forms import ModelForm
from django import forms
from datetime import date
from crispy_forms.helper import FormHelper

from samples.models import Sample, Organism, AQISSampleGroup, Permit, Project, Extraction, ExtractResult, C14, Amplification, AmplificationResult, Enrichment, EnrichmentResult, Sequence

class SampleAddForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = "__all__"
        widgets = {
            "date_of_entry": forms.DateInput(attrs={'class': 'datepicker'}),
            "collection_date": forms.DateInput(attrs={'class': 'datepicker'}),
            "sample_date": forms.DateInput(attrs={'class': 'datepicker'})
        }

    def __init__(self, *args, **kwargs):
        super(SampleAddForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

class SampleEditForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = "__all__"
        widgets = {
            "date_of_entry": forms.DateInput(attrs={'class': 'datepicker'}),
            "collection_date": forms.DateInput(attrs={'class': 'datepicker'}),
            "sample_date": forms.DateInput(attrs={'class': 'datepicker'})
        }

    def __init__(self, *args, **kwargs):
        super(SampleEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

class SampleDeleteForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = "__all__"

def _clean_group_num(data):
    try:
        data = int(data)
    except ValueError:
        raise forms.ValidationError("Only number is allowed")
    return data

class SampleGroupAddForm(forms.ModelForm):
    class Meta:
        model = AQISSampleGroup
        fields = "__all__"
        widgets = {"accession_date": forms.DateInput(attrs={'class': 'datepicker'})}

    def __init__(self, *args, **kwargs):
        super(SampleGroupAddForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

    def clean_group_num(self):
        return _clean_group_num(self.cleaned_data['group_num'])

class SampleGroupEditForm(forms.ModelForm):
    class Meta:
        model = AQISSampleGroup
        fields = "__all__"
        widgets = {"accession_date": forms.DateInput(attrs={'class': 'datepicker'})}

    def __init__(self, *args, **kwargs):
        super(SampleGroupEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

    def clean_group_num(self):
        return _clean_group_num(self.cleaned_data['group_num'])

class SampleGroupDeleteForm(forms.ModelForm):
    class Meta:
        model = AQISSampleGroup
        fields = "__all__"

class PermitAddForm(forms.ModelForm):
    class Meta:
        model = Permit
        fields = "__all__"
        widgets = {
            "valid_from": forms.DateInput(attrs={'class': 'datepicker'}),
            "valid_to": forms.DateInput(attrs={'class': 'datepicker'}),
            "active_from": forms.DateInput(attrs={'class': 'datepicker'})
        }

    def __init__(self, *args, **kwargs):
        super(PermitAddForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

class PermitEditForm(forms.ModelForm):
    class Meta:
        model = Permit
        fields = "__all__"
        widgets = {
            "valid_from": forms.DateInput(attrs={'class': 'datepicker'}),
            "valid_to": forms.DateInput(attrs={'class': 'datepicker'}),
            "active_from": forms.DateInput(attrs={'class': 'datepicker'})
        }

    def __init__(self, *args, **kwargs):
        super(PermitEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

class PermitDeleteForm(forms.ModelForm):
    class Meta:
        model = Permit
        fields = "__all__"

class ProjectAddForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProjectAddForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

class ProjectEditForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProjectEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

class ProjectDeleteForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"

class OrganismAddForm(forms.ModelForm):
    class Meta:
        model = Organism
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(OrganismAddForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

class OrganismEditForm(forms.ModelForm):
    class Meta:
        model = Organism
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(OrganismEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

class OrganismDeleteForm(forms.ModelForm):
    class Meta:
        model = Organism
        fields = "__all__"

class ExtractionAddForm(forms.ModelForm):
    class Meta:
        model = Extraction
        fields = "__all__"
        widgets = {"date": forms.DateInput(attrs={'class': 'datepicker'})}

    def __init__(self, *args, **kwargs):
        super(ExtractionAddForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

class ExtractionEditForm(forms.ModelForm):
    class Meta:
        model = Extraction
        fields = "__all__"
        widgets = {"date": forms.DateInput(attrs={'class': 'datepicker'})}

    def __init__(self, *args, **kwargs):
        super(ExtractionEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

class ExtractionDeleteForm(forms.ModelForm):
    class Meta:
        model = Extraction
        fields = "__all__"

class ExtractResultEditForm(forms.ModelForm):
    sample = forms.IntegerField(label="Sample number", widget=forms.TextInput(attrs={'readonly':'readonly'}))
    starting = forms.CharField(label="Starting material", required=False)
    final_vol = forms.CharField(label="Final DNA volume (in ul)", required=False)
    dna_yield = forms.DecimalField(label="DNA yield", required=False, max_digits=5, decimal_places=2)
    from django.db.models.fields import BLANK_CHOICE_DASH
    quant_method = forms.ChoiceField(label="Quantification method", choices=BLANK_CHOICE_DASH + list(ExtractResult.QUANT_METHODS), required=False)

    class Meta:
        model = ExtractResult
        fields = ["sample", "starting", "final_vol", "dna_yield", "quant_method"]

    def __init__(self, *args, **kwargs):
        super(ExtractResultEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

    def clean_sample(self):
        from django.core.exceptions import ObjectDoesNotExist
        cleaned_data = super(ExtractResultEditForm, self).clean()

        try:
            Sample.objects.get(acad_num=cleaned_data["sample"])
        except ObjectDoesNotExist:
            raise forms.ValidationError("Sample number {} doesn't exist".format(cleaned_data["sample"]))

        return Sample.objects.get(acad_num=cleaned_data["sample"])

class ExtractionAddResultForm(forms.Form):
    sample = forms.IntegerField(label="Sample number")
    starting = forms.CharField(label="Starting material", required=False)
    final_vol = forms.CharField(label="Final DNA volume (in ul)", required=False)
    dna_yield = forms.DecimalField(label="DNA yield", required=False, max_digits=5, decimal_places=2)
    from django.db.models.fields import BLANK_CHOICE_DASH
    quant_method = forms.ChoiceField(label="Quantification method", choices=BLANK_CHOICE_DASH + list(ExtractResult.QUANT_METHODS), required=False)

    def __init__(self, *args, **kwargs):
        super(ExtractionAddResultForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

    def clean_sample(self):
        from django.core.exceptions import ObjectDoesNotExist
        cleaned_data = super(ExtractionAddResultForm, self).clean()

        try:
            Sample.objects.get(acad_num=cleaned_data["sample"])
        except ObjectDoesNotExist:
            raise forms.ValidationError("Sample number {} doesn't exist".format(cleaned_data["sample"]))

        return cleaned_data["sample"]

class AmplificationAddForm(forms.ModelForm):
    class Meta:
        model = Amplification
        fields = "__all__"
        widgets = {"date": forms.DateInput(attrs={'class': 'datepicker'})}

    def __init__(self, *args, **kwargs):
        super(AmplificationAddForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

class AmplificationEditForm(forms.ModelForm):
    class Meta:
        model = Amplification
        fields = "__all__"
        widgets = {"date": forms.DateInput(attrs={'class': 'datepicker'})}

    def __init__(self, *args, **kwargs):
        super(AmplificationEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

class AmplificationDeleteForm(forms.ModelForm):
    class Meta:
        model = Amplification
        fields = "__all__"

class AmplificationAddResultForm(forms.Form):
    extractresult = forms.CharField(label="Extract result id")
    dna_yield = forms.DecimalField(label="DNA yield", required=False, max_digits=5, decimal_places=2)
    quant_method = forms.CharField(label="Quantification method", required=False)

    def __init__(self, *args, **kwargs):
        super(AmplificationAddResultForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

    def clean_extractresult(self):
        from django.core.exceptions import ObjectDoesNotExist
        self.cleaned_data = super(AmplificationAddResultForm, self).clean()

        try:
            ExtractResult.objects.get(id=self.cleaned_data["extractresult"])
        except ObjectDoesNotExist:
            raise forms.ValidationError("Extract result {} doesn't exist".format(self.cleaned_data["extractresult"]))

        return self.cleaned_data["extractresult"]

class AmplificationResultEditForm(forms.ModelForm):
    extractresult = forms.CharField(label="Extract result id", widget=forms.TextInput(attrs={'readonly':'readonly'}))
    dna_yield = forms.DecimalField(label="DNA yield", required=False, max_digits=5, decimal_places=2)
    quant_method = forms.CharField(label="Quantification method", required=False)

    class Meta:
        model = AmplificationResult
        fields = ["extractresult", "dna_yield", "quant_method"]

    def __init__(self, *args, **kwargs):
        super(AmplificationResultEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

    def clean_extractresult(self):
        from django.core.exceptions import ObjectDoesNotExist
        cleaned_data = super(AmplificationResultEditForm, self).clean()

        try:
            ExtractResult.objects.get(id=cleaned_data["extractresult"])
        except ObjectDoesNotExist:
            raise forms.ValidationError("Extract result {} doesn't exist".format(cleaned_data["extractresult"]))

        return ExtractResult.objects.get(id=cleaned_data["extractresult"])

class EnrichmentAddForm(forms.ModelForm):
    class Meta:
        model = Enrichment
        fields = "__all__"
        widgets = {"date": forms.DateInput(attrs={'class': 'datepicker'})}

    def __init__(self, *args, **kwargs):
        super(EnrichmentAddForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

class EnrichmentEditForm(forms.ModelForm):
    class Meta:
        model = Enrichment
        fields = "__all__"
        widgets = {"date": forms.DateInput(attrs={'class': 'datepicker'})}

    def __init__(self, *args, **kwargs):
        super(EnrichmentEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

class EnrichmentDeleteForm(forms.ModelForm):
    class Meta:
        model = Enrichment
        fields = "__all__"

class EnrichmentAddResultForm(forms.Form):
    ampresult = forms.CharField(label="Amplification result id")
    enrich_type = forms.CharField(label="Enrichment type", required=False)
    bait_detail = forms.CharField(label="Bait detail", required=False)
    dna_yield = forms.DecimalField(label="DNA yield", required=False, max_digits=5, decimal_places=2)
    quant_method = forms.CharField(label="Quantification method", required=False)

    def __init__(self, *args, **kwargs):
        super(EnrichmentAddResultForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

    def clean_ampresult(self):
        from django.core.exceptions import ObjectDoesNotExist
        self.cleaned_data = super(EnrichmentAddResultForm, self).clean()

        try:
            AmplificationResult.objects.get(id=self.cleaned_data["ampresult"])
        except ObjectDoesNotExist:
            raise forms.ValidationError("Amplification result {} doesn't exist".format(self.cleaned_data["ampresult"]))

        return self.cleaned_data["ampresult"]

class EnrichmentResultEditForm(forms.ModelForm):
    ampresult = forms.CharField(label="Amplification result id", widget=forms.TextInput(attrs={'readonly':'readonly'}))
    enrich_type = forms.CharField(label="Enrichment type", required=False)
    bait_detail = forms.CharField(label="Bait detail", required=False)
    dna_yield = forms.DecimalField(label="DNA yield", required=False, max_digits=5, decimal_places=2)
    quant_method = forms.CharField(label="Quantification method", required=False)

    class Meta:
        model = EnrichmentResult
        fields = ["ampresult", "enrich_type", "bait_detail", "dna_yield", "quant_method"]

    def __init__(self, *args, **kwargs):
        super(EnrichmentResultEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

    def clean_ampresult(self):
        from django.core.exceptions import ObjectDoesNotExist
        cleaned_data = super(EnrichmentResultEditForm, self).clean()

        try:
            AmplificationResult.objects.get(id=cleaned_data["ampresult"])
        except ObjectDoesNotExist:
            raise forms.ValidationError("Amplification result {} doesn't exist".format(cleaned_data["ampresult"]))

        return AmplificationResult.objects.get(id=cleaned_data["ampresult"])

class SequenceAddForm(forms.ModelForm):
    class Meta:
        model = Sequence
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(SequenceAddForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

class SequenceEditForm(forms.ModelForm):
    class Meta:
        model = Sequence
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(SequenceEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

class SequenceDeleteForm(forms.ModelForm):
    class Meta:
        model = Sequence
        fields = "__all__"

class C14AddForm(forms.ModelForm):
    class Meta:
        model = C14
        exclude = ["slug"]

    def __init__(self, *args, **kwargs):
        super(C14AddForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

class C14EditForm(forms.ModelForm):
    class Meta:
        model = C14
        exclude = ["slug"]

    def __init__(self, *args, **kwargs):
        super(C14EditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

class UploadSamplesFileForm(forms.Form):
    file = forms.FileField(label="Upload your samples source file")
    force_update = forms.BooleanField(label="Update samples that already exist", required=False, initial=False)
    makeagroup = forms.BooleanField(label="Make a new AQIS group from these samples?", required=False, initial=False)
    group_description = forms.CharField(label="Description for group", required=False)
    group_origin = forms.CharField(label="Country of origin", required=False)

    def __init__(self, *args, **kwargs):
        super(UploadSamplesFileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

class UploadC14FileForm(forms.Form):
    file = forms.FileField(label="Upload your C14 source file")

    def __init__(self, *args, **kwargs):
        super(UploadC14FileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

class UploadSampleGroupFileForm(forms.Form):
    file = forms.FileField(label="Upload your groups source file")

    def __init__(self, *args, **kwargs):
        super(UploadSampleGroupFileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

class UploadFileForm(forms.Form):
    file = forms.FileField(label="Upload your file")
    next = forms.CharField(label="Redirect page", required=False)

from haystack.forms import SearchForm
class RawSearchForm(SearchForm):
    """ This is just a copy-paste from django-haystack's SearchForm, but using
    SearchQuerySet's raw_search() rather than auto_query(). """
    def search(self):
        if not self.is_valid():
            return self.no_query_found()

        if not self.cleaned_data.get('q'):
            return self.no_query_found()

        sqs = self.searchqueryset.raw_search(self.cleaned_data['q'])

        if self.load_all:
            sqs = sqs.load_all()

        return sqs

    def __init__(self, *args, **kwargs):
        super(RawSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.disable_csrf = True

from django.contrib.auth.models import User, Group
class UserEditForm(forms.ModelForm):
    groups = forms.ModelMultipleChoiceField(label="Groups", queryset=Group.objects.all(), required=False)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "groups"]

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

class UserGroupAddForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(label="Users", queryset=User.objects.all(), required=False, widget=forms.SelectMultiple(attrs={'size': '10'}))
    class Meta:
        model = Group
        fields = ["name", "users"]

    def __init__(self, *args, **kwargs):
        super(UserGroupAddForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

class UserGroupEditForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(label="Users", queryset=User.objects.all(), required=False, widget=forms.SelectMultiple(attrs={'size': '10'}))
    class Meta:
        model = Group
        fields = ["name", "users"]

    def __init__(self, *args, **kwargs):
        super(UserGroupEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

class UserGroupDeleteForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = "__all__"
