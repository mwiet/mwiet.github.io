---
permalink: /
title: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<div class="aside">
  <head>
    <title></title>
    <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.3">
    <style scoped>
      @import url('https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css');
    </style>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <style>
      .carousel {
        width: 60%;
        margin: 0;
      }
      .carousel-inner {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 420px;
        position: relative;
      }
      .carousel-inner img {
        max-height: 100%;
        max-width: 100%;
        height: auto;
        width: auto;
        margin: 0 auto;
        display: block;
      }
      .carousel-caption {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent black background */
        color: #fff; /* White text */
        padding: 28px; /* Add some padding */
        text-align: left; /* Center the text */
        margin: 0;
      }
    </style>
  </head>
  <div class="container">
    <div id="myCarousel" class="carousel slide" data-ride="carousel">
      <!-- Indicators -->
      <ol class="carousel-indicators">
        <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
        <li data-target="#myCarousel" data-slide-to="1"></li>
        <li data-target="#myCarousel" data-slide-to="2"></li>
      </ol>
      <div class="carousel-inner">
        <div class="item active">
          <img src="../images/webb_seahorse.jpg" alt="JWST observation of the cosmic seahorse. Credit: ESA/Webb, NASA & CSA, J. Rigby" height="500px">
          <div class="carousel-caption">
            <p id="carousel-caption-text">JWST observation of the cosmic seahorse. Credit: ESA/Webb, NASA & CSA, J. Rigby</p>
          </div>
        </div>
        <div class="item">
          <img src="../images/kids_sky.jpg" alt="ESO Kilo-Degree Survey weak lensing data. Credit: ESO KiDS" height="500px">
          <div class="carousel-caption">
            <p id="carousel-caption-text">ESO Kilo-Degree Survey weak lensing data. Credit: ESO KiDS</p>
          </div>
        </div>
        <div class="item">
          <img src="../images/kids_sbi_results.jpg" alt="Latest cosmological constraints from SBI analysis of KiDS-1000." height="500px">
          <div class="carousel-caption">
            <p id="carousel-caption-text">Latest cosmological constraints from SBI analysis of KiDS-1000.</p>
          </div>
        </div>
        
      </div>
      <a class="left carousel-control" href="#myCarousel" data-slide="prev">
        <span class="glyphicon glyphicon-chevron-left"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a class="right carousel-control" href="#myCarousel" data-slide="next">
        <span class="glyphicon glyphicon-chevron-right"></span>
        <span class="sr-only">Next</span>
      </a>
    </div>
  </div>
  <script>
    // JavaScript to update the caption text based on the current image
    $('#myCarousel').on('slide.bs.carousel', function (e) {
      var altText = $(e.relatedTarget).find('img').attr('alt');
      $('#carousel-caption-text').text(altText);
    });
  </script>
</div>

About me
==============

My research focuses on cosmology, understanding dark matter as well as its effect on the formation of large-scale and small-scale structure. I am interested in modelling the observable effects such as strong gravitational lensing, weak gravitational lensing, and galaxy clustering. To this end, I develop simulations of LSS, galaxy clusters, galaxies as well as simulation-based inference pipelines with future galaxy surveys in mind, together with other various projects.

Understanding the formation and evolution of structure at the largest scales allows us to determine how gravity and dark matter act on the cosmology of the Universe. Simultaneously, studying substucture formation at the scale of galaxies probes the nature of dark matter at small scales. Therefore, we can test Einstein's theory of general relativity as well as the theory of cold dark matter.

I am a member of the following collaborations:

[<img src="../images/Euclid_consortium_logo.png" width="200" />](https://www.euclid-ec.org/)
[<img src="../images/Euclid_logo_pillars.png" width="120" />](https://www.cosmos.esa.int/web/euclid)
[<img src="../images/COSMOSWeb_logo.png" width="200" />](https://cosmos.astro.caltech.edu/page/cosmosweb)
[<img src="../images/KiDS_logo.jpg" width="200" />](https://kids.strw.leidenuniv.nl/)


