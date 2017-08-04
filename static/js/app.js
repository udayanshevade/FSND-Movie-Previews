$(function() {
  $('.preloader').removeClass('visible');
  // Default carousel display options
  var CAROUSEL_OPTIONS = {
    duration: 200,
    dist: -200,
    shift: 125,
    padding: 200,
  };
  var NUM_MOVIES = 7;
  var oldNum = 0;
  var carouselInitialized;

  /**
   * @description: Dynamically sizes the carousel slider
   * based on the height of the tallest carousel item.
   */
  function setCarouselHeight(type) {
    var typeSelector = '#' + type + '-carousel';
    var childrenSelector = typeSelector + ' ' + '.carousel-item';
    $(typeSelector).height(function() {
      var heights = jQuery.makeArray(
        $(childrenSelector).map(function() {
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
   * Sets height for multiple targets
   */
  function setCarouselHeights() {
    for (i = 0, len = arguments.length; i < len; i += 1) {
      setCarouselHeight(arguments[i]);
    }
  }

  /**
   * @description: Starts/refreshes the carousel component
   */
  function initializeCarousels(options) {
    if (carouselInitialized) $('.carousel').carousel('destroy');
    // Adjust height before initializing carousel
    setCarouselHeights('movies', 'shows');
    carouselInitialized = true;
    $('.carousel').carousel(options);
    // sample animation on load
    $('.carousel').carousel('set', Math.round($('.carousel-item').length / 2));
  }

  // Initialize modal and add listeners
  function initializeModal() {
    $('.modal').modal();

    // Pause the video when the modal is closed
    $('.hanging-close, .modal-overlay').click(function (event) {
        // Remove the src so the player itself gets removed, as this is the only
        // reliable way to ensure the video stops playing in IE
        $("#trailer-video-container").empty();
    });

    // Start playing the video whenever the trailer modal is opened
    $('.modal-trigger').click(function (event) {
        // prevent accidental video trigger on unselected carousel items
        if ($(this).parents('.carousel-item').hasClass('active')) {
          var trailerYouTubeId = $(this).attr('data-trailer-youtube-id');
          var sourceUrl = 'https://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
          $("#trailer-video-container").empty().append($("<iframe></iframe>", {
            'id': 'trailer-video',
            'type': 'text-html',
            'src': sourceUrl,
            'frameborder': 0
          }));
        }
    });

    $(document).keyup(function(event) {
      if (event.keyCode === 27) {
        $("#trailer-video-container").empty();
        $('.modal').modal('close');
      }
    });
  }

  // Prevents consecutive duplicate numbers
  function randomizeNumber() {
    var newNum = Math.floor(Math.random() * NUM_MOVIES);
    if (oldNum === newNum) return randomizeNumber();
    oldNum = newNum;
    return newNum;
  }

  // Add click listener for randomizer button
  function initializeShufflers() {
    $('.randomizer').click(function() {
      var newNum = randomizeNumber();
      $(this).parent('.random-container').prev('.carousel').carousel('set', newNum);
    });
  }

  // Loads the parallax functionality
  function initializeParallax() {
    $('.parallax').parallax();
  }

  initializeModal();
  initializeCarousels();
  // If browser is resized, set carousel height again
  $(document).on('resize', function() {
    initializeCarousels(CAROUSEL_OPTIONS);
  });
  initializeShufflers();
  initializeParallax();
});