from flask import Flask, render_template, request
import os
import db
import json

# Make sure to source the .env file
# hint:
# source .env

PORT = int(os.environ.get('PORT', '5000'))


def main():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    engine = db.create_engine(app.config)

    # @app.route('/', methods=('GET', 'POST'))
    # def hello():
    #     return render_template('index.html')

    @app.route('/', methods=['GET', 'POST'])
    def search():
        if request.method == 'POST':
            do_the_search()
        else:
            return render_template('index.html')

    app.run(host='0.0.0.0', port=PORT, debug=True)


if __name__ == '__main__':
    main()
