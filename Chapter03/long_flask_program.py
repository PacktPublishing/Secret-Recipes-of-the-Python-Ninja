@app.route("/") # Root (default) page to display when landing on web site
@app.route("/page/<int:page>") # Specific site page
@login_required # Force authentication
def entries(page=1):
    """
    Query the database entries of the blog.

    :param page: The page number of the site.
    :return: Template page with the number of entries specified, Next/Previous links, page number, and total number of
    pages in the site
    """
    # Zero-indexed page
    default_entries = 10
    max_entries = 50

    # Set the number of entries displayed per page
    try:
        entry_limit = int(request.args.get('limit', default_entries)) # Get the limit from HTML argument 'limit'
        assert entry_limit > 0 # Ensure positive number
        assert entry_limit <= max_entries # Ensure entries don't exceed max value
    except (ValueError, AssertionError): # Use default value if number of entries doesn't meet expectations
        entry_limit = default_entries

    page_index = page - 1

    count = session.query(Entry).count()

    start = page_index * PAGINATE_BY # Index of first entry on page
    end = start + PAGINATE_BY # Index of last entry on page
    total_pages = (count - 1) // PAGINATE_BY + 1 # Total number of pages
    has_next = page_index < total_pages - 1 # Does following page exit?
    has_prev = page_index > 0 # Does previous page exist?

    entries = session.query(Entry)
    entries = entries.order_by(Entry.datetime.desc())
    entries = entries[start:end]

    return render_template("entries.html",
                           entries=entries,
                           has_next=has_next,
                           has_prev=has_prev,
                           page=page,
                           total_pages=total_pages
                           )
