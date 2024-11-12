from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.models import Page,Orderable
from wagtail.fields import RichTextField
from modelcluster.fields import ParentalKey

from wagtail.admin.panels import FieldPanel,MultiFieldPanel,InlinePanel


# class Banner(Page):
#     template = "home/banner_page.html"
#     subpage_types = []
    


class HomePage(Page):
    template = "home/home_page.html"
    max_count=1

    banner_image = models.ForeignKey("wagtailimages.Image", null=True,blank=True, on_delete=models.SET_NULL)
    banner_title = models.CharField(_("Banner Title"), max_length=100,help_text="Banner Title *")
    banner_subtitle = models.CharField(_("Banner Sub Title"), max_length=300,null=True,blank=True,help_text="Banner Subtitle ")
    banner_cta = models.CharField(_(""), max_length=50,help_text="Text to display on Call to Action")
    banner_cta_link = models.ForeignKey("wagtailcore.Page",null=True,blank=True,on_delete=models.SET_NULL,related_name="homePageBannerLink",help_text="Choose a page to link to for the Call to Action")
    banner_cta_url = models.URLField(_(""), max_length=250,null=True,blank=True,help_text="if banner_cta_link not found. Then this url will work")

    content_panels = Page.content_panels + [ 
        MultiFieldPanel([
            FieldPanel("banner_image"),
            FieldPanel("banner_title"),
            FieldPanel("banner_subtitle"),
            FieldPanel("banner_cta"),
            FieldPanel("banner_cta_link"),
            FieldPanel("banner_cta_url"),
        ],heading="Home Page Banner")
    ]

    def get_admin_display_title(self):
        return "Zealve's Home"