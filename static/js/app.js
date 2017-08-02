$(function() {
  // Default carousel display options
  var CAROUSEL_OPTIONS = {
    duration: 225,
    dist: -200,
    shift: 50,
    padding: 150,
  };
  var carouselInitialized;

  /**
   * @description: Dynamically sizes the carousel slider
   * based on the height of the tallest carousel item.
   */
  function setCarouselHeight() {
    $('.carousel').height(function() {
      var heights = jQuery.makeArray(
        $('.carousel-item').map(function() {
          return $(this).height();
        })
      );
      var height = heights.reduce(function(a, b) {
        return Math.max(a, b);
      }, 0);
      return height;
    });
  }

  /**
   * @description: Starts/refreshes the carousel component
   */
  function initializeCarousel(options) {
    if (carouselInitialized) $('.carousel').carousel('destroy');
    // Adjust height before initializing carousel
    setCarouselHeight();
    $('.carousel').carousel(options);
  }

  // Initialize modal and add listeners
  function initializeModal() {
    $('.modal').modal();

    // Pause the video when the modal is closed
    $('.hanging-close, .modal-overlay, .modal').click(function (event) {
        // Remove the src so the player itself gets removed, as this is the only
        // reliable way to ensure the video stops playing in IE
        $("#trailer-video-container").empty();
    });

    // Start playing the video whenever the trailer modal is opened
    $('.modal-trigger').click(function (event) {
        var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
        var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
        $("#trailer-video-container").empty().append($("<iframe></iframe>", {
          'id': 'trailer-video',
          'type': 'text-html',
          'src': sourceUrl,
          'frameborder': 0
        }));
    });

    $(document).keyup(function(event) {
      if (event.keyCode === 27) {
        $("#trailer-video-container").empty();
        $('.modal').modal('close');
      }
    });
  }

  initializeModal();
  initializeCarousel();
  // If browser is resized, set carousel height again
  $(document).on('resize', function() {
    initializeCarousel(CAROUSEL_OPTIONS);
  });
});