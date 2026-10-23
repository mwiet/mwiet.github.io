---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if site.author.googlescholar %}
  <div class="wordwrap">You can also find my articles on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</div>
{% endif %}

{% include base_path %}

{% for group in site.data.authorship %}
  {% assign pubs = site.publications | where: "authorship", group.key | sort: "date" | reverse %}
  {% if pubs.size > 0 %}
  <h2>{{ group.title }}</h2>
  {% for post in pubs %}
    {% include archive-single.html %}
  {% endfor %}
  {% endif %}
{% endfor %}
