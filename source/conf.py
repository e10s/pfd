project = "部分分数分解いみじ"
copyright = "2023, electrolysis"
author = "electrolysis"

extensions = [
    "sphinx.ext.githubpages",
    "sphinx.ext.mathjax",
    "sphinxcontrib.bibtex",
    "sphinx_proof",
    "sphinx_togglebutton",
    "sphinx_last_updated_by_git",
    "sphinx_sitemap",
    "sphinxext.opengraph",
]
templates_path = ["_templates"]
# exclude_patterns = []
numfig = True
numfig_secnum_depth = 3

language = "ja"

html_theme = "sphinx_book_theme"
html_theme_options = {
    "show_toc_level": 2,
}

html_static_path = ["_static"]
html_css_files = [
    "custom.css",
]
html_title = project
html_baseurl = "https://e10s.github.io/pfd/"
html_extra_path = ["googlefb2b68adba636a34.html"]
html_last_updated_fmt = ""

mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"
mathjax3_config = {
    "loader": {"load": ["ui/lazy", "[tex]/physics", "[tex]/empheq"]},
    "tex": {
        "packages": {
            "[+]": [
                "physics",
                "empheq",
            ]
        },
        "physics": {"italicdiff": True},
        "macros": {"stirI": ["{\\genfrac{[}{]}{0pt}{}{#1}{#2}}", 2]},
    },
    "svg": {"fontCache": "global"},
}

bibtex_bibfiles = ["article_refs.bib", "book_refs.bib", "web_refs.bib"]
bibtex_footbibliography_header = ".. rubric:: 参考文献"

sitemap_url_scheme = "{link}"

ogp_site_url = html_baseurl
