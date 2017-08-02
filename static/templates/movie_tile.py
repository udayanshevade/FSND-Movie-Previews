# A single movie entry html template
movie_tile_content = '''
<a class="carousel-item movie-tile center-align grey-text text-darken-4">
    <div class="card hoverable">
        <div class="card-image">
            <img class="movie-image" src="{poster_image_url}">
            <h2 class="card-title">{movie_title}</h2>
        </div>
        <div class="card-content">
            <p class="movie-description flow-text">{movie_description}</p>
        </div>
        <div class="card-action cyan darken-2">
            <!-- Modal trigger -->
            <button data-target="trailer" class="btn btn-floating cyan lighten-1 modal-trigger" data-trailer-youtube-id="{trailer_youtube_id}">
                <i class="material-icons right">play_arrow</i>
            </button>
        </div>
    </div>
</a>
'''