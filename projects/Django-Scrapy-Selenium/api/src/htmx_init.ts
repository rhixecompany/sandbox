import htmx from "htmx.org";

window.htmx = htmx;
window.htmx.config.historyEnabled = true;
window.htmx.config.historyCacheSize = 0;
window.htmx.config.refreshOnHistoryMiss = true;
window.htmx.config.defaultSwapStyle = "outerHTML";
// window.htmx.config.allowEval = true;
// window.htmx.config.useTemplateFragments = true;
// window.htmx.config.globalViewTransitions = true;
// window.htmx.config.selfRequestsOnly = true;
window.htmx.config.allowScriptTags = true;
// window.htmx.config.ignoreTitle = false;
// window.htmx.config.timeout = 0;
