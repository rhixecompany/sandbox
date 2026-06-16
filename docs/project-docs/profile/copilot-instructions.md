# profile
**Django**: PEP 8, CBVs preferred, namespaced app URLs, custom `ModelAdmin`.
**Models**: define `__str__`, `Meta`, `get_absolute_url`; `prepopulated_fields` for slugs.
**Security**: no `SECRET_KEY` in VCS; django-environ; `DEBUG=False` in prod; sanitize CKEditor HTML to prevent XSS.
