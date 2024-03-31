var multipleCardCarousel = document.querySelector(
    "#carouselExampleControls"
  );
  if (window.matchMedia("(min-width: 768px)").matches) {
    var carousel = new bootstrap.Carousel(multipleCardCarousel, {
      interval: false,
    });
    var carouselWidth = $(".carousel-inner")[0].scrollWidth;
    var cardWidth = $(".carousel-item").width();
    var scrollPosition = 0;
    $("#carouselExampleControls .carousel-control-next").on("click", function () {
      if (scrollPosition < carouselWidth - cardWidth * 4) {
        scrollPosition += cardWidth;
        $("#carouselExampleControls .carousel-inner").animate(
          { scrollLeft: scrollPosition },
          600
        );
      }
    });
    $("#carouselExampleControls .carousel-control-prev").on("click", function () {
      if (scrollPosition > 0) {
        scrollPosition -= cardWidth;
        $("#carouselExampleControls .carousel-inner").animate(
          { scrollLeft: scrollPosition },
          600
        );
      }
    });
  } else {
    $(multipleCardCarousel).addClass("slide");
  
    // $(document).on("submit" , "form.ajax" , function (e) {
    //   e.preventDefault();
    //   var $this = $(this);

    //   var url = $this.attr("action");
    //   var method = $this.attr("method");

    //   jQuery.ajax({
    //       type: method,
    //       url: url,
    //       dataType: "json",
    //       data: new FormData(this),
    //       processData: false,
    //       contentType: false,
    //       Cache: false,
    //       success:function(data) {
    //           let title = data["title"];
    //           let message = data["message"];

    //           Swal.fire({
    //               icon: "success",
    //               title: title,
    //               text: message,
    //             });
    //       },
    //       error:function(error) {
    //           console.log("Failure");
    //       },
    //   });

  // });
  }