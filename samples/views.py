from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.forms.models import model_to_dict
import json

from django.db.models import Q

from samples.models import Sample, Organism, Project, FileAttachment, AQISSampleGroup, Permit, Extraction, ExtractResult, Amplification, AmplificationResult, Enrichment, EnrichmentResult, Sequence, C14
import samples.forms

def is_topbuttons_required(num):
    """Bridge templates and settings in terms if display top buttons"""
    if hasattr(settings, 'TOP_BUTTONS_REQUIRED'):
        return num >= settings.TOP_BUTTONS_REQUIRED
    return False

def index(request):
    return render(request, "index.html")

def sample_index(request):
    default_step = 100

    if "step" in request.GET and int(request.GET["step"]) > 0:
        step = int(request.GET["step"])
    else:
        step = default_step

    start = 0
    end = step
    page = 1

    if "page" in request.GET and int(request.GET["page"]) > 0:
        page = int(request.GET["page"])
        start = start + ((page-1) * step)
        end = end + ((page-1) * step)

    context = {"sample_list": Sample.objects.all()[start:end]}
    context["page"] = page

    import math
    numpages = int(math.ceil(len(Sample.objects.all()) / step)) # Yuck!
    context["numpages"] = numpages
    pages = range(1, numpages+1)

    if step != default_step:
        context["step"] = step
    if page > 1:
        context["prevpage"] = page - 1
    if page < numpages:
        context["nextpage"] = page + 1

    pagedict={}
    for p in pages:
        pagedict[p] = [(p-1)*step+1, ((p-1)*step)+step]
        if p == numpages:
            pagedict[p][1] = len(Sample.objects.all())
    context["pagedict"] = pagedict
    context["topbuttons"] = is_topbuttons_required(len(context["sample_list"]))

    return render(request, "sample/index.html", context)

def sample_detail(request, pk):
    sample = get_object_or_404(Sample, acad_num=pk)
    if sample.category == "extractcontrol":
        extraction_list = Extraction.objects.filter(extract_control=pk).distinct()
    else:
        extraction_list = Extraction.objects.filter(extractresult__sample=pk).distinct()
    c14_list = C14.objects.filter(sample=pk)
    amp_list = AmplificationResult.objects.filter(extractresult__sample__acad_num=sample.acad_num)
    amps = [rslt.amplification for rslt in amp_list]
    enr_list = EnrichmentResult.objects.filter(ampresult__extractresult__sample__acad_num=sample.acad_num)
    enrs = [rslt.enrichment for rslt in enr_list]
    seq_list = Sequence.objects.filter(Q(amplification__in=amps) | Q(enrichment__in=enrs))

    context = {"sample": sample, "extraction_list": extraction_list, "c14_list": c14_list,
               "amplification_list": frozenset(amps),
               "enrichment_list": frozenset(enrs),
               "sequence_list": seq_list
              }
    return render(request, "sample/detail.html", context)

def samplegroup_index(request):
    context = {"samplegroup_list": AQISSampleGroup.objects.all()}
    context["topbuttons"] = is_topbuttons_required(len(context["samplegroup_list"]))
    return render(request, "samplegroup/index.html", context)

def samplegroup_detail(request, pk):
    samplegroup = get_object_or_404(AQISSampleGroup, group_num=pk)
    context = {"samplegroup": samplegroup}
    return render(request, "samplegroup/detail.html", context)

def c14_index(request):
    context = {"c14_list": C14.objects.all().order_by("-sample")}
    context["topbuttons"] = is_topbuttons_required(len(context["c14_list"]))
    return render(request, "c14/index.html", context)

def permit_index(request):
    context = {"permit_list": Permit.objects.all()}
    context["topbuttons"] = is_topbuttons_required(len(context["permit_list"]))
    return render(request, "permit/index.html", context)

def permit_detail(request, pk):
    permit = get_object_or_404(Permit, pk=pk)
    context = {"permit": permit}
    return render(request, "permit/detail.html", context)

def organism_index(request):
    context = {"organism_list": Organism.objects.all().order_by("genus")}
    return render(request, "organism/index.html", context)

def organism_detail(request, pk):
    organism = get_object_or_404(Organism, id=pk)
    editform = samples.forms.OrganismEditForm(initial=model_to_dict(organism))
    context = {"organism": organism, "editform": editform}
    return render(request, "organism/detail.html", context)

def project_index(request):
    project_list = Project.objects.all()

    user_projects = []
    group_projects = {}
    if request.user.is_authenticated():
        user_projects = Project.objects.filter(user=request.user)
        user_groups = request.user.groups.all()
        for group in user_groups:
            temp = []
            for project in Project.objects.filter(group=group):
                temp.append(project)
            group_projects[group] = temp

    context = {"project_list": project_list, "user_projects": user_projects, "group_projects": group_projects}
    return render(request, "project/index.html", context)

def project_detail(request, pk):
    project = get_object_or_404(Project, id=pk)
    sample_list = Sample.objects.filter(project=project)
    extraction_list = Extraction.objects.filter(extractresult__sample=sample_list).distinct()
    context = {"project": project, "sample_list": sample_list, "extraction_list": extraction_list}
    return render(request, "project/detail.html", context)

def extraction_index(request):
    context = {"extraction_list": Extraction.objects.all()}
    context["topbuttons"] = is_topbuttons_required(len(context["extraction_list"]))
    return render(request, "extraction/index.html", context)

def extraction_detail(request, pk):
    extraction = get_object_or_404(Extraction, id=pk)
    results = ExtractResult.objects.filter(extraction=extraction).order_by("sample")
    addresultform = samples.forms.ExtractionAddResultForm()
    context = {"extraction": extraction, "results": results, "addresultform": addresultform }
    return render(request, "extraction/detail.html", context)

def amplification_index(request):
    context = {"amplification_list": Amplification.objects.all()}
    context["topbuttons"] = is_topbuttons_required(len(context["amplification_list"]))
    return render(request, "amplification/index.html", context)

def amplification_detail(request, pk):
    amplification = get_object_or_404(Amplification, id=pk)
    results = AmplificationResult.objects.filter(amplification=amplification).order_by("extractresult")
    sequence_list = Sequence.objects.filter(amplification=pk)
    addresultform = samples.forms.AmplificationAddResultForm()
    context = {"amplification": amplification, "results": results, "sequence_list": sequence_list, "addresultform": addresultform }
    return render(request, "amplification/detail.html", context)

def enrichment_index(request):
    context = {"enrichment_list": Enrichment.objects.all()}
    context["topbuttons"] = is_topbuttons_required(len(context["enrichment_list"]))
    return render(request, "enrichment/index.html", context)

def enrichment_detail(request, pk):
    enrichment = get_object_or_404(Enrichment, id=pk)
    results = EnrichmentResult.objects.filter(enrichment=enrichment).order_by("ampresult")
    sequence_list = Sequence.objects.filter(enrichment=pk)
    addresultform = samples.forms.EnrichmentAddResultForm()
    context = {"enrichment": enrichment, "results": results, "sequence_list": sequence_list, "addresultform": addresultform }
    return render(request, "enrichment/detail.html", context)

def sequence_index(request):
    context = {"sequence_list": Sequence.objects.all()}
    context["topbuttons"] = is_topbuttons_required(len(context["sequence_list"]))
    return render(request, "sequence/index.html", context)

def sequence_detail(request, pk):
    sequence = get_object_or_404(Sequence, id=pk)
    context = {"sequence": sequence }
    return render(request, "sequence/detail.html", context)

class SampleCreate(CreateView):
    model = Sample
    form_class = samples.forms.SampleAddForm
    template_name = "sample/sample_form.html"

class SampleEdit(UpdateView):
    model = Sample
    form_class = samples.forms.SampleEditForm
    template_name = "sample/sample_form.html"
    success_message = "Sample edited"

class SampleDelete(DeleteView):
    model = Sample
    form_class = samples.forms.SampleDeleteForm
    template_name = "sample/sample_delete.html"
    success_url = reverse_lazy("sample_index")

    def get_object(self, queryset=None):
        from django.core.exceptions import PermissionDenied
        obj = super(SampleDelete, self).get_object(queryset)
        if obj.is_extracted() and not self.request.user.is_superuser:
            raise PermissionDenied
        return obj

class SampleGroupCreate(CreateView):
    model = AQISSampleGroup
    form_class = samples.forms.SampleGroupAddForm
    template_name = "samplegroup/samplegroup_form.html"

class SampleGroupEdit(UpdateView):
    model = AQISSampleGroup
    form_class = samples.forms.SampleGroupEditForm
    template_name = "samplegroup/samplegroup_form.html"
    success_message = "Sample group edited"

class SampleGroupDelete(DeleteView):
    model = AQISSampleGroup
    form_class = samples.forms.SampleDeleteForm
    template_name = "samplegroup/samplegroup_delete.html"
    success_url = reverse_lazy("samplegroup_index")

class PermitCreate(CreateView):
    model = Permit
    form_class = samples.forms.PermitAddForm
    template_name = "permit/permit_form.html"

class PermitEdit(UpdateView):
    model = Permit
    form_class = samples.forms.PermitEditForm
    template_name = "permit/permit_form.html"
    success_message = "Permit edited"

class PermitDelete(DeleteView):
    model = Permit
    form_class = samples.forms.PermitDeleteForm
    template_name = "permit/permit_delete.html"
    success_url = reverse_lazy("permit_index")

class ProjectCreate(CreateView):
    model = Project
    form_class = samples.forms.ProjectAddForm
    template_name = "project/project_form.html"

class ProjectEdit(UpdateView):
    model = Project
    form_class = samples.forms.ProjectEditForm
    template_name = "project/project_form.html"

class ProjectDelete(DeleteView):
    model = Project
    form_class = samples.forms.ProjectDeleteForm
    template_name = "project/project_delete.html"
    success_url = reverse_lazy("project_index")

class OrganismCreate(CreateView):
    model = Organism
    form_class = samples.forms.OrganismAddForm
    template_name = "organism/organism_form.html"

#  Adapted from https://docs.djangoproject.com/en/1.8/topics/class-based-views/generic-editing/#ajax-example
from django.http import JsonResponse
class AjaxableResponseMixin(object):
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            from crispy_forms.utils import render_crispy_form
            data = { "errors": form.errors, "form_html": render_crispy_form(form) }
            return JsonResponse(data, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response

class OrganismEdit(AjaxableResponseMixin, UpdateView):
    model = Organism
    form_class = samples.forms.OrganismEditForm
    template_name = "organism/organism_form.html"
    success_message = "Organism edited"

class OrganismDelete(DeleteView):
    model = Organism
    form_class = samples.forms.OrganismDeleteForm
    template_name = "organism/organism_delete.html"
    success_url = reverse_lazy("organism_index")

class ExtractionCreate(CreateView):
    model = Extraction
    form_class = samples.forms.ExtractionAddForm
    template_name = "extraction/extraction_form.html"

    def get_initial(self):
        initial = super(ExtractionCreate, self).get_initial()
        from datetime import date
        initial["date"] = date.today()
        initial["extracted_by"] = "{} {}".format(self.request.user.first_name, self.request.user.last_name)
        return initial

class ExtractionEdit(UpdateView):
    model = Extraction
    form_class = samples.forms.ExtractionEditForm
    template_name = "extraction/extraction_form.html"

class ExtractionDelete(DeleteView):
    model = Extraction
    form_class = samples.forms.ExtractionDeleteForm
    template_name = "extraction/extraction_delete.html"
    success_url = reverse_lazy("extraction_index")

class ExtractResultEdit(UpdateView):
    model = ExtractResult
    form_class = samples.forms.ExtractResultEditForm
    template_name = "extractresult/extractresult_form.html"

class C14Create(CreateView):
    model = C14
    form_class = samples.forms.C14AddForm
    template_name = "c14/c14_form.html"
    success_url = reverse_lazy("c14_index")

class C14Edit(UpdateView):
    model = C14
    form_class = samples.forms.C14EditForm
    template_name = "c14/c14_form.html"
    success_url = reverse_lazy("c14_index")

class AmplificationCreate(CreateView):
    model = Amplification
    form_class = samples.forms.AmplificationAddForm
    template_name = "amplification/amplification_form.html"

    def get_initial(self):
        initial = super(AmplificationCreate, self).get_initial()
        from datetime import date
        initial["date"] = date.today()
        initial["prepared_by"] = "{} {}".format(self.request.user.first_name, self.request.user.last_name)
        return initial

class AmplificationEdit(UpdateView):
    model = Amplification
    form_class = samples.forms.AmplificationEditForm
    template_name = "amplification/amplification_form.html"

class AmplificationDelete(DeleteView):
    model = Amplification
    form_class = samples.forms.AmplificationDeleteForm
    template_name = "amplification/amplification_delete.html"
    success_url = reverse_lazy("amplification_index")

class AmplificationResultEdit(UpdateView):
    model = AmplificationResult
    form_class = samples.forms.AmplificationResultEditForm
    template_name = "amplificationresult/amplificationresult_form.html"

class EnrichmentCreate(CreateView):
    model = Enrichment
    form_class = samples.forms.EnrichmentAddForm
    template_name = "enrichment/enrichment_form.html"

    def get_initial(self):
        initial = super(EnrichmentCreate, self).get_initial()
        from datetime import date
        initial["date"] = date.today()
        initial["prepared_by"] = "{} {}".format(self.request.user.first_name, self.request.user.last_name)
        return initial

class EnrichmentEdit(UpdateView):
    model = Enrichment
    form_class = samples.forms.EnrichmentEditForm
    template_name = "enrichment/enrichment_form.html"

class EnrichmentDelete(DeleteView):
    model = Enrichment
    form_class = samples.forms.EnrichmentDeleteForm
    template_name = "enrichment/enrichment_delete.html"
    success_url = reverse_lazy("enrichment_index")

class EnrichmentResultEdit(UpdateView):
    model = EnrichmentResult
    form_class = samples.forms.EnrichmentResultEditForm
    template_name = "enrichmentresult/enrichmentresult_form.html"

class SequenceCreate(CreateView):
    model = Sequence
    form_class = samples.forms.SequenceAddForm
    template_name = "sequence/sequence_form.html"

class SequenceEdit(UpdateView):
    model = Sequence
    form_class = samples.forms.SequenceEditForm
    template_name = "sequence/sequence_form.html"

class SequenceDelete(DeleteView):
    model = Sequence
    form_class = samples.forms.SequenceDeleteForm
    template_name = "sequence/sequence_delete.html"
    success_url = reverse_lazy("sequence_index")

def extraction_addresult(request, pk):
    if request.method == "POST":
        form = samples.forms.ExtractionAddResultForm(request.POST)

        if form.is_valid():
            cleaned_data = form.cleaned_data

            result = ExtractResult()
            result.sample = Sample.objects.get(acad_num=cleaned_data["sample"])
            result.starting = cleaned_data["starting"]
            result.final_vol = cleaned_data["final_vol"]
            result.dna_yield = cleaned_data["dna_yield"]
            result.quant_method = cleaned_data["quant_method"]
            result.extraction = Extraction.objects.get(id=pk)

            import string
            suffixes = list(string.ascii_uppercase)

            count = 0
            while count < len(suffixes):
                result.id = "{}{}".format(result.sample.acad_num, suffixes[count])
                if not ExtractResult.objects.filter(id=result.id):
                    break
                else:
                    count = count + 1

            else:
                """ We went through all the suffixes and couldn't find an available samplenum+suffix combination, so generate some probably/hopefully unique id """
                import uuid
                result.id = "{}{}".format(result.sample.acad_num, str(uuid.uuid4())[0:8])

            result.save()

            if request.is_ajax():
                return JsonResponse({ "pk": result.pk })
            else:
                return HttpResponseRedirect(reverse_lazy("extraction_detail", kwargs={"pk": pk}))

        else:
            if request.is_ajax():
                data = { "errors": form.errors }
                return JsonResponse(data, status=400)
            else:
                print(form.errors) # debugging
                return HttpResponse("invalid form data")

    else:
        return HttpResponse("should only be POSTing to this view. wtf are you doing")

def amplification_addresult(request, pk):
    if request.method == "POST":
        form = samples.forms.AmplificationAddResultForm(request.POST)

        if form.is_valid():
            cleaned_data = form.cleaned_data

            result = AmplificationResult()
            result.extractresult = ExtractResult.objects.get(id=cleaned_data["extractresult"])
            result.dna_yield = cleaned_data["dna_yield"]
            result.quant_method = cleaned_data["quant_method"]
            result.amplification = Amplification.objects.get(id=pk)

            count = 1
            while count < 99:
                result.id = "{}_{}".format(result.extractresult.id, count)
                if not AmplificationResult.objects.filter(id=result.id):
                    break
                else:
                    count = count + 1

            else:
                """ We couldn't find an available extractid+suffix combination, so generate some probably/hopefully unique id """
                import uuid
                result.id = "{}_{}".format(result.extractresult.id, str(uuid.uuid4())[0:8])

            result.save()

            if request.is_ajax():
                return JsonResponse({ "pk": result.pk })
            else:
                return HttpResponseRedirect(reverse_lazy("amplification_detail", kwargs={"pk": pk}))

        else:
            if request.is_ajax():
                data = { "errors": form.errors }
                return JsonResponse(data, status=400)
            else:
                return HttpResponse("invalid form data")

    else:
        return HttpResponse("should only be POSTing to this view. wtf are you doing")

def enrichment_addresult(request, pk):
    if request.method == "POST":
        form = samples.forms.EnrichmentAddResultForm(request.POST)

        if form.is_valid():
            cleaned_data = form.cleaned_data

            result = EnrichmentResult()
            result.ampresult = AmplificationResult.objects.get(id=cleaned_data["ampresult"])
            result.enrich_type = cleaned_data["enrich_type"]
            result.bait_detail = cleaned_data["bait_detail"]
            result.dna_yield = cleaned_data["dna_yield"]
            result.quant_method = cleaned_data["quant_method"]
            result.enrichment = Enrichment.objects.get(id=pk)

            import string
            suffixes = list(string.ascii_lowercase)

            count = 0
            while count < len(suffixes):
                result.id = "{}{}".format(result.ampresult.id, suffixes[count])
                if not EnrichmentResult.objects.filter(id=result.id):
                    break
                else:
                    count = count + 1

            else:
                """ We couldn't find an available extractid+suffix combination, so generate some probably/hopefully unique id """
                import uuid
                result.id = "{}_{}".format(result.ampresult.id, str(uuid.uuid4())[0:8])

            result.save()

            if request.is_ajax():
                return JsonResponse({ "pk": result.pk })
            else:
                return HttpResponseRedirect(reverse_lazy("enrichment_detail", kwargs={"pk": pk}))

        else:
            if request.is_ajax():
                data = { "errors": form.errors }
                return JsonResponse(data, status=400)
            else:
                return HttpResponse("invalid form data")

    else:
        return HttpResponse("should only be POSTing to this view. wtf are you doing")

# ajaxy
def delete_extractresult(request, result_id):
    try:
        result = ExtractResult.objects.get(id=result_id)
    except Exception as e:
        return JsonResponse({"status": "failed", "message": str(e)})

    try:
        result.delete()
    except Exception as e:
        return JsonResponse({"status": "failed", "message": str(e)})

    return JsonResponse({"status": "success"})

# ajaxy
def delete_amplificationresult(request, result_id):
    try:
        result = AmplificationResult.objects.get(id=result_id)
    except Exception as e:
        return JsonResponse({"status": "failed", "message": str(e)})

    try:
        result.delete()
    except Exception as e:
        return JsonResponse({"status": "failed", "message": str(e)})

    return JsonResponse({"status": "success"})

# ajaxy
def delete_enrichmentresult(request, result_id):
    try:
        result = EnrichmentResult.objects.get(id=result_id)
    except Exception as e:
        return JsonResponse({"status": "failed", "message": str(e)})

    try:
        result.delete()
    except Exception as e:
        return JsonResponse({"status": "failed", "message": str(e)})

    return JsonResponse({"status": "success"})

# ajaxy
def delete_c14(request, slug):
    try:
        c14 = C14.objects.get(slug=slug)
    except Exception as e:
        return JsonResponse({"status": "failed", "message": str(e)})

    try:
        c14.delete()
    except Exception as e:
        return JsonResponse({"status": "failed", "message": str(e)})

    return JsonResponse({"status": "success"})

#Used to check if samples.sample has pk
def _check_sample_pk(jsondata):
    import json
    objects = json.loads(jsondata)
    for obj in objects:
        if obj['model'] == 'samples.sample' and 'pk' in obj:
            return True
    return False

def upload_samples(request):
    if request.method == "POST":
        form = samples.forms.UploadSamplesFileForm(request.POST, request.FILES)

        if form.is_valid():
            """ May need better handling than read() if we ever have to deal
            with a huge ingest file. """
            from readfromexcel import ReadFromExcel
            try:
                excel = ReadFromExcel(request.FILES["file"].read())
            except Exception:
                return HttpResponse("problem with input data")
            try:
                jsondata = excel.json_from_sheets()
            except Exception as e:
                return HttpResponse("Cannot upload data: " + str(e))

            if not request.user.is_superuser and _check_sample_pk(jsondata):
                return HttpResponse("Your user permission does not allow to have acad_num in uploading spreadsheet.")

            newobjs = []
            rejects = []
            force_update = False
            if request.user.is_superuser and form.cleaned_data["force_update"]:
                force_update = True
            newgroup = False

            from django.core.serializers import deserialize
            from django.core.serializers.base import DeserializationError
            try:
                for obj in deserialize("json", jsondata, ignorenonexistent=True):
                    if Sample.objects.filter(acad_num=obj.object.pk) and not force_update:
                        rejects.append(obj.object)
                    else:
                        newobjs.append(obj.object)
                        if obj.object.group_id and not AQISSampleGroup.objects.filter(group_num=obj.object.group_id):
                            AQISSampleGroup.objects.create(group_num=obj.object.group_id)
            except DeserializationError as error:
                return HttpResponse("problem with input data following ACAD{}: {}".format(obj.object.acad_num, error))

            if form.cleaned_data["makeagroup"] and newobjs:
                newgroup = AQISSampleGroup.objects.create()
                for newobj in newobjs:
                    if not newobj.group:
                        newobj.group = newgroup
                newgroup.description = form.cleaned_data["group_description"]
                newgroup.origin = form.cleaned_data["group_origin"]
                newgroup.quantity = len(newobjs)
                newgroup.save()

            for newobj in newobjs:
                newobj.save()

            context = {"sample_list": newobjs, "reject_list": rejects}
            if newgroup:
                context["newgroup"] = newgroup
            return render(request, "upload_samples_results.html", context)
        else:
            return HttpResponse("invalid form data")

    else:
        form = samples.forms.UploadSamplesFileForm()
        if not request.user.is_superuser:
            del form.fields['force_update']
        return render(request, "upload_samples.html", {"form": form})

def upload_c14(request):
    if request.method == "POST":
        form = samples.forms.UploadC14FileForm(request.POST, request.FILES)

        if form.is_valid():
            from readfromexcel import ReadFromExcel
            try:
                excel = ReadFromExcel(request.FILES["file"].read())
            except Exception:
                return HttpResponse("problem with input data")
            jsondata = excel.json_from_sheets()

            from django.core.serializers import deserialize
            from django.core.serializers.base import DeserializationError
            try:
                for obj in deserialize("json", jsondata, ignorenonexistent=True):
                    if not Sample.objects.filter(acad_num=obj.object.sample_id):
                        obj.object.sample = None
                    try:
                        existing = C14.objects.get(slug="{}-{}".format(obj.object.centre, obj.object.centre_num))
                        obj.object.pk = existing.id
                    except Exception:
                        pass
                    obj.save()
                    obj.object.save()
            except DeserializationError as error:
                return HttpResponse("problem with input data: {}".format(error))

            return HttpResponseRedirect(reverse_lazy("c14_index"))

        else:
            return HttpResponse("invalid form data")

    else:
        form = samples.forms.UploadC14FileForm()
        return render(request, "upload_c14.html", {"form": form})

def upload_samplegroups(request):
    if request.method == "POST":
        form = samples.forms.UploadSampleGroupFileForm(request.POST, request.FILES)

        if form.is_valid():
            from readfromexcel import ReadFromExcel
            try:
                excel = ReadFromExcel(request.FILES["file"].read())
            except Exception:
                return HttpResponse("problem with input data")
            try:
                jsondata = excel.json_from_sheets()
            except Exception as e:
                return HttpResponse("Cannot upload data: " + str(e))

            from django.core.serializers import deserialize
            from django.core.serializers.base import DeserializationError
            try:
                for obj in deserialize("json", jsondata, ignorenonexistent=True):
                    obj.save()
                    """ Call the newly created AQISSampleGroup object's save() method """
                    obj.object.save()
            except DeserializationError as error:
                return HttpResponse("problem with input data: {}".format(error))

            return HttpResponseRedirect(reverse_lazy("samplegroup_index"))

        else:
            return HttpResponse("invalid form data")

    else:
        form = samples.forms.UploadSampleGroupFileForm()
        return render(request, "upload_samplegroups.html", {"form": form})

def upload_file(request):
    if request.method == "POST":
        form = samples.forms.UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            from django.forms import ValidationError
            file = FileAttachment(file = request.FILES["file"])
            try:
                file.save()
            except ValidationError as e:
                return HttpResponse(e)
            cleaned_data = form.cleaned_data
            if cleaned_data["next"]:
                return HttpResponseRedirect(cleaned_data["next"])
            else:
                return HttpResponse("it worked")
        else:
            print(form.cleaned_data)
            return HttpResponse("invalid form data")

    else:
        form = samples.forms.UploadFileForm()
        return render(request, "upload_file.html", {"form": form})

def attach_file(request, pk, model):
    from django.contrib import messages
    object = get_object_or_404(model, pk=pk)

    if request.method=="POST":
        form = samples.forms.UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            from django.forms import ValidationError
            uploaded = request.FILES.getlist('file')
            for uf in uploaded:
                file = FileAttachment(file = uf)
                try:
                    file.save()
                except ValidationError as e:
                    return HttpResponse(e)
                object.file.add(file)
                object.save()

            cleaned_data = form.cleaned_data
            if cleaned_data["next"]:
                return HttpResponseRedirect(cleaned_data["next"] + "#files")
            else:
                return HttpResponse("it worked")
        else:
            return HttpResponseRedirect(form.data["next"] + "#files")

    else:
        return HttpResponse("implement something here")

def download_file(request, fileid):
    import os, mimetypes
    fileobj = get_object_or_404(FileAttachment, id=fileid).file
    filename = os.path.basename(fileobj.name)
    response = HttpResponse(fileobj, content_type=mimetypes.guess_type(filename)[0])
    response["Content-Length"] = fileobj.size
    response["Content-Disposition"] = "filename={}".format(filename)
    return response

def file_index(request):
    context = {"fileattachment_list": FileAttachment.objects.all().order_by("name", "-size")}
    return render(request, "file/index.html", context)

# ajaxy
def delete_file(request, file_id):
    try:
        result = FileAttachment.objects.get(id=file_id)
    except Exception as e:
        return JsonResponse({"status": "failed", "message": str(e)})

    try:
        result.delete()
    except Exception as e:
        return JsonResponse({"status": "failed", "message": str(e)})

    return JsonResponse({"status": "success"})

def samples_table_form(request):
    samples = []
    if request.POST.getlist("check"):
        for c in request.POST.getlist("check"):
            sample = Sample.objects.get(acad_num=c)
            samples.append(sample)

    response = HttpResponse("nothing happened")
    if request.POST["opt"] == "csv":
        response = samples_to_csv(samples)
    elif request.POST["opt"] == "project":
        response = create_project_from_samples(samples, user=request.user)
    return response

def export_sample_to_csv(request, pk):
    samples = [Sample.objects.get(acad_num=pk)]
    filename = "ACAD" + pk + ".csv"
    response = samples_to_csv(samples, filename=filename)
    return response

def create_project_from_samples(samples, user=None):
    import datetime
    title = "Project " + datetime.datetime.now().strftime("%Y-%m-%d")
    project = Project.objects.create(title=title)
    project.sample = samples
    if user:
        project.user = [user]
    project.save()
    return HttpResponseRedirect(reverse_lazy("project_detail", kwargs={"pk": project.id}))

def samples_to_csv(samples, filename=None):
    import tablib
    dataset = tablib.Dataset()

    """ Put these fields in the order you want them to appear in the CSV output. """
    headers = ["acad_num", "other_num", "group", "category", "extracted_by_date", "acad_location", "date_of_entry", "abc_num", "organism", "common_name", "genus", "species", "subspecies", "notes", "region", "country", "state", "locality", "lat", "lon", "datum", "collection_date", "collected_by", "quality", "museum", "museum_num", "sampled_by", "sample_date", "mismatch_reason", "sample_repat"]
    dataset.headers = headers

    for sample in samples:
        dict = model_to_dict(sample)
        vals = []
        for header in headers:
            vals.append(dict[header])
        dataset.append(vals)

    response = HttpResponse(content_type='text/csv')
    if not filename:
        filename = "samplesdb_export.csv"
    response['Content-Disposition'] = "attachment; filename={}".format(filename)
    response.write(dataset.csv)
    return response

from haystack.generic_views import SearchView
class MySearchView(SearchView):
    form_class = samples.forms.RawSearchForm
    paginate_by = 0

    def form_valid(self, form):
        self.queryset = form.search()
        context = self.get_context_data(**{
            self.form_name: form,
            'query': form.cleaned_data.get(self.search_field),
            'object_list': self.queryset
        })
        context["sample_list"] = []
        for object in context["object_list"]:
            if object.model_name == "sample":
                context["sample_list"].append(object.object)
        return self.render_to_response(context)

# to enable ajax serch as MySearchView
def search(request):
    # Not necessary to be here
    from django.core import serializers
    f = samples.forms.RawSearchForm(request.GET)
    samples_response = {'sampleList': []}
    try:
        results = f.search()
        for result in results:
            sample_obj = result.object
            sample = json.loads(serializers.serialize('json', [sample_obj]))[0]['fields']
            sample['acad_num'] = sample_obj.pk
            sample['get_location'] = '%s %s' % (sample['region'], sample['country'])
            sample['isExtracted'] = sample_obj.is_extracted()
            sample['isExtracted'] = sample_obj.is_extracted()
            sample['isCarbondated'] = sample_obj.is_carbondated()
            sample['isAmplified'] = sample_obj.is_amplified()
            sample['isEnriched'] = sample_obj.is_enriched()
            sample['isSequenced'] = sample_obj.is_sequenced()
            samples_response['sampleList'].append(sample)
    except Exception as e:
        print(e)
        pass
    return JsonResponse(samples_response)

from django.contrib.auth.models import User, Group
class UserEdit(SuccessMessageMixin, UpdateView):
    model = User
    form_class = samples.forms.UserEditForm
    template_name = "user/user_form.html"
    success_url = reverse_lazy("myaccount")
    success_message = "User updated"

    def get_object(self, queryset=None):
        return self.request.user

def usergroup_index(request):
    group_list = Group.objects.all()

    group_dict = {}
    for group in group_list:
        group_dict[group] = User.objects.filter(groups=group)

    context = {"group_dict": group_dict}
    return render(request, "usergroup/index.html", context)

def usergroup_detail(request, pk):
    group = get_object_or_404(Group, id=pk)
    user_list = User.objects.filter(groups=group)
    project_list = Project.objects.filter(group=group)
    context = {"group": group, "user_list": user_list, "project_list": project_list}
    return render(request, "usergroup/detail.html", context)

class UserGroupAdd(CreateView):
    model = Group
    form_class = samples.forms.UserGroupAddForm
    template_name = "usergroup/usergroup_form.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        if form.cleaned_data["users"]:
            for user in form.cleaned_data["users"]:
                user.groups.add(self.object)
        return HttpResponseRedirect(reverse_lazy("usergroup_detail", kwargs={"pk": self.object.pk}))

class UserGroupEdit(UpdateView):
    model = Group
    form_class = samples.forms.UserGroupEditForm
    template_name = "usergroup/usergroup_form.html"

    def get_initial(self):
        initial = super(UserGroupEdit, self).get_initial()

        try:
            current_users = User.objects.filter(groups=self.object)
        except:
            pass
        else:
            initial["users"] = []
            for user in current_users:
                initial["users"].append(user)
        return initial

    def form_valid(self, form):
        if form.cleaned_data["users"]:
            for user in User.objects.filter(groups=self.object):
                user.groups.remove(self.object)
            for user in form.cleaned_data["users"]:
                user.groups.add(self.object)
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect(reverse_lazy("usergroup_detail", kwargs={"pk": self.object.pk}))

class UserGroupDelete(DeleteView):
    model = Group
    form_class = samples.forms.UserGroupDeleteForm
    template_name = "usergroup/usergroup_delete.html"
    success_url = reverse_lazy("usergroup_index")
