# Django-Scrapy-Selenium - Folder Structure Blueprint

**Project Path:** `C:\Users\Alexa\Desktop\SandBox\projects\Django-Scrapy-Selenium`
**Generated:** 2026-07-10
**Stack:** Django/Scrapy/Selenium

## Directory Tree

```
Django-Scrapy-Selenium/
├── .editorconfig
├── .github/
│   ├── copilot-instructions.md
│   └── workflows/
│       ├── ci.yml
│       ├── collectstatic.yaml
│       ├── deploy.yaml
│       ├── main.yaml
│       └── prod.yaml
├── .vscode/
│   ├── extensions.json
│   ├── launch.json
│   ├── settings.json
│   └── tasks.json
├── AGENTS.md
├── api/
│   ├── __init__.py
│   ├── apps/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── filters.py
│   │   ├── forms.py
│   │   ├── migrations/
│   │   │   ├── 0001_initial.py
│   │   │   ├── 0002_initial.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── scripts/
│   │   │   ├── __init__.py
│   │   │   ├── count_script.py
│   │   │   └── orm_script.py
│   │   ├── signals.py
│   │   ├── tables.py
│   │   ├── templatetags/
│   │   │   ├── __init__.py
│   │   │   ├── example.py
│   │   │   └── format_json.py
│   │   ├── tests.py
│   │   ├── urls/
│   │   │   ├── __init__.py
│   │   │   ├── bookmark_urls.py
│   │   │   ├── chapter_urls.py
│   │   │   └── comic_urls.py
│   │   ├── utils.py
│   │   ├── validators.py
│   │   └── views/
│   │       ├── __init__.py
│   │       ├── bookmark_views.py
│   │       ├── chapter_views.py
│   │       └── comic_views.py
│   ├── conftest.py
│   ├── contrib/
│   │   ├── __init__.py
│   │   └── sites/
│   │       ├── __init__.py
│   │       └── migrations/
│   │           ├── 0001_initial.py
│   │           ├── 0002_alter_domain_unique.py
│   │           ├── 0003_set_site_domain_and_name.py
│   │           ├── 0004_alter_options_ordering_domain.py
│   │           └── __init__.py
│   ├── home/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── context_processors.py
│   │   ├── migrations/
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── src/
│   │   ├── alpine_init.ts
│   │   ├── backtotop.ts
│   │   ├── carousel.ts
│   │   ├── dark-mode.ts
│   │   ├── htmx_init.ts
│   │   ├── hyper_init.ts
│   │   ├── navbar.ts
│   │   ├── project.ts
│   │   ├── sass/
│   │   │   ├── function/
│   │   │   │   ├── alpine.scss
│   │   │   │   ├── app.scss
│   │   │   │   ├── carousel.scss
│   │   │   │   ├── default.scss
│   │   │   │   ├── fonts.scss
│   │   │   │   ├── form.scss
│   │   │   │   ├── htmx.scss
│   │   │   │   ├── rating.scss
│   │   │   │   ├── scrolltop.scss
│   │   │   │   ├── table.scss
│   │   │   │   └── ud.scss
│   │   │   └── project.scss
│   │   ├── sidebar.ts
│   │   ├── types/
│   │   │   └── index.d.ts
│   │   └── vendors.ts
│   ├── static/
│   │   ├── ckeditor/
│   │   │   └── ckeditor/
│   │   │       └── plugins/
│   │   ├── fonts/
│   │   │   ├── FiraSans-Black.ttf
│   │   │   ├── FiraSans-BlackItalic.ttf
│   │   │   ├── FiraSans-Bold.ttf
│   │   │   ├── FiraSans-BoldItalic.ttf
│   │   │   ├── FiraSans-ExtraBold.ttf
│   │   │   ├── FiraSans-ExtraBoldItalic.ttf
│   │   │   ├── FiraSans-ExtraLight.ttf
│   │   │   ├── FiraSans-ExtraLightItalic.ttf
│   │   │   ├── FiraSans-Italic.ttf
│   │   │   ├── FiraSans-Light.ttf
│   │   │   ├── FiraSans-LightItalic.ttf
│   │   │   ├── FiraSans-Medium.ttf
│   │   │   ├── FiraSans-MediumItalic.ttf
│   │   │   ├── FiraSans-Regular.ttf
│   │   │   ├── FiraSans-SemiBold.ttf
│   │   │   ├── FiraSans-SemiBoldItalic.ttf
│   │   │   ├── FiraSans-Thin.ttf
│   │   │   ├── FiraSans-ThinItalic.ttf
│   │   │   └── OFL.txt
│   │   ├── images/
│   │   │   ├── authentication/
│   │   │   │   ├── create-account.jpg
│   │   │   │   ├── login.jpg
│   │   │   │   └── reset-password.jpg
│   │   │   ├── blog/
│   │   │   │   ├── image-1.jpg
│   │   │   │   ├── image-2.jpg
│   │   │   │   ├── image-3.jpg
│   │   │   │   ├── image-4.jpg
│   │   │   │   └── image-7.jpg
│   │   │   ├── favicon.webp
│   │   │   ├── feed/
│   │   │   │   ├── image-1.jpg
│   │   │   │   └── image-2.jpg
│   │   │   ├── files/
│   │   │   │   ├── 01J3BAXFBTABT3VNAV3RPNZK7S-thumb-small.webp
│   │   │   │   ├── 01J3BAY4P9AZ1Y9GGSAAP2HQ1K-thumb-small.webp
│   │   │   │   ├── 01J6AR9XJKAQHET3AJYG9YPZ57-thumb-small.webp
│   │   │   │   ├── 01J7TV2G7719CVSTSW9T9M6F31-thumb-small.webp
│   │   │   │   ├── 01JF3DFZHDVHCNHVKXCGTD16KM-thumb-small.webp
│   │   │   │   ├── 01JG6WNTBZ27PWXBTXT46SF92N-thumb-small.webp
│   │   │   │   ├── 01JGSJVDCVF69YNEFZDS4CWM2Z-thumb-small.webp
│   │   │   │   ├── 01JH1A72V199K0YS3AN32BK9AF-thumb-small.webp
│   │   │   │   ├── 1018-a1b59c97e9a527a5.js.download
│   │   │   │   ├── 1169-83de5bd313f0d745.js.download
│   │   │   │   ├── 1935-a9e901cb5809e0c7.js.download
│   │   │   │   ├── 1976-491c4918643530b6.js.download
│   │   │   │   ├── 28901aff-thumb-small.webp
│   │   │   │   ├── 2ae37984-thumb-small.webp
│   │   │   │   ├── 3020-f6a8b63d56de75bd.js.download
│   │   │   │   ├── 3490-dbd90eb94426969b.js.download
│   │   │   │   ├── 39E9yO0.png
│   │   │   │   ├── 4250-12e477d786f54db6.js.download
│   │   │   │   ├── 4314-8d250c10e6e18ce7.js.download
│   │   │   │   ├── 4790-083a26793a15a81e.js.download
│   │   │   │   ├── 485b0913c49be1b0.css
│   │   │   │   ├── 5357f1a1-thumb-small.webp
│   │   │   │   ├── 5507-1d85edf06cead3e4.js.download
│   │   │   │   ├── 6067-f0ad1c1a7e2e0028.js.download
│   │   │   │   ├── 62df3d3f-thumb-small.webp
│   │   │   │   ├── 6329-38e186930142590a.js.download
│   │   │   │   ├── 6839-6e197913bd2382c6.js.download
│   │   │   │   ├── 6f88de8f10cbf30e.css
│   │   │   │   ├── 7519-ba99b4d71a543854.js.download
│   │   │   │   ├── 7612-8c22309576f45c87.js.download
│   │   │   │   ├── 7725-01ed917067c4810c.js.download
│   │   │   │   ├── 7854-e0f42b563d1c53bf.js.download
│   │   │   │   ├── 8053-51c191352484a71b.js.download
│   │   │   │   ├── 84fbfe7f-58f130442b743c99.js.download
│   │   │   │   ├── 8868-23ac1d29138a7bb8.js.download
│   │   │   │   ├── 9473bc3f-6587d3f148698ef8.js.download
│   │   │   │   ├── 9ab6b724-thumb-small.webp
│   │   │   │   ├── 9b59fdec-thumb-small.webp
│   │   │   │   ├── a45e4a4a-thumb-small.webp
│   │   │   │   ├── b8682ff8-thumb-small.webp
│   │   │   │   ├── d86aab25-thumb-small.webp
│   │   │   │   ├── da5433706d453ccc.css
│   │   │   │   ├── dfdeab7268d20d16.css
│   │   │   │   ├── e43c72fb-thumb-small.webp
│   │   │   │   ├── fb10ca24-thumb-small.webp
│   │   │   │   ├── fc6b81ea-thumb-small.webp
│   │   │   │   ├── global-error-a02be7fc5bd281fa.js.download
│   │   │   │   ├── js
│   │   │   │   ├── layout-1dd5b9b385960108.js.download
│   │   │   │   ├── layout-467c4bdbcf436890.js.download
│   │   │   │   ├── layout-f9fb224a2773328b.js.download
│   │   │   │   ├── logo.webp
│   │   │   │   ├── main-app-bdea5486d0b8262f.js.download
│   │   │   │   ├── not-found-f6aaf92e727fb7e2.js.download
│   │   │   │   ├── page-d3ba0f50bb6220b0.js.download
│   │   │   │   ├── page-f47a216b19a5e84e.js.download
│   │   │   │   ├── polyfills-78c92fac7aa8fdd8.js.download
│   │   │   │   ├── profile-picture.webp
│   │   │   │   ├── vcd15cbe7772f49c399c6a5babf22c1241717689176015
│   │   │   │   └── webpack-083d27093dff83d7.js.download
│   │   │   ├── flags/
│   │   │   │   ├── ad.svg
│   │   │   │   ├── ae.svg
│   │   │   │   ├── af.svg
│   │   │   │   ├── ag.svg
│   │   │   │   ├── ai.svg
│   │   │   │   ├── al.svg
│   │   │   │   ├── am.svg
│   │   │   │   ├── an.svg
│   │   │   │   ├── ao.svg
│   │   │   │   ├── ar.svg
│   │   │   │   ├── at.svg
│   │   │   │   ├── au.svg
│   │   │   │   ├── aw.svg
│   │   │   │   ├── ax.svg
│   │   │   │   ├── az.svg
│   │   │   │   ├── ba.svg
│   │   │   │   ├── bb.svg
│   │   │   │   ├── bd.svg
│   │   │   │   ├── be.svg
│   │   │   │   ├── bf.svg
│   │   │   │   ├── bg.svg
│   │   │   │   ├── bh.svg
│   │   │   │   ├── bi.svg
│   │   │   │   ├── bj.svg
│   │   │   │   ├── bm.svg
│   │   │   │   ├── bn.svg
│   │   │   │   ├── bo.svg
│   │   │   │   ├── br.svg
│   │   │   │   ├── bs.svg
│   │   │   │   ├── bt.svg
│   │   │   │   ├── bw.svg
│   │   │   │   ├── by.svg
│   │   │   │   ├── bz.svg
│   │   │   │   ├── ca.svg
│   │   │   │   ├── caf.svg
│   │   │   │   ├── cas.svg
│   │   │   │   ├── cd.svg
│   │   │   │   ├── ceu.svg
│   │   │   │   ├── cf.svg
│   │   │   │   ├── cg.svg
│   │   │   │   ├── ch.svg
│   │   │   │   ├── ci.svg
│   │   │   │   ├── cl.svg
│   │   │   │   ├── cm.svg
│   │   │   │   ├── cn.svg
│   │   │   │   ├── cna.svg
│   │   │   │   ├── co.svg
│   │   │   │   ├── coc.svg
│   │   │   │   ├── cr.svg
│   │   │   │   ├── csa.svg
│   │   │   │   ├── cu.svg
│   │   │   │   ├── cv.svg
│   │   │   │   ├── cy.svg
│   │   │   │   ├── cz.svg
│   │   │   │   ├── de.svg
│   │   │   │   ├── dj.svg
│   │   │   │   ├── dk.svg
│   │   │   │   ├── dm.svg
│   │   │   │   ├── do.svg
│   │   │   │   ├── dz.svg
│   │   │   │   ├── ec.svg
│   │   │   │   ├── ee.svg
│   │   │   │   ├── eg.svg
│   │   │   │   ├── er.svg
│   │   │   │   ├── es.svg
│   │   │   │   ├── et.svg
│   │   │   │   ├── eu.svg
│   │   │   │   ├── fi.svg
│   │   │   │   ├── fj.svg
│   │   │   │   ├── fk.svg
│   │   │   │   ├── fm.svg
│   │   │   │   ├── fr.svg
│   │   │   │   ├── ga.svg
│   │   │   │   ├── gb.svg
│   │   │   │   ├── gd.svg
│   │   │   │   ├── ge.svg
│   │   │   │   ├── gg.svg
│   │   │   │   ├── gh.svg
│   │   │   │   ├── gi.svg
│   │   │   │   ├── gm.svg
│   │   │   │   ├── gn.svg
│   │   │   │   ├── gq.svg
│   │   │   │   ├── gr.svg
│   │   │   │   ├── gt.svg
│   │   │   │   ├── gw.svg
│   │   │   │   ├── gy.svg
│   │   │   │   ├── hk.svg
│   │   │   │   ├── hn.svg
│   │   │   │   ├── hr.svg
│   │   │   │   ├── ht.svg
│   │   │   │   ├── hu.svg
│   │   │   │   ├── id.svg
│   │   │   │   ├── ie.svg
│   │   │   │   ├── il.svg
│   │   │   │   ├── im.svg
│   │   │   │   ├── in.svg
│   │   │   │   ├── iq.svg
│   │   │   │   ├── ir.svg
│   │   │   │   ├── is.svg
│   │   │   │   ├── it.svg
│   │   │   │   ├── je.svg
│   │   │   │   ├── jm.svg
│   │   │   │   ├── jo.svg
│   │   │   │   ├── jp.svg
│   │   │   │   ├── ke.svg
│   │   │   │   ├── kg.svg
│   │   │   │   ├── kh.svg
│   │   │   │   ├── km.svg
│   │   │   │   ├── kn.svg
│   │   │   │   ├── kp.svg
│   │   │   │   ├── kr.svg
│   │   │   │   ├── kw.svg
│   │   │   │   ├── ky.svg
│   │   │   │   ├── kz.svg
│   │   │   │   ├── la.svg
│   │   │   │   ├── lb.svg
│   │   │   │   ├── lc.svg
│   │   │   │   ├── li.svg
│   │   │   │   ├── lk.svg
│   │   │   │   ├── lr.svg
│   │   │   │   ├── ls.svg
│   │   │   │   ├── lt.svg
│   │   │   │   ├── lu.svg
│   │   │   │   ├── lv.svg
│   │   │   │   ├── ly.svg
│   │   │   │   ├── ma.svg
│   │   │   │   ├── mc.svg
│   │   │   │   ├── md.svg
│   │   │   │   ├── me.svg
│   │   │   │   ├── mg.svg
│   │   │   │   ├── mk.svg
│   │   │   │   ├── ml.svg
│   │   │   │   ├── mm.svg
│   │   │   │   ├── mn.svg
│   │   │   │   ├── mo.svg
│   │   │   │   ├── mr.svg
│   │   │   │   ├── ms.svg
│   │   │   │   ├── mt.svg
│   │   │   │   ├── mu.svg
│   │   │   │   ├── mv.svg
│   │   │   │   ├── mw.svg
│   │   │   │   ├── mx.svg
│   │   │   │   ├── my.svg
│   │   │   │   ├── mz.svg
│   │   │   │   ├── na.svg
│   │   │   │   ├── ne.svg
│   │   │   │   ├── ng.svg
│   │   │   │   ├── ni.svg
│   │   │   │   ├── nl.svg
│   │   │   │   ├── no.svg
│   │   │   │   ├── np.svg
│   │   │   │   ├── nz.svg
│   │   │   │   ├── om.svg
│   │   │   │   ├── pa.svg
│   │   │   │   ├── pe.svg
│   │   │   │   ├── pf.svg
│   │   │   │   ├── pg.svg
│   │   │   │   ├── ph.svg
│   │   │   │   ├── pk.svg
│   │   │   │   ├── pl.svg
│   │   │   │   ├── pr.svg
│   │   │   │   ├── pt.svg
│   │   │   │   ├── pw.svg
│   │   │   │   ├── py.svg
│   │   │   │   ├── qa.svg
│   │   │   │   ├── ro.svg
│   │   │   │   ├── rs.svg
│   │   │   │   ├── ru.svg
│   │   │   │   ├── rw.svg
│   │   │   │   ├── sa.svg
│   │   │   │   ├── sb.svg
│   │   │   │   ├── sc.svg
│   │   │   │   ├── sd.svg
│   │   │   │   ├── se.svg
│   │   │   │   ├── sg.svg
│   │   │   │   ├── sh.svg
│   │   │   │   ├── si.svg
│   │   │   │   ├── sk.svg
│   │   │   │   ├── sl.svg
│   │   │   │   ├── sm.svg
│   │   │   │   ├── sn.svg
│   │   │   │   ├── so.svg
│   │   │   │   ├── sr.svg
│   │   │   │   ├── st.svg
│   │   │   │   ├── sv.svg
│   │   │   │   ├── sy.svg
│   │   │   │   ├── sz.svg
│   │   │   │   ├── tc.svg
│   │   │   │   ├── td.svg
│   │   │   │   ├── tg.svg
│   │   │   │   ├── th.svg
│   │   │   │   ├── tj.svg
│   │   │   │   ├── tl.svg
│   │   │   │   ├── tm.svg
│   │   │   │   ├── tn.svg
│   │   │   │   ├── to.svg
│   │   │   │   ├── tr.svg
│   │   │   │   ├── tt.svg
│   │   │   │   ├── tw.svg
│   │   │   │   ├── tz.svg
│   │   │   │   ├── ua.svg
│   │   │   │   ├── ug.svg
│   │   │   │   ├── us.svg
│   │   │   │   ├── uy.svg
│   │   │   │   ├── uz.svg
│   │   │   │   ├── vc.svg
│   │   │   │   ├── ve.svg
│   │   │   │   ├── vg.svg
│   │   │   │   ├── vn.svg
│   │   │   │   ├── vu.svg
│   │   │   │   ├── ws.svg
│   │   │   │   ├── ww.svg
│   │   │   │   ├── ye.svg
│   │   │   │   ├── za.svg
│   │   │   │   ├── zm.svg
│   │   │   │   └── zw.svg
│   │   │   ├── illustrations/
│   │   │   │   ├── 404.svg
│   │   │   │   ├── 500.svg
│   │   │   │   ├── maintenance.svg
│   │   │   │   └── sign-in.svg
│   │   │   ├── kanban/
│   │   │   │   ├── task-1.jpg
│   │   │   │   ├── task-2.jpg
│   │   │   │   └── task-3.jpg
│   │   │   ├── logo-192x192.webp
│   │   │   ├── logo-512x512.webp
│   │   │   ├── logo.webp
│   │   │   ├── logos/
│   │   │   │   ├── crown.webp
│   │   │   │   ├── favicon.webp
│   │   │   │   ├── logo-192x192.webp
│   │   │   │   ├── logo-512x512.webp
│   │   │   │   ├── logo.webp
│   │   │   │   ├── manifest.json
│   │   │   │   └── profile-placeholder.svg
│   │   │   ├── manifest.json
│   │   │   ├── products/
│   │   │   │   ├── apple-imac-1.png
│   │   │   │   ├── apple-imac-2.png
│   │   │   │   ├── apple-imac-3.png
│   │   │   │   ├── imac.png
│   │   │   │   ├── ipad.png
│   │   │   │   ├── iphone.png
│   │   │   │   └── watch.png
│   │   │   ├── svg/
│   │   │   │   ├── black.webp
│   │   │   │   ├── book-open-cover.svg
│   │   │   │   ├── bookmark.svg
│   │   │   │   ├── crown.webp
│   │   │   │   ├── facebook.svg
│   │   │   │   ├── google.webp
│   │   │   │   ├── home.svg
│   │   │   │   ├── pinterest.svg
│   │   │   │   ├── twitter.svg
│   │   │   │   └── whatsapp.svg
│   │   │   ├── themesberg.svg
│   │   │   └── users/
│   │   │       ├── bonnie-green-2x.png
│   │   │       ├── bonnie-green.png
│   │   │       ├── helene-engels.png
│   │   │       ├── jese-leos-2x.png
│   │   │       ├── jese-leos.png
│   │   │       ├── joseph-mcfall.png
│   │   │       ├── lana-byrd.png
│   │   │       ├── leslie-livingston.png
│   │   │       ├── michael-gough.png
│   │   │       ├── neil-sims.png
│   │   │       ├── robert-brown.png
│   │   │       ├── roberta-casas-2x.png
│   │   │       ├── roberta-casas.png
│   │   │       └── thomas-lean.png
│   │   ├── img/
│   │   │   └── result.png
│   │   ├── js/
│   │   │   ├── buttons.js
│   │   │   ├── hyperscript.js
│   │   │   ├── jquery-3.6.3.min.js
│   │   │   ├── select2.css
│   │   │   ├── select2.js
│   │   │   ├── sweetalert2.all.min.js
│   │   │   ├── sweetalert2.min.css
│   │   │   └── theme.js
│   │   └── main.js
│   ├── templates/
│   │   ├── 403.html
│   │   ├── 403_csrf.html
│   │   ├── 404.html
│   │   ├── 505.html
│   │   ├── account/
│   │   │   ├── base_manage_password.html
│   │   │   ├── login.html
│   │   │   ├── password_reset.html
│   │   │   └── signup.html
│   │   ├── allauth/
│   │   │   ├── elements/
│   │   │   │   ├── alert.html
│   │   │   │   ├── badge.html
│   │   │   │   ├── button.html
│   │   │   │   ├── field.html
│   │   │   │   ├── fields.html
│   │   │   │   ├── panel.html
│   │   │   │   └── table.html
│   │   │   └── layouts/
│   │   │       ├── entrance.html
│   │   │       └── manage.html
│   │   ├── base.html
│   │   ├── bookmark/
│   │   │   ├── base.html
│   │   │   └── list.html
│   │   ├── chapters/
│   │   │   ├── add_chapter.html
│   │   │   ├── base.html
│   │   │   ├── chapter_list.html
│   │   │   ├── delete.html
│   │   │   ├── detail.html
│   │   │   └── update_chapter.html
│   │   ├── comics/
│   │   │   ├── add_comic.html
│   │   │   ├── base.html
│   │   │   ├── comic_list copy 2.html
│   │   │   ├── comic_list copy.html
│   │   │   ├── comic_list.html
│   │   │   ├── delete.html
│   │   │   ├── detail.html
│   │   │   ├── update-chapter.html
│   │   │   ├── update_comic.html
│   │   │   └── upload-image.html
│   │   ├── error.html
│   │   ├── home/
│   │   │   ├── base.html
│   │   │   ├── digital.html
│   │   │   ├── index.html
│   │   │   ├── privacy.html
│   │   │   ├── series.html
│   │   │   └── terms.html
│   │   ├── partials/
│   │   │   ├── base/
│   │   │   │   ├── bookmarks.html
│   │   │   │   ├── footer.html
│   │   │   │   ├── header.html
│   │   │   │   ├── message.html
│   │   │   │   ├── script.html
│   │   │   │   ├── scrolltop.html
│   │   │   │   ├── style.html
│   │   │   │   └── topbar.html
│   │   │   ├── bookmark/
│   │   │   │   ├── grid.html
│   │   │   │   ├── grid_item.html
│   │   │   │   ├── hero.html
│   │   │   │   ├── pagination.html
│   │   │   │   └── rating.html
│   │   │   ├── chapter/
│   │   │   │   ├── comments copy 2.html
│   │   │   │   ├── comments copy.html
│   │   │   │   ├── comments.html
│   │   │   │   ├── detail.html
│   │   │   │   ├── downbutton.html
│   │   │   │   ├── footer.html
│   │   │   │   ├── item.html
│   │   │   │   ├── navbar.html
│   │   │   │   ├── related.html
│   │   │   │   └── topbutton.html
│   │   │   ├── chapters/
│   │   │   │   ├── container.html
│   │   │   │   ├── create.html
│   │   │   │   ├── form.html
│   │   │   │   ├── hero.html
│   │   │   │   ├── images-inline-form.html
│   │   │   │   ├── images-inline.html
│   │   │   │   ├── pagination.html
│   │   │   │   ├── table.html
│   │   │   │   └── update.html
│   │   │   ├── comic/
│   │   │   │   ├── bookmark.html
│   │   │   │   ├── chapters.html
│   │   │   │   ├── comments.html
│   │   │   │   ├── detail.html
│   │   │   │   ├── navbar.html
│   │   │   │   ├── rating.html
│   │   │   │   └── related.html
│   │   │   ├── comics/
│   │   │   │   ├── chapters-inline-form.html
│   │   │   │   ├── chapters-inline.html
│   │   │   │   ├── container.html
│   │   │   │   ├── create.html
│   │   │   │   ├── custom_table.html
│   │   │   │   ├── form.html
│   │   │   │   ├── hero copy.html
│   │   │   │   ├── hero.html
│   │   │   │   ├── images-inline-form.html
│   │   │   │   ├── images-inline.html
│   │   │   │   ├── pagination.html
│   │   │   │   ├── table_actions.html
│   │   │   │   ├── table_comic.html
│   │   │   │   └── update.html
│   │   │   ├── comics copy/
│   │   │   │   ├── container.html
│   │   │   │   ├── create.html
│   │   │   │   ├── custom_table.html
│   │   │   │   ├── form copy 2.html
│   │   │   │   ├── form copy.html
│   │   │   │   ├── form.html
│   │   │   │   ├── hero copy.html
│   │   │   │   ├── hero.html
│   │   │   │   ├── images-inline-form.html
│   │   │   │   ├── images-inline.html
│   │   │   │   ├── pagination.html
│   │   │   │   ├── table.html
│   │   │   │   ├── table_actions.html
│   │   │   │   ├── table_comic.html
│   │   │   │   ├── table_comic_image.html
│   │   │   │   └── update.html
│   │   │   ├── home/
│   │   │   │   ├── index/
│   │   │   │   └── series/
│   │   │   ├── htmx/
│   │   │   │   └── spinner.html
│   │   │   ├── user/
│   │   │   │   ├── detail.html
│   │   │   │   ├── left-item.html
│   │   │   │   └── right-item.html
│   │   │   ├── users/
│   │   │   │   ├── container.html
│   │   │   │   ├── create.html
│   │   │   │   ├── form.html
│   │   │   │   ├── hero.html
│   │   │   │   ├── pagination.html
│   │   │   │   ├── table.html
│   │   │   │   └── update.html
│   │   │   └── widgets/
│   │   │       ├── attrs.html
│   │   │       ├── checkbox_option.html
│   │   │       ├── checkbox_select.html
│   │   │       ├── ckwidget.html
│   │   │       ├── custom_image_widget copy.html
│   │   │       ├── custom_image_widget.html
│   │   │       ├── input.html
│   │   │       ├── input_option.html
│   │   │       ├── multiple_input.html
│   │   │       ├── radio.html
│   │   │       └── radio_option.html
│   │   └── users/
│   │       ├── add_user.html
│   │       ├── base.html
│   │       ├── delete.html
│   │       ├── detail.html
│   │       ├── update_user.html
│   │       ├── user_list copy.html
│   │       └── user_list.html
│   └── users/
│       ├── __init__.py
│       ├── adapters.py
│       ├── admin.py
│       ├── apps.py
│       ├── context_processors.py
│       ├── decorators.py
│       ├── forms.py
│       ├── migrations/
│       │   ├── 0001_initial.py
│       │   └── __init__.py
│       ├── models.py
│       ├── signals.py
│       ├── tasks.py
│       ├── tests/
│       │   ├── __init__.py
│       │   ├── factories.py
│       │   ├── test_admin.py
│       │   ├── test_forms.py
│       │   ├── test_models.py
│       │   ├── test_tasks.py
│       │   ├── test_urls.py
│       │   └── test_views.py
│       ├── urls.py
│       ├── utils.py
│       ├── views.py
│       └── widgets.py
├── api.sqlite3
├── API_REFERENCE.md
├── ARCHITECTURE.md
├── CHANGELOG.md
├── chapters.json
├── code-exemplars.md
├── comics.json
├── compose/
│   ├── local/
│   │   ├── django/
│   │   │   ├── celery/
│   │   │   │   ├── beat/
│   │   │   │   ├── flower/
│   │   │   │   └── worker/
│   │   │   ├── Dockerfile
│   │   │   └── start
│   │   ├── docs/
│   │   │   ├── Dockerfile
│   │   │   └── start
│   │   └── node/
│   │       └── Dockerfile
│   └── production/
│       ├── aws/
│       │   ├── Dockerfile
│       │   └── maintenance/
│       │       ├── download
│       │       └── upload
│       ├── django/
│       │   ├── celery/
│       │   │   ├── beat/
│       │   │   ├── flower/
│       │   │   └── worker/
│       │   ├── Dockerfile
│       │   ├── entrypoint
│       │   └── start
│       ├── postgres/
│       │   ├── Dockerfile
│       │   └── maintenance/
│       │       ├── _sourced/
│       │       ├── backup
│       │       ├── backups
│       │       ├── restore
│       │       └── rmbackup
│       └── traefik/
│           ├── Dockerfile
│           └── traefik.yml
├── config/
│   ├── __init__.py
│   ├── celery_app.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── local.py
│   │   ├── production.py
│   │   └── test.py
│   ├── urls.py
│   ├── utils.py
│   └── wsgi.py
├── CONTRIBUTING.md
├── CONTRIBUTORS.txt
├── copilot-instructions.md
├── crawler/
│   ├── __init__.py
│   ├── addon.py
│   ├── extensions.py
│   ├── items.py
│   ├── management/
│   │   ├── __init__.py
│   │   └── commands/
│   │       ├── __init__.py
│   │       ├── crawl.py
│   │       ├── crawls.py
│   │       ├── load.py
│   │       └── read.py
│   ├── middlewares/
│   │   ├── __init__.py
│   │   ├── default.py
│   │   ├── retry.py
│   │   ├── rotate.py
│   │   └── sele.py
│   ├── pipelines/
│   │   ├── __init__.py
│   │   ├── appsdb.py
│   │   ├── download.py
│   │   ├── dupelicate.py
│   │   ├── images/
│   │   │   ├── __init__.py
│   │   │   ├── pipe copy.py
│   │   │   └── pipe.py
│   │   └── redis/
│   │       ├── __init__.py
│   │       ├── connection.py
│   │       ├── defaults.py
│   │       └── red.py
│   ├── settings.py
│   ├── spiders/
│   │   ├── __init__.py
│   │   ├── asuracomic.py
│   │   ├── asuracomics.py
│   │   ├── bs4spider.py
│   │   └── html.py
│   ├── tasks.py
│   └── utils.py
├── cross-linking-report.md
├── DATABASE_SCHEMA.md
├── DEPLOYMENT_GUIDE.md
├── DEVELOPMENT_GUIDE.md
├── docker-compose.docs.yml
├── docker-compose.local.yml
├── docker-compose.production.yml
├── docs/
│   ├── __init__.py
│   ├── audit-report.md
│   ├── CODE_DOCS.md
│   ├── conf.py
│   ├── django-scrapy-triage-context.md
│   ├── howto.rst
│   ├── index.rst
│   ├── make.bat
│   ├── Makefile
│   ├── Project_Architecture/
│   │   ├── exemplars.md
│   │   ├── Project_Architecture_Blueprint.md
│   │   ├── Project_Folder_Structure.md
│   │   ├── Technology_Stack_Blueprint.md
│   │   └── Workflow_Analysis.md
│   ├── PROJECT_DOCS.docx
│   ├── PROJECT_DOCS.md
│   └── users.rst
├── execution-summary.md
├── fixtures/
│   └── db.json
├── folder-structure.md
├── geckodriver.exe
├── install_gecko.sh
├── justfile
├── LICENSE
├── locale/
│   ├── en/
│   │   └── LC_MESSAGES/
│   │       └── django.po
│   ├── fr/
│   │   └── LC_MESSAGES/
│   │       └── django.po
│   ├── ja/
│   │   └── LC_MESSAGES/
│   │       └── django.po
│   ├── pt/
│   │   └── LC_MESSAGES/
│   │       └── django.po
│   └── README.md
├── Makefile
├── manage.py
├── merge_production_dotenvs_in_dotenv.py
├── package-lock.json
├── package.json
├── postcss.config.cjs
├── Procfile
├── project-workflow.md
├── pyproject.toml
├── README.md
├── requirements/
│   ├── base.txt
│   ├── local.txt
│   └── production.txt
├── requirements.txt
├── RESEARCH_REPORT.md
├── runtime.txt
├── scrapy.cfg
├── SECURITY.md
├── sel.py
├── SETUP_GUIDE.md
├── tailwind.config.cjs
├── technology-stack.md
├── TESTING_GUIDE.md
├── tests/
│   ├── __init__.py
│   ├── test_cases.py
│   ├── test_merge_production_dotenvs_in_dotenv.py
│   └── test_middlewares.py
├── tsconfig.json
├── validation-report.md
└── webpack/
    ├── common.config.js
    ├── dev.config.js
    └── prod.config.js
```

## Key Directories

| Directory               | Purpose          | Convention                 |
| ----------------------- | ---------------- | -------------------------- |
| `<app>/`                | Django apps      | lowercase, plural          |
| `config/` / `settings/` | Settings modules | base/local/production      |
| `templates/`            | HTML templates   | app-specific subdirs       |
| `static/`               | Static assets    | Collected by collectstatic |

## Naming Conventions

- **Directories:** kebab-case (multi-word) or lowercase
- **Files:** Match language convention (PascalCase for React, snake_case for Python)
- **Configs:** lowercase with extension (.json, .yaml, .toml)

## File Placement Patterns

- Tests: co-located (`__tests__/`) or mirrored `tests/` structure
- Types: `types/` or co-located with implementation
- Config: Root level for tool configs

---

_Generated by agents-system-prompt-context-fix-runner_
