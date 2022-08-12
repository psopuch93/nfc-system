from website import create_app

app = create_app()

#Only if we run this file -> execute Flask app.
#Every change in server is applying up to date

if __name__ == '__main__':
    app.run(debug=True)