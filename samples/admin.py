from django.contrib import admin
import samples.models

admin.site.register(samples.models.Organism)
admin.site.register(samples.models.Sample)
admin.site.register(samples.models.Project)
admin.site.register(samples.models.Extraction)
admin.site.register(samples.models.ExtractResult)
admin.site.register(samples.models.Amplification)
admin.site.register(samples.models.AmplificationResult)
admin.site.register(samples.models.Enrichment)
admin.site.register(samples.models.EnrichmentResult)
admin.site.register(samples.models.Sequence)
admin.site.register(samples.models.Permit)
admin.site.register(samples.models.AQISSampleGroup)
admin.site.register(samples.models.FileAttachment)
admin.site.register(samples.models.C14)
