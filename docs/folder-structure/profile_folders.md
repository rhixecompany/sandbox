# profile - Folder Structure Blueprint

**Project Path:** `C:\Users\Alexa\Desktop\SandBox\projects\profile`
**Generated:** 2026-07-10
**Stack:** Django

## Directory Tree

```
profile/
├── .github/
│   └── copilot-instructions.md
├── .vscode/
│   ├── extensions.json
│   ├── launch.json
│   ├── settings.json
│   └── tasks.json
├── AGENTS.md
├── base/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── decorators.py
│   ├── filters.py
│   ├── forms.py
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── 0002_post_thumbnail.py
│   │   ├── 0003_post_slug.py
│   │   ├── 0004_auto_20200729_1333.py
│   │   ├── 0005_auto_20200729_1349.py
│   │   ├── 0006_auto_20201107_1212.py
│   │   ├── 0007_profile_user.py
│   │   ├── 0008_auto_20201107_1351.py
│   │   ├── 0009_postcomment_created.py
│   │   ├── 0010_auto_20201109_1219.py
│   │   ├── 0011_profile_bio.py
│   │   ├── 0012_auto_20201109_1408.py
│   │   ├── 0013_auto_20201109_1436.py
│   │   ├── 0014_auto_20220627_2139.py
│   │   ├── 0015_auto_20220627_2211.py
│   │   └── __init__.py
│   ├── models.py
│   ├── signals.py
│   ├── static/
│   │   ├── admin/
│   │   │   ├── css/
│   │   │   │   ├── autocomplete.css
│   │   │   │   ├── base.css
│   │   │   │   ├── changelists.css
│   │   │   │   ├── dashboard.css
│   │   │   │   ├── fonts.css
│   │   │   │   ├── forms.css
│   │   │   │   ├── login.css
│   │   │   │   ├── responsive.css
│   │   │   │   ├── responsive_rtl.css
│   │   │   │   ├── rtl.css
│   │   │   │   ├── vendor/
│   │   │   │   └── widgets.css
│   │   │   ├── fonts/
│   │   │   │   ├── LICENSE.txt
│   │   │   │   ├── README.txt
│   │   │   │   ├── Roboto-Bold-webfont.woff
│   │   │   │   ├── Roboto-Light-webfont.woff
│   │   │   │   └── Roboto-Regular-webfont.woff
│   │   │   ├── img/
│   │   │   │   ├── calendar-icons.svg
│   │   │   │   ├── gis/
│   │   │   │   ├── icon-addlink.svg
│   │   │   │   ├── icon-alert.svg
│   │   │   │   ├── icon-calendar.svg
│   │   │   │   ├── icon-changelink.svg
│   │   │   │   ├── icon-clock.svg
│   │   │   │   ├── icon-deletelink.svg
│   │   │   │   ├── icon-no.svg
│   │   │   │   ├── icon-unknown-alt.svg
│   │   │   │   ├── icon-unknown.svg
│   │   │   │   ├── icon-viewlink.svg
│   │   │   │   ├── icon-yes.svg
│   │   │   │   ├── inline-delete.svg
│   │   │   │   ├── LICENSE
│   │   │   │   ├── README.txt
│   │   │   │   ├── search.svg
│   │   │   │   ├── selector-icons.svg
│   │   │   │   ├── sorting-icons.svg
│   │   │   │   ├── tooltag-add.svg
│   │   │   │   └── tooltag-arrowright.svg
│   │   │   └── js/
│   │   │       ├── actions.js
│   │   │       ├── actions.min.js
│   │   │       ├── admin/
│   │   │       ├── autocomplete.js
│   │   │       ├── calendar.js
│   │   │       ├── cancel.js
│   │   │       ├── change_form.js
│   │   │       ├── collapse.js
│   │   │       ├── collapse.min.js
│   │   │       ├── core.js
│   │   │       ├── inlines.js
│   │   │       ├── inlines.min.js
│   │   │       ├── jquery.init.js
│   │   │       ├── popup_response.js
│   │   │       ├── prepopulate.js
│   │   │       ├── prepopulate.min.js
│   │   │       ├── prepopulate_init.js
│   │   │       ├── SelectBox.js
│   │   │       ├── SelectFilter2.js
│   │   │       ├── urlify.js
│   │   │       └── vendor/
│   │   ├── ckeditor/
│   │   │   ├── ckeditor/
│   │   │   │   ├── adapters/
│   │   │   │   ├── build-config.js
│   │   │   │   ├── CHANGES.md
│   │   │   │   ├── ckeditor.js
│   │   │   │   ├── config.js
│   │   │   │   ├── contents.css
│   │   │   │   ├── lang/
│   │   │   │   ├── LICENSE.md
│   │   │   │   ├── plugins/
│   │   │   │   ├── README.md
│   │   │   │   ├── skins/
│   │   │   │   ├── styles.js
│   │   │   │   └── vendor/
│   │   │   ├── ckeditor-init.js
│   │   │   ├── ckeditor_uploader/
│   │   │   │   └── admin_base.css
│   │   │   ├── file-icons/
│   │   │   │   ├── doc.png
│   │   │   │   ├── file.png
│   │   │   │   ├── pdf.png
│   │   │   │   ├── ppt.png
│   │   │   │   ├── swf.png
│   │   │   │   ├── txt.png
│   │   │   │   └── xls.png
│   │   │   └── galleriffic/
│   │   │       ├── css/
│   │   │       └── js/
│   │   ├── css/
│   │   │   ├── blue.css
│   │   │   ├── default.css
│   │   │   ├── green.css
│   │   │   └── purple.css
│   │   ├── images/
│   │   │   ├── Aei.jpg
│   │   │   ├── favicon.ico
│   │   │   ├── Frontcard.png
│   │   │   ├── images/
│   │   │   │   ├── ecom.jpg
│   │   │   │   ├── filter.JPG
│   │   │   │   ├── user.png
│   │   │   │   ├── user_y01oU5U.png
│   │   │   │   └── wordpress_or_django.jpg
│   │   │   ├── Logo.jpg
│   │   │   ├── Logo.png
│   │   │   ├── menu.png
│   │   │   ├── placeholder.png
│   │   │   ├── uploads/
│   │   │   │   └── 2020/
│   │   │   └── user.png
│   │   ├── js/
│   │   │   └── script.js
│   │   └── resume.pdf
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── migrate.yaml
├── Procfile
├── requirements.txt
├── RESEARCH_REPORT.md
├── rhixecompany/
│   ├── __init__.py
│   ├── asgi.py
│   ├── migrations/
│   │   ├── 0001_createsuperuser.py
│   │   └── __init__.py
│   ├── setting.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/
│   ├── admin/
│   │   ├── css/
│   │   │   ├── autocomplete.css
│   │   │   ├── base.css
│   │   │   ├── changelists.css
│   │   │   ├── dashboard.css
│   │   │   ├── fonts.css
│   │   │   ├── forms.css
│   │   │   ├── login.css
│   │   │   ├── responsive.css
│   │   │   ├── responsive_rtl.css
│   │   │   ├── rtl.css
│   │   │   ├── vendor/
│   │   │   │   └── select2/
│   │   │   └── widgets.css
│   │   ├── fonts/
│   │   │   ├── LICENSE.txt
│   │   │   ├── README.txt
│   │   │   ├── Roboto-Bold-webfont.woff
│   │   │   ├── Roboto-Light-webfont.woff
│   │   │   └── Roboto-Regular-webfont.woff
│   │   ├── img/
│   │   │   ├── calendar-icons.svg
│   │   │   ├── gis/
│   │   │   │   ├── move_vertex_off.svg
│   │   │   │   └── move_vertex_on.svg
│   │   │   ├── icon-addlink.svg
│   │   │   ├── icon-alert.svg
│   │   │   ├── icon-calendar.svg
│   │   │   ├── icon-changelink.svg
│   │   │   ├── icon-clock.svg
│   │   │   ├── icon-deletelink.svg
│   │   │   ├── icon-no.svg
│   │   │   ├── icon-unknown-alt.svg
│   │   │   ├── icon-unknown.svg
│   │   │   ├── icon-viewlink.svg
│   │   │   ├── icon-yes.svg
│   │   │   ├── inline-delete.svg
│   │   │   ├── LICENSE
│   │   │   ├── README.txt
│   │   │   ├── search.svg
│   │   │   ├── selector-icons.svg
│   │   │   ├── sorting-icons.svg
│   │   │   ├── tooltag-add.svg
│   │   │   └── tooltag-arrowright.svg
│   │   └── js/
│   │       ├── actions.js
│   │       ├── actions.min.js
│   │       ├── admin/
│   │       │   ├── DateTimeShortcuts.js
│   │       │   └── RelatedObjectLookups.js
│   │       ├── autocomplete.js
│   │       ├── calendar.js
│   │       ├── cancel.js
│   │       ├── change_form.js
│   │       ├── collapse.js
│   │       ├── collapse.min.js
│   │       ├── core.js
│   │       ├── inlines.js
│   │       ├── inlines.min.js
│   │       ├── jquery.init.js
│   │       ├── popup_response.js
│   │       ├── prepopulate.js
│   │       ├── prepopulate.min.js
│   │       ├── prepopulate_init.js
│   │       ├── SelectBox.js
│   │       ├── SelectFilter2.js
│   │       ├── urlify.js
│   │       └── vendor/
│   │           ├── jquery/
│   │           ├── select2/
│   │           └── xregexp/
│   ├── ckeditor/
│   │   ├── ckeditor/
│   │   │   ├── adapters/
│   │   │   │   └── jquery.js
│   │   │   ├── build-config.js
│   │   │   ├── CHANGES.md
│   │   │   ├── ckeditor.js
│   │   │   ├── config.js
│   │   │   ├── contents.css
│   │   │   ├── lang/
│   │   │   │   ├── af.js
│   │   │   │   ├── ar.js
│   │   │   │   ├── az.js
│   │   │   │   ├── bg.js
│   │   │   │   ├── bn.js
│   │   │   │   ├── bs.js
│   │   │   │   ├── ca.js
│   │   │   │   ├── cs.js
│   │   │   │   ├── cy.js
│   │   │   │   ├── da.js
│   │   │   │   ├── de-ch.js
│   │   │   │   ├── de.js
│   │   │   │   ├── el.js
│   │   │   │   ├── en-au.js
│   │   │   │   ├── en-ca.js
│   │   │   │   ├── en-gb.js
│   │   │   │   ├── en.js
│   │   │   │   ├── eo.js
│   │   │   │   ├── es-mx.js
│   │   │   │   ├── es.js
│   │   │   │   ├── et.js
│   │   │   │   ├── eu.js
│   │   │   │   ├── fa.js
│   │   │   │   ├── fi.js
│   │   │   │   ├── fo.js
│   │   │   │   ├── fr-ca.js
│   │   │   │   ├── fr.js
│   │   │   │   ├── gl.js
│   │   │   │   ├── gu.js
│   │   │   │   ├── he.js
│   │   │   │   ├── hi.js
│   │   │   │   ├── hr.js
│   │   │   │   ├── hu.js
│   │   │   │   ├── id.js
│   │   │   │   ├── is.js
│   │   │   │   ├── it.js
│   │   │   │   ├── ja.js
│   │   │   │   ├── ka.js
│   │   │   │   ├── km.js
│   │   │   │   ├── ko.js
│   │   │   │   ├── ku.js
│   │   │   │   ├── lt.js
│   │   │   │   ├── lv.js
│   │   │   │   ├── mk.js
│   │   │   │   ├── mn.js
│   │   │   │   ├── ms.js
│   │   │   │   ├── nb.js
│   │   │   │   ├── nl.js
│   │   │   │   ├── no.js
│   │   │   │   ├── oc.js
│   │   │   │   ├── pl.js
│   │   │   │   ├── pt-br.js
│   │   │   │   ├── pt.js
│   │   │   │   ├── ro.js
│   │   │   │   ├── ru.js
│   │   │   │   ├── si.js
│   │   │   │   ├── sk.js
│   │   │   │   ├── sl.js
│   │   │   │   ├── sq.js
│   │   │   │   ├── sr-latn.js
│   │   │   │   ├── sr.js
│   │   │   │   ├── sv.js
│   │   │   │   ├── th.js
│   │   │   │   ├── tr.js
│   │   │   │   ├── tt.js
│   │   │   │   ├── ug.js
│   │   │   │   ├── uk.js
│   │   │   │   ├── vi.js
│   │   │   │   ├── zh-cn.js
│   │   │   │   └── zh.js
│   │   │   ├── LICENSE.md
│   │   │   ├── plugins/
│   │   │   │   ├── a11yhelp/
│   │   │   │   ├── about/
│   │   │   │   ├── adobeair/
│   │   │   │   ├── ajax/
│   │   │   │   ├── autoembed/
│   │   │   │   ├── autogrow/
│   │   │   │   ├── autolink/
│   │   │   │   ├── bbcode/
│   │   │   │   ├── clipboard/
│   │   │   │   ├── codesnippet/
│   │   │   │   ├── codesnippetgeshi/
│   │   │   │   ├── colordialog/
│   │   │   │   ├── copyformatting/
│   │   │   │   ├── devtools/
│   │   │   │   ├── dialog/
│   │   │   │   ├── div/
│   │   │   │   ├── divarea/
│   │   │   │   ├── docprops/
│   │   │   │   ├── embed/
│   │   │   │   ├── embedbase/
│   │   │   │   ├── embedsemantic/
│   │   │   │   ├── filetools/
│   │   │   │   ├── find/
│   │   │   │   ├── flash/
│   │   │   │   ├── forms/
│   │   │   │   ├── icons.png
│   │   │   │   ├── icons_hidpi.png
│   │   │   │   ├── iframe/
│   │   │   │   ├── iframedialog/
│   │   │   │   ├── image/
│   │   │   │   ├── image2/
│   │   │   │   ├── language/
│   │   │   │   ├── lineutils/
│   │   │   │   ├── link/
│   │   │   │   ├── liststyle/
│   │   │   │   ├── magicline/
│   │   │   │   ├── mathjax/
│   │   │   │   ├── menubutton/
│   │   │   │   ├── notification/
│   │   │   │   ├── notificationaggregator/
│   │   │   │   ├── pagebreak/
│   │   │   │   ├── pastefromgdocs/
│   │   │   │   ├── pastefromword/
│   │   │   │   ├── pastetools/
│   │   │   │   ├── placeholder/
│   │   │   │   ├── preview/
│   │   │   │   ├── scayt/
│   │   │   │   ├── sharedspace/
│   │   │   │   ├── showblocks/
│   │   │   │   ├── smiley/
│   │   │   │   ├── sourcedialog/
│   │   │   │   ├── specialchar/
│   │   │   │   ├── stylesheetparser/
│   │   │   │   ├── table/
│   │   │   │   ├── tableresize/
│   │   │   │   ├── tableselection/
│   │   │   │   ├── tabletools/
│   │   │   │   ├── templates/
│   │   │   │   ├── uicolor/
│   │   │   │   ├── uploadimage/
│   │   │   │   ├── uploadwidget/
│   │   │   │   ├── widget/
│   │   │   │   ├── wsc/
│   │   │   │   └── xml/
│   │   │   ├── README.md
│   │   │   ├── skins/
│   │   │   │   ├── moono/
│   │   │   │   └── moono-lisa/
│   │   │   ├── styles.js
│   │   │   └── vendor/
│   │   │       └── promise.js
│   │   ├── ckeditor-init.js
│   │   ├── ckeditor_uploader/
│   │   │   └── admin_base.css
│   │   ├── file-icons/
│   │   │   ├── doc.png
│   │   │   ├── file.png
│   │   │   ├── pdf.png
│   │   │   ├── ppt.png
│   │   │   ├── swf.png
│   │   │   ├── txt.png
│   │   │   └── xls.png
│   │   └── galleriffic/
│   │       ├── css/
│   │       │   ├── basic.css
│   │       │   ├── black.css
│   │       │   ├── caption.png
│   │       │   ├── galleriffic-1.css
│   │       │   ├── galleriffic-2.css
│   │       │   ├── galleriffic-3.css
│   │       │   ├── galleriffic-4.css
│   │       │   ├── galleriffic-5.css
│   │       │   ├── jush.css
│   │       │   ├── loader.gif
│   │       │   ├── loaderWhite.gif
│   │       │   ├── nextPageArrow.gif
│   │       │   ├── nextPageArrowWhite.gif
│   │       │   ├── prevPageArrow.gif
│   │       │   ├── prevPageArrowWhite.gif
│   │       │   └── white.css
│   │       └── js/
│   │           ├── jquery-1.3.2.js
│   │           ├── jquery.galleriffic.js
│   │           ├── jquery.history.js
│   │           ├── jquery.opacityrollover.js
│   │           └── jush.js
│   ├── css/
│   │   ├── blue.css
│   │   ├── default.css
│   │   ├── green.css
│   │   └── purple.css
│   ├── images/
│   │   ├── Aei.jpg
│   │   ├── favicon.ico
│   │   ├── Frontcard.png
│   │   ├── images/
│   │   │   ├── ecom.jpg
│   │   │   ├── filter.JPG
│   │   │   ├── Screenshot_from_2022-08-07_04-21-58.png
│   │   │   ├── user.png
│   │   │   ├── user_y01oU5U.png
│   │   │   └── wordpress_or_django.jpg
│   │   ├── Logo.jpg
│   │   ├── Logo.png
│   │   ├── menu.png
│   │   ├── placeholder.png
│   │   ├── uploads/
│   │   │   └── 2020/
│   │   │       └── 07/
│   │   └── user.png
│   ├── js/
│   │   └── script.js
│   └── resume.pdf
└── templates/
    ├── base/
    │   ├── account.html
    │   ├── delete.html
    │   ├── email_sent.html
    │   ├── email_template.html
    │   ├── index.html
    │   ├── login.html
    │   ├── main.html
    │   ├── navbar.html
    │   ├── password_reset.html
    │   ├── post.html
    │   ├── post_form.html
    │   ├── posts.html
    │   ├── profile_form.html
    │   └── register.html
    ├── email_sent.html
    ├── password_reset.html
    ├── reset.html
    └── reset_complete.html
```

## Key Directories

| Directory | Purpose | Convention |
| ----------- | --------- | ------------ |
| `<app>/` | Django apps | lowercase, plural |
| `config/` / `settings/` | Settings modules | base/local/production |
| `templates/` | HTML templates | app-specific subdirs |
| `static/` | Static assets | Collected by collectstatic |

## Naming Conventions

- **Directories:** kebab-case (multi-word) or lowercase
- **Files:** Match language convention (PascalCase for React, snake_case for Python)
- **Configs:** lowercase with extension (.json, .yaml, .toml)

## File Placement Patterns

- Tests: co-located (`__tests__/`) or mirrored `tests/` structure
- Types: `types/` or co-located with implementation
- Config: Root level for tool configs

---
*Generated by agents-system-prompt-context-fix-runner*
