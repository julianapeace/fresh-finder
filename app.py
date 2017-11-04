from flask import Flask, render_template, request
import os
import db
import json

# Make sure to source the .env file
# hint:
# source .env

PORT = int(os.environ.get('PORT', '5000'))


# def do_the_search():
# define here once twitter json data is ready
# use python.request method and return results


def main():
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object(os.environ['APP_SETTINGS'])
    engine = db.create_engine(app.config)

    @app.route('/', methods=('GET', 'POST'))
    def home():
        return render_template('search.html')

    @app.route('/search', methods=['POST'])
    def search():
        results = do_the_search()
        return render_template('search.html', {'results': results})

    app.run(host='0.0.0.0', port=PORT, debug=True)


if __name__ == '__main__':
    main()
