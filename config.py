import os

current_dir = os.path.dirname(os.path.abspath(__file__))

config = {
    '/index.js': {
        'tools.staticfile.on': True,
        'tools.staticfile.filename': os.path.join(current_dir, 'static', 'js', 'index.js'),
    },
    '/style.css': {
        'tools.staticfile.on': True,
        'tools.staticfile.filename': os.path.join(current_dir, 'static', 'css', 'style.css'),
    }
}
