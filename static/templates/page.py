# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Fresh Tomatoes!</title>
    <!-- Materialize -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.1/css/materialize.min.css">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link rel="stylesheet" href="static/css/styles.css">
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    {trailer_modal_content}

    <!-- Main Page Content -->
    <nav class="navbar">
      <div class="nav-wrapper cyan darken-2">
        <a href="" class="brand-logo">Sneak Picks</a>
      </div>
    </nav>
    <div class="carousel">
      {movie_tiles}
    </div>
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.1/js/materialize.min.js"></script>
    <script src="static/js/app.js"></script>
  </body>
</html>
'''
