video/                  # Top-level package
    __init__.py         # Top-level initialization
    formats/            # Sub-package for file formats
        __init__.py     # Package-level initialization
        avi_in.py
        avi_out.py
        mpg2_in.py
        mpg2_out.py
        webm_in.py
        webm_out.py
    effects/             # Sub-package for video effects
        specialFX/       # Sub-package for special effects
            __init__.py
            sepia.py
            mosaic.py
            old_movie.py
            glass.py
            pencil.py
            tv.py
        transform/        # Sub-package for transform effects
            __init__.py
            flip.py
            skew.py
            rotate.py
            mirror.py
            wave.py
            broken_glass.py
        draw/              # Sub-package for draw effects
            __init__.py
            rectangle.py
            ellipse.py
            border.py
            line.py
            polygon.py
