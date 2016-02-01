from django.db.models import Q
from django.db import models
from django.core.urlresolvers import reverse_lazy

class Organism(models.Model):
    id = models.PositiveSmallIntegerField("NCBI taxonomy ID", primary_key=True, editable=True)
    genus = models.CharField("Genus", max_length=2048, blank=True)
    species = models.CharField("Species", max_length=2048, blank=True)
    subspecies = models.CharField("Subspecies", max_length=2048, blank=True)
# varietas????
    common = models.CharField("Common name", max_length=2048)

    def __str__(self):
        return "{} ({})".format(self.get_long_name(), self.common)

    def get_absolute_url(self):
        return reverse_lazy("organism_detail", kwargs={"pk": self.pk})

    def get_long_name(self):
        return (" ").join(filter(None, [self.genus, self.species, self.subspecies]))

class Sample(models.Model):
    class Meta:
        ordering = ["acad_num"]

    acad_num = models.AutoField("ACAD sample number", primary_key=True)
    other_num = models.CharField("Other sample number", max_length=2048, blank=True)
    group = models.ForeignKey("AQISSampleGroup", blank=True, null=True, on_delete=models.SET_NULL)
    category = models.CharField("Category of sample", max_length=2048)
    extracted_by_date = models.CharField("Extracted by/date", max_length=2048, blank=True)
    acad_location = models.CharField("ACAD location", max_length=2048, blank=True)
    date_of_entry = models.DateField("Date of entry into ACAD", blank=True, null=True)
    abc_num = models.CharField("ABC/Oxford sample number", max_length=2048, blank=True)
    organism = models.ForeignKey(Organism, blank=True, null=True)
    common_name = models.CharField("Organism common name", max_length=2048, blank=True)
    genus = models.CharField("Genus", max_length=2048, blank=True)
    species = models.CharField("Species", max_length=2048, blank=True)
    subspecies = models.CharField("Subspecies", max_length=2048, blank=True)
    notes = models.TextField("Sample notes", blank=True)
    region = models.CharField("Region", max_length=2048, blank=True)
    country = models.CharField("Country", max_length=2048, blank=True)
    state = models.CharField("State", max_length=2048, blank=True)
    locality = models.CharField("Locality", max_length=2048, blank=True)
    location = models.CharField("Specific location", max_length=2048, blank=True)
    lat = models.CharField("Latitude", max_length=2048, blank=True)
    lon = models.CharField("Longitude", max_length=2048, blank=True)
    datum = models.CharField("Map or GPS datum from which lat/lon taken", max_length=2048, blank=True)
    collection_date = models.DateField("Collection date", blank=True, null=True)
    collected_by = models.CharField("Collected by", max_length=2048, blank=True)
    quality = models.CharField("Quality", max_length=2048, blank=True)
    museum = models.CharField("Museum name", max_length=2048, blank=True)
    museum_num = models.CharField("Museum accession number", max_length=2048, blank=True)
    sampled_by = models.CharField("Sampled by", max_length=2048, blank=True)
    sample_date = models.DateField("Date sampled", blank=True, null=True)
    mismatch_reason = models.CharField("Mismatch reason", max_length=2048, blank=True)
    sample_repat = models.CharField("Sample repatriated", max_length=2048, blank=True)
    file = models.ManyToManyField('FileAttachment', blank=True)

    def __str__(self):
        title_elems = [self.get_formatted_acad_num(), self.common_name, self.category, self.get_location()]
        return (" / ").join(filter(None, title_elems))

    def get_formatted_acad_num(self):
        return "ACAD{}".format(self.acad_num)

    def get_organism(self):
        if self.organism:
            return str(self.organism)
        else:
            return self.common_name

    def get_location(self):
        geo_elems = [self.region, self.country]
        return (", ").join(filter(None, geo_elems))

    def get_truncated_notes(self, chars=50):
        from django.template.defaultfilters import truncatechars
        return truncatechars(self.notes, chars)

    def get_absolute_url(self):
        return reverse_lazy("sample_detail", kwargs={"pk": self.pk})

    def is_extracted(self):
        if ExtractResult.objects.filter(sample=self.acad_num):
            return True
        else:
            return False

    def is_carbondated(self):
        if C14.objects.filter(sample=self.acad_num):
            return True
        else:
            return False

    def is_amplified(self):
        return len(AmplificationResult.objects.filter(extractresult__sample__acad_num=self.acad_num)) > 0

    def is_enriched(self):
        return len(EnrichmentResult.objects.filter(ampresult__extractresult__sample__acad_num=self.acad_num)) > 0

    def is_sequenced(self):
        if self.is_amplified() and self.is_enriched():
            amp_rslts = AmplificationResult.objects.filter(extractresult__sample__acad_num=self.acad_num)
            amps = (rslt.amplification for rslt in amp_rslts)
            enr_rslts = EnrichmentResult.objects.filter(ampresult__extractresult__sample__acad_num=self.acad_num)
            enrs = (rslt.enrichment for rslt in enr_rslts)
            return len(Sequence.objects.filter(Q(amplification__in=amps) | Q(enrichment__in=enrs))) > 0
        else:
            return False

from django.contrib.auth.models import User, Group

class Project(models.Model):
    title = models.CharField("Project title", max_length=2048)
    description = models.TextField("Project description", blank=True)
    sample = models.ManyToManyField(Sample, blank=True)
    user = models.ManyToManyField(User, blank=True)
    group = models.ManyToManyField(Group, blank=True)
    file = models.ManyToManyField('FileAttachment', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("project_detail", kwargs={"pk": self.pk})

class Extraction(models.Model):
    date = models.DateField("Date extracted")
    extracted_by = models.CharField("Extracted by", max_length=2048)
    method = models.TextField("Extraction method")
    extract_control = models.ManyToManyField(Sample, limit_choices_to={'category': 'Extraction control'}, related_name="controls", blank=True)
    notes = models.TextField(blank=True)
    file = models.ManyToManyField('FileAttachment', blank=True)

    def __str__(self):
        return "Extraction {} {}".format(str(self.date), self.extracted_by)

    def get_absolute_url(self):
        return reverse_lazy("extraction_detail", kwargs={"pk": self.pk})

class ExtractResult(models.Model):
    QUANT_METHODS = (
        ('tapestation', 'TapeStation'),
        ('nanodrop', 'NanoDrop'),
        ('qpcr', 'qPCR'),
    )

    id = models.CharField(max_length=2048, primary_key=True, blank=True)
    sample = models.ForeignKey(Sample)
    extraction = models.ForeignKey(Extraction)
    starting = models.CharField("Starting material", max_length=2048, blank=True)
    final_vol = models.CharField("Final DNA volume", help_text="(in ul)", max_length=2048, blank=True)
    dna_yield = models.PositiveIntegerField(blank=True, null=True)
    quant_method = models.CharField("Quantification method", max_length=2048, choices=QUANT_METHODS, blank=True)

    def __str__(self):
        return "{} extracted {}".format(self.id, str(self.extraction.date))

    def get_absolute_url(self):
        return reverse_lazy("extraction_detail", kwargs={"pk": self.extraction.pk})

class Amplification(models.Model):
    date = models.DateField("Date")
    prepared_by = models.CharField("Prepared by", max_length=2048)
    method = models.TextField("Method", help_text="e.g. library prep or PCR")
    amp_type = models.CharField("Amplification type", max_length=2048, blank=True)
    treatment = models.CharField("Treatment", max_length=2048, blank=True)
    notes = models.TextField(blank=True)
    file = models.ManyToManyField('FileAttachment', blank=True)

    def __str__(self):
        return "Amplification {} {}".format(str(self.date), self.prepared_by)

    def get_absolute_url(self):
        return reverse_lazy("amplification_detail", kwargs={"pk": self.pk})

class AmplificationResult(models.Model):
    id = models.CharField(max_length=2048, primary_key=True, blank=True)
    extractresult = models.ForeignKey(ExtractResult)
    amplification = models.ForeignKey(Amplification)
    dna_yield = models.PositiveIntegerField(blank=True, null=True)
    quant_method = models.CharField("Quantification method", max_length=2048, blank=True)

    def __str__(self):
        return "{} prepared {}".format(self.id, str(self.amplification.date))

    def get_absolute_url(self):
        return reverse_lazy("amplification_detail", kwargs={"pk": self.amplification.pk})

class Enrichment(models.Model):
    date = models.DateField("Date")
    prepared_by = models.CharField("Prepared by", max_length=2048)
    notes = models.TextField(blank=True)
    file = models.ManyToManyField('FileAttachment', blank=True)

    def __str__(self):
        return "Enrichment {} {}".format(str(self.date), self.prepared_by)

    def get_absolute_url(self):
        return reverse_lazy("enrichment_detail", kwargs={"pk": self.pk})

class EnrichmentResult(models.Model):
    id = models.CharField(max_length=2048, primary_key=True, blank=True)
    ampresult = models.ForeignKey(AmplificationResult)
    enrichment = models.ForeignKey(Enrichment)
    enrich_type = models.CharField("Enrichment type", max_length=2048, help_text="e.g. Mito, 10k", blank=True)
    bait_detail = models.CharField("Bait detail", max_length=2048, help_text="MyBait batch number", blank=True)
    dna_yield = models.PositiveIntegerField(blank=True, null=True)
    quant_method = models.CharField("Quantification method", max_length=2048, blank=True)

    def __str__(self):
        return "{} prepared {}".format(self.id, str(self.enrichment.date))

    def get_absolute_url(self):
        return reverse_lazy("enrichment_detail", kwargs={"pk": self.enrichment.pk})

class Sequence(models.Model):
    amplification = models.ForeignKey(Amplification, blank=True, null=True)
    enrichment = models.ForeignKey(Enrichment, blank=True, null=True)
    path = models.TextField("Path to sequencing files")

    def __str__(self):
        if self.amplification:
            return "Sequence for {}".format(self.amplification)
        elif self.enrichment:
            return "Sequence for {}".format(self.enrichment)
        else:
            return "Sequence not attached to anything"

    def get_absolute_url(self):
        return reverse_lazy("sequence_detail", kwargs={"pk": self.pk})

class Permit(models.Model):
    permit_num = models.CharField("Permit number", max_length=2048)
    valid_from = models.DateField("Valid from")
    valid_to = models.DateField("Valid to")
    valid_for = models.CharField("Valid for", max_length=2048)
    active_from = models.DateField("Active from", blank=True)
    conditions = models.TextField("Conditions", max_length=2048, blank=True)
    qap = models.CharField(max_length=2048, blank=True)
    file = models.ManyToManyField('FileAttachment', blank=True)

    def __str__(self):
        return "{} {} (valid to {})".format(self.permit_num, self.valid_for, self.valid_to)

    def get_absolute_url(self):
        return reverse_lazy("permit_detail", kwargs={"pk": self.pk})

class AQISSampleGroup(models.Model):
    class Meta:
        verbose_name = "AQIS sample group"
        ordering = ["-group_num_int", "-group_num"]

    group_num = models.CharField("Group number", max_length=2048, primary_key=True, blank=True)
    group_num_int= models.PositiveIntegerField(blank=True, null=True)
    aqis_num = models.CharField("AQIS Quarantine Entry/Order Number", max_length=2048, blank=True)
    accession_date = models.DateField("Date of entry into ACAD", blank=True, null=True)
    permit = models.ForeignKey(Permit, blank=True, null=True)
    permit_num = models.CharField("Permit number", max_length=2048, blank=True)
    description = models.CharField("Goods description", max_length=2048, blank=True)
    quantity = models.PositiveSmallIntegerField("Quantity", blank=True, null=True)
    origin = models.CharField("Country of origin", max_length=2048, blank=True)
    acad_loc = models.CharField("ACAD location", max_length=2048, blank=True)
    movement = models.CharField("Movement and transfer", max_length=2048, blank=True)
    notes = models.CharField("Other relevant info", max_length=2048, blank=True)
    sent_by = models.CharField("Sent by", max_length=2048, blank=True)
    contact = models.CharField("ACAD contact", max_length=2048, blank=True)

    def get_formatted_group_num(self):
        try:
            int(self.group_num)
            return "GP{:0>4}".format(self.group_num)
        except ValueError:
            return "GP{:0>5}".format(self.group_num)

    def __str__(self):
        string = "{} {}".format(self.get_formatted_group_num(), self.description)
        if self.origin:
            string = "{} ({})".format(string, self.origin)
        return string

    def get_absolute_url(self):
        return reverse_lazy("samplegroup_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        if not self.group_num:
            try:
                previous_group_num_int = AQISSampleGroup.objects.order_by("-group_num_int")[0].group_num_int
            except Exception:
                previous_group_num_int = 0
            self.group_num = previous_group_num_int + 1
        import re
        self.group_num_int = int(re.sub(r"[^\d.]", "", str(self.group_num)))
        super(AQISSampleGroup, self).save(*args, **kwargs)

class FileAttachment(models.Model):
    file = models.FileField(upload_to="files")
    name = models.CharField("File name", max_length=2048, blank=True)
    size = models.PositiveIntegerField("File size", blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("download_file", kwargs={"fileid": self.id})

    def get_attached_objects(self):
        objects = []
        objects.extend(self.project_set.all())
        objects.extend(self.permit_set.all())
        objects.extend(self.extraction_set.all())
        objects.extend(self.sample_set.all())
        return objects

    def save(self, *args, **kwargs):
        from django.conf import settings
        if hasattr(settings, 'MAX_UPLOAD_SIZE'):
            if self.file.size > settings.MAX_UPLOAD_SIZE:
                from django.forms import ValidationError
                raise ValidationError("file too big")
        if not self.name:
            import os
            self.name = os.path.basename(self.file.name)
        self.size = self.file.size
        super(FileAttachment, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.file.delete(save=False)
        super(FileAttachment, self).delete(*args, **kwargs)

class C14(models.Model):
    class Meta:
        unique_together = ("centre", "centre_num")

    sample = models.ForeignKey(Sample, blank=True, null=True)
    sampref = models.CharField(max_length=2048)
    date = models.CharField("Estimated age in radiocarbon years", max_length=2048)
    error = models.PositiveSmallIntegerField("Estimated carbon date error range", blank=True, null=True)
    centre = models.CharField("Centre that did carbon dating", max_length=2048)
    centre_num = models.CharField("Centre reference number", max_length=2048)
    del13 = models.DecimalField(max_digits=25, decimal_places=20, blank=True, null=True)
    del15 = models.DecimalField(max_digits=25, decimal_places=20, blank=True, null=True)
    cnratio = models.DecimalField(max_digits=25, decimal_places=20, blank=True, null=True)
    use_weight = models.DecimalField(max_digits=25, decimal_places=20, blank=True, null=True)
    pyield = models.DecimalField(max_digits=25, decimal_places=20, blank=True, null=True)
    burnweight = models.DecimalField(max_digits=25, decimal_places=20, blank=True, null=True)
    burnyield = models.DecimalField(max_digits=25, decimal_places=20, blank=True, null=True)
    pcbyield = models.DecimalField(max_digits=25, decimal_places=20, blank=True, null=True)
    nyield = models.DecimalField(max_digits=25, decimal_places=20, blank=True, null=True)
    percent_c = models.DecimalField(max_digits=25, decimal_places=20, blank=True, null=True)
    mg_c = models.DecimalField(max_digits=25, decimal_places=20, blank=True, null=True)
    slug = models.SlugField(max_length=2048, blank=True, null=True)

    def __str__(self):
        if self.sample:
            return "{} {}-{}".format(self.sample.get_formatted_acad_num(), self.centre, self.centre_num)
        else:
            return "{}-{}".format(self.centre, self.centre_num)

    def save(self, *args, **kwargs):
        self.slug = "{}-{}".format(self.centre, self.centre_num)
        super(C14, self).save(*args, **kwargs)
        """ If this C14 is associated with a sample, we need to save() that
        sample to trigger reindexing it in Elasticsearch and populate its
        carbondate_field. """
        if self.sample:
            Sample.objects.get(acad_num=self.sample_id).save()
