from django.db import models

# Create your models here.

# Stores customer information and notes.
class Client(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField(blank=True)
    notes = models.TextField(blank=True)

# Main entity representing both estimates and templates.
class Job(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order_type = models.CharField(max_length=100)  # e.g. Box, Book
    order_name = models.CharField(max_length=255)
    is_template = models.BooleanField(default=False)
    is_finalized = models.BooleanField(default=False)
    version = models.CharField(max_length=10, default="v01")
    quantity = models.PositiveIntegerField()
    variant_quantities = models.CharField(max_length=100, blank=True)  # comma-separated
    # Paper parameters
    paper_type = models.CharField(max_length=100)
    paper_weight = models.PositiveIntegerField(help_text="g/m²")
    end_size = models.CharField(max_length=50)
    printing_size = models.CharField(max_length=50)
    selling_size = models.CharField(max_length=50)
    parts_of_selling_size = models.PositiveIntegerField()
    # Print parameters
    n_up = models.PositiveIntegerField()
    colors_front = models.PositiveIntegerField()
    colors_back = models.PositiveIntegerField()
    special_colors = models.PositiveIntegerField()
    # Book-specific
    num_pages = models.PositiveIntegerField(null=True, blank=True)
    n_up_signatures = models.PositiveIntegerField(null=True, blank=True)

# Global reusable operations (Cutting, Printing, etc.)
class MasterOperation(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)  # e.g. Printing, Finishing
    cost_formula = models.TextField()
    time_formula = models.TextField()
    description = models.TextField(blank=True)

# Operation instance for a specific job
class JobOperation(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='operations')
    master_operation = models.ForeignKey(MasterOperation, on_delete=models.PROTECT)
    sequence = models.PositiveIntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    time = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

