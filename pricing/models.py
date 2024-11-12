from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.models import Page,Orderable
from modelcluster.fields import ParentalKey
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel,MultiFieldPanel,InlinePanel

class PricingPlan(Orderable):
    subpage_types = []
    max_count=1
    class PlanBasis(models.TextChoices):
        YEAR ="YEAR","year",
        MONTH ="MONTH","month",
        WEEK ="WEEK","week",
        DAY ="DAY","day",

    page=ParentalKey("pricing.PricingPage",related_name="pricingPagePlan")
    plan_name = models.CharField(_("Plan Name"), max_length=80,help_text="Plan Name is Mendatory*")
    plan_price = models.CharField(_("Plan Price"),max_length=20,help_text="Plan Price is Mendatory*")
    price_basis = models.CharField(_(""), max_length=100,choices=PlanBasis.choices,default=PlanBasis.MONTH)
    plan_subdesc= models.CharField(_("Plan Subdescription"), max_length=200,null=True,blank=True,help_text="This field is optional")
    plan_service_desc = RichTextField(blank=True)
    plan_cta = models.CharField(_(""), max_length=50,help_text="Text to display on Call to Action")
    plan_cta_link = models.ForeignKey("wagtailcore.Page",null=True,blank=True,on_delete=models.SET_NULL,related_name="planCtaLink",help_text="Choose a page to link to for the Call to Action")


    panels = [ 
        FieldPanel("plan_name"),
        FieldPanel("plan_price"),
        FieldPanel("price_basis"),
        FieldPanel("plan_subdesc"),
        FieldPanel("plan_service_desc"),
        FieldPanel("plan_cta"),
        FieldPanel("plan_cta_link"),
    ]

class PricingPage(Page):

    content_panels = Page.content_panels + [ 
        MultiFieldPanel([
            InlinePanel("pricingPagePlan",max_num=3,min_num=3,label="Price Plan")
        ],heading="Pricing Plan"),
    ]

