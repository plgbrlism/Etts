from flask import Blueprint, render_template
from .services import get_all_snippets, get_snippet_by_id

# Define the Blueprint. 
# Note: We tell it where to find templates specifically for this module.
library_bp = Blueprint('library', __name__, template_folder='templates')

@library_bp.route('/')
@library_bp.route('/snippet/<int:snippet_id>')
def index(snippet_id=None):
    snippets = get_all_snippets()
    
    active_snippet = None
    if snippet_id:
        active_snippet = get_snippet_by_id(snippet_id)
    elif snippets:
        active_snippet = snippets[0] # Default to first
        
    return render_template('library/index.html', snippets=snippets, active_snippet=active_snippet)